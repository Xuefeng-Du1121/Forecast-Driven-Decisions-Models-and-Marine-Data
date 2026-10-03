"""Generic residual-distribution structures requiring caller-supplied state.

No fitting, data selection, experiment configuration, or stored parameters are
provided. Sampling noise must also be supplied by the caller.
"""

import numpy as np


class GaussianResidualModel:
    """Add a caller-supplied Gaussian residual to a supplied baseline location."""

    def __init__(self, mean, covariance):
        mean = np.asarray(mean, dtype=float)
        covariance = np.asarray(covariance, dtype=float)
        if mean.ndim != 1 or not mean.size or not np.isfinite(mean).all():
            raise ValueError('mean must be a finite nonempty vector')
        if covariance.shape != (mean.size, mean.size) or not np.isfinite(covariance).all():
            raise ValueError('covariance must match the supplied mean dimension')
        if not np.allclose(covariance, covariance.T):
            raise ValueError('covariance must be symmetric')
        self._mean = mean.copy()
        self._root = np.linalg.cholesky(covariance)

    @property
    def dimension(self):
        return self._mean.size

    def sample(self, baseline, standard_normal):
        """Transform externally supplied independent standard-normal draws."""
        baseline = np.asarray(baseline, dtype=float)
        noise = np.asarray(standard_normal, dtype=float)
        if baseline.shape != (self.dimension,) or not np.isfinite(baseline).all():
            raise ValueError('baseline must match the model dimension')
        if noise.ndim != 2 or noise.shape[1] != self.dimension or not np.isfinite(noise).all():
            raise ValueError('noise must be a finite sample-by-dimension matrix')
        return baseline + self._mean + noise @ self._root.T


class MixtureResidualModel:
    """Combine caller-supplied Gaussian components and mixture probabilities."""

    def __init__(self, probabilities, components):
        probabilities = np.asarray(probabilities, dtype=float)
        components = tuple(components)
        if not components or any(not isinstance(c, GaussianResidualModel) for c in components):
            raise ValueError('components must contain GaussianResidualModel instances')
        if probabilities.shape != (len(components),) or not np.isfinite(probabilities).all():
            raise ValueError('one finite probability is required per component')
        if np.any(probabilities < 0) or not np.isclose(probabilities.sum(), 1):
            raise ValueError('probabilities must be nonnegative and sum to one')
        if any(c.dimension != components[0].dimension for c in components):
            raise ValueError('components must share their dimension')
        self._components = components
        self._cumulative = np.cumsum(probabilities / probabilities.sum())
        self._cumulative[-1] = 1

    def sample(self, baseline, standard_normal, component_uniforms):
        """Use externally supplied Gaussian noise and uniforms in [0, 1)."""
        noise = np.asarray(standard_normal, dtype=float)
        uniforms = np.asarray(component_uniforms, dtype=float)
        if noise.ndim != 2 or uniforms.shape != (len(noise),):
            raise ValueError('supply one uniform per noise row')
        if not np.isfinite(uniforms).all() or np.any((uniforms < 0) | (uniforms >= 1)):
            raise ValueError('component uniforms must be finite and in [0, 1)')
        selected = np.searchsorted(self._cumulative, uniforms, side='right')
        result = np.empty_like(noise, dtype=float)
        for index, component in enumerate(self._components):
            mask = selected == index
            result[mask] = component.sample(baseline, noise[mask])
        return result
