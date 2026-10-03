# Forecast-Driven Decisions: Models and Marine Data

Forecast-driven marine decisions connect uncertain environmental states with
choices about actions. Clear model interfaces and traceable data sources help
make this connection inspectable.

This repository provides illustrative residual-distribution models and a marine
data example relevant to that setting. The current public snapshot focuses on
the model interface, data representation and source documentation.

## Repository contents

| Directory | Contents |
| --- | --- |
| [`models/`](models/) | Illustrative Gaussian and Gaussian-mixture residual models implemented with NumPy |
| [`datasets/`](datasets/) | A NOAA Global Drifter Program data excerpt, field descriptions and source documentation |

The model interface separates distribution state from sampling noise, allowing
both to be supplied explicitly by the caller. The data example preserves the
provider's field names, unit entries and values so that its structure can be
inspected alongside the source documentation.

## Research materials and availability

The examples illustrate distribution families and data formats relevant to the
study. The complete experimental implementation and reproduction materials are
maintained separately for editorial and peer-review assessment. Their public
release is planned following acceptance, together with the corresponding
configuration and reproducibility documentation.

## Data provenance

The included excerpt comes from the NOAA Global Drifter Program's six-hourly,
quality-controlled interpolated product. Product references, attribution and
data terms are provided in [`datasets/SOURCE.md`](datasets/SOURCE.md) and
[`datasets/DATA_TERMS.txt`](datasets/DATA_TERMS.txt).

## 中文说明

本项目围绕预报驱动的海洋决策，提供残差分布模型的接口示例，以及具有明确来源的海洋数据样例。当前公开内容便于了解模型接口、数据字段和来源信息。

完整实验实现与复现材料单独保留，供编辑和审稿核查；计划在论文录用后，连同对应配置和复现文档统一公开。
