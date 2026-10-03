# Marine data example and sources

`gdp_sample.json` illustrates the JSON format of the NOAA Global Drifter
Program's six-hourly, quality-controlled interpolated trajectory product.
Original column names, unit entries and row values are preserved.

Use [`fields.md`](fields.md) for general field meanings and
[`SOURCE.md`](SOURCE.md) for the example's provenance. The provider's original
data terms are retained in [`DATA_TERMS.txt`](DATA_TERMS.txt).

## Public source directory

| Source | Public entry point | Data type |
| --- | --- | --- |
| NOAA Global Drifter Program | https://www.aoml.noaa.gov/phod/gdp/ | Drifting-buoy observations and processed trajectory products |
| NOAA GDP ERDDAP | https://erddap.aoml.noaa.gov/gdp/erddap/ | Public discovery and access service for GDP products |
| HYCOM | https://www.hycom.org/dataserver | Gridded ocean model products |

These entry points support discovery of the relevant public products. Consult
each product's metadata for its processing history, units, version and terms of
use. Observation timestamps and data-availability timestamps have distinct
meanings; missing availability information should remain unknown.

本目录用于说明公开海洋数据的字段格式和来源。样例来自 NOAA 的质量控制插值产品；具体字段、单位和使用条款请结合所附来源文档阅读。
