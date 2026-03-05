# household_finance_analysis

一个用于**家庭金融数据分析**的标准 Python 项目模板。

## 项目结构

```text
household_finance_analysis/
│
├── data/                # 存放原始数据、清洗后数据、临时中间数据
├── analysis/            # 存放分析脚本或 Jupyter Notebook
├── figures/             # 存放可视化图表输出（PNG、SVG、PDF 等）
├── README.md            # 项目说明文档
└── requirements.txt     # Python 依赖列表
```

## 文件夹说明

- `data/`
  - 用于管理家庭收支、资产负债、预算等数据文件。
  - 建议按层级区分：`raw/`（原始数据）、`processed/`（清洗后数据）。

- `analysis/`
  - 用于保存分析过程相关内容。
  - 可放置 `.ipynb`（交互式分析）和 `.py`（可复用脚本）。

- `figures/`
  - 用于集中存放分析结果图表。
  - 便于在报告、汇报或 README 中直接引用。

## 快速开始

1. 创建并激活虚拟环境（可选但推荐）
2. 安装依赖：

```bash
pip install -r requirements.txt
```

3. 在 `analysis/` 中开始你的家庭金融分析。

## 后续建议

- 增加 `data/raw` 与 `data/processed` 子目录。
- 添加 `analysis/eda.ipynb` 进行探索性分析。
- 使用版本控制追踪脚本，不建议提交敏感原始账单数据。
