# General marine-data fields

These are conceptual field descriptions, not a study-specific schema or an
implemented adapter. Actual names and units must be read from source metadata.

| Concept | Meaning |
| --- | --- |
| Trajectory identifier | Provider-specific identifier for a trajectory or deployment |
| Observation time | Time represented by an observation or processed estimate |
| Availability time | Time a record became available, if supplied by the provider |
| Longitude and latitude | Geographic coordinates with a declared convention and units |
| Eastward and northward velocity | Horizontal velocity components with declared units |
| Depth | Vertical coordinate with declared sign convention and units |
| Quality information | Product-specific quality flags, uncertainties or processing status |
| Missing values | Values identified by the product's missing-data metadata |

Observation time and availability time are not interchangeable. A missing
availability timestamp should remain unknown. Deployment identifiers and other
platform numbering schemes should not be merged without an explicit mapping.
