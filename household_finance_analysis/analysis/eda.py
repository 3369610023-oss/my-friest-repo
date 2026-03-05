from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    data_path = project_root / "data" / "household_data.csv"
    figures_dir = project_root / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    # 1) Load dataset
    df = pd.read_csv(data_path)

    # 2) Basic descriptive statistics
    print("=== Basic Descriptive Statistics ===")
    print(df.describe(include="all"))

    # 3) Create financial_ratio
    df["financial_ratio"] = df["financial_assets"] / df["total_assets"]

    # 4) Divide into 3 income groups by quantiles
    df["income_group"] = pd.qcut(
        df["income"],
        q=3,
        labels=["Low income", "Middle income", "High income"],
    )

    # 5) Average financial_ratio by income group
    avg_ratio = df.groupby("income_group", observed=False)["financial_ratio"].mean()
    print("\n=== Average Financial Ratio by Income Group ===")
    print(avg_ratio)

    # 6) Visualizations
    sns.set_theme(style="whitegrid")

    # Histogram of income
    plt.figure(figsize=(10, 6))
    sns.histplot(df["income"], bins=30, kde=True)
    plt.title("Income Distribution")
    plt.xlabel("Income")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(figures_dir / "income_histogram.png", dpi=300)
    plt.close()

    # Boxplot of financial_ratio by income group
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x="income_group", y="financial_ratio")
    plt.title("Financial Ratio by Income Group")
    plt.xlabel("Income Group")
    plt.ylabel("Financial Ratio")
    plt.tight_layout()
    plt.savefig(figures_dir / "financial_ratio_by_income_group_boxplot.png", dpi=300)
    plt.close()

    print("\nSaved figures:")
    print(f"- {figures_dir / 'income_histogram.png'}")
    print(f"- {figures_dir / 'financial_ratio_by_income_group_boxplot.png'}")


if __name__ == "__main__":
    main()
