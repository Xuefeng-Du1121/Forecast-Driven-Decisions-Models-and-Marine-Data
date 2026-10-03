# Marine Data Format Examples and Residual Models

This repository demonstrates marine data formats and residual modeling interfaces supporting forecast-driven decision research in ocean science applications.

## Purpose

This is a **minimal demonstration repository** providing:

1. **Marine data format examples** — NOAA Global Drifter Program trajectory data structure
2. **Residual modeling interfaces** — Conceptual code for forecast uncertainty quantification
3. **Public data source directory** — Access points for operational ocean data products

This repository supports the methodology described in:

> Du, X., et al. (2026). "Evaluating Action-Selection Reliability in Forecast-Driven Decision Systems: A Maritime Search Planning Benchmark." *Environmental Modelling & Software*. (manuscript under review)

## Repository Contents

### Data Format Documentation

- **[gdp_sample.json](gdp_sample.json)** — Sample of NOAA GDP six-hourly quality-controlled interpolated trajectory data (12 observations from buoy 122702, January 2019). Original column names, units, and values are preserved from the provider's format.

- **[fields.md](fields.md)** — Conceptual field definitions for marine trajectory data (trajectory ID, observation time, availability time, position, velocity, depth, quality flags). Note: this is a reference document, not a study-specific schema.

- **[SOURCE.md](SOURCE.md)** — Data provenance for the GDP example: NOAA source, DOI (10.25921/7ntx-z961), access URL, and Creative Commons Attribution 4.0 license.

- **[DATA_TERMS.txt](DATA_TERMS.txt)** — Original data terms from NOAA Global Drifter Program.

### Residual Modeling Code

- **[residual_models.py](residual_models.py)** — Python classes for residual distribution modeling:
  - `GaussianResidualModel` — Adds Gaussian-distributed forecast uncertainty
  - `MixtureResidualModel` — Gaussian mixture model for multimodal residuals
  
  These classes define **interfaces only** — they accept statistical parameters at initialization but do not contain fitted values or training data. Users supply all parameters (mean vectors, covariance matrices, mixing weights).

## Public Data Source Directory

| Source | Public Entry Point | Data Type |
|--------|-------------------|-----------|
| NOAA Global Drifter Program | https://www.aoml.noaa.gov/phod/gdp/ | Drifting-buoy observations and processed trajectory products |
| NOAA GDP ERDDAP | https://erddap.aoml.noaa.gov/gdp/erddap/ | Public discovery and access service for GDP products |
| HYCOM | https://www.hycom.org/dataserver | Gridded ocean model products |

**Important notes:**
- Consult each product's metadata for processing history, units, version, and terms of use
- Observation timestamps and data-availability timestamps have distinct meanings
- Missing availability information should remain unknown (not imputed as observation time)

## Usage Example

```python
import numpy as np
from residual_models import GaussianResidualModel

# Define residual statistics
mean = np.array([0.0, 0.0])  # eastward, northward velocity residual means
cov = np.array([[0.01, 0.002], [0.002, 0.01]])  # covariance matrix

# Create model
model = GaussianResidualModel(mean, cov)

# Sample residuals (using external random state for reproducibility)
rng = np.random.default_rng(seed=42)
z = rng.standard_normal(2)  # standard normal draws
residual = model.sample(z)  # correlated residuals
```

## Citation

If you use this data format documentation or modeling code, please cite:

1. **For NOAA GDP data:**
   > Elipot, S., Lumpkin, R., Perez, R. C., Lilly, J. M., Early, J. J., & Sykulski, A. M. (2016). A global surface drifter data set at hourly resolution. *Journal of Geophysical Research: Oceans*, 121(5), 2937-2966. https://doi.org/10.25921/7ntx-z961

2. **For this repository and associated methodology:**
   > Du, X., et al. (2026). "Evaluating Action-Selection Reliability in Forecast-Driven Decision Systems: A Maritime Search Planning Benchmark." *Environmental Modelling & Software*. (under review)
   >
   > Repository: https://github.com/Xuefeng-Du1121/Forecast-Driven-Decisions-Models-and-Marine-Data

## Scope and Limitations

This repository demonstrates:
- ✅ Public marine data formats (structure, fields, units)
- ✅ Conceptual residual modeling interfaces (class design, input validation)
- ✅ Data source discovery (links to operational data providers)

This repository does **not** include:
- ❌ Complete experimental code from the manuscript
- ❌ Fitted model parameters or trained weights
- ❌ Full drifter trajectory datasets (use NOAA GDP ERDDAP for complete data)
- ❌ Action library generators or decision protocol implementations

**For full experimental code supporting the manuscript**, contact the authors upon reasonable request after publication acceptance.

## License

- **Code** ([residual_models.py](residual_models.py), [__init__.py](__init__.py)): MIT License (see [LICENSE](LICENSE))
- **Data sample** ([gdp_sample.json](gdp_sample.json)): Creative Commons Attribution 4.0 (see [DATA_TERMS.txt](DATA_TERMS.txt))
- **Documentation** ([README.md](README.md), [fields.md](fields.md), [SOURCE.md](SOURCE.md)): CC0 1.0 Universal (public domain)

## Attribution

This example uses data collected and made freely available by the [NOAA Global Drifter Program](https://www.aoml.noaa.gov/phod/gdp/), accessed via their public ERDDAP service.

---

本目录用于说明公开海洋数据的字段格式和来源，以及残差建模的概念性接口设计。样例数据来自 NOAA 全球漂流浮标计划的质量控制插值产品；具体字段、单位和使用条款请结合所附来源文档阅读。完整的实验代码和模型参数未包含在此开源仓库中。
