import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
df = pd.read_csv(Path(__file__).with_name("experiment_9_retail_sales.csv"))
df["Date"] = pd.to_datetime(df["Date"])
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]
print("----- RETAIL SALES DATASET -----")
print(df.head())
print("\nTotal Units Sold:", df["Units_Sold"].sum())
print("Total Revenue: Rs.",
    df["Revenue"].sum())
monthly_sales = df.groupby(
  df["Date"].dt.to_period("M"))["Revenue"].sum()
print("\n----- MONTHLY REVENUE -----")
print(monthly_sales)
category_sales = df.groupby(
  "Category")["Revenue"].sum()
print("\n----- CATEGORY-WISE REVENUE -----")
print(category_sales)
region_sales = df.groupby(
  "Region")["Revenue"].sum()
print("\n----- REGION-WISE REVENUE -----")
print(region_sales)
plt.figure(figsize=(9, 5))
monthly_sales.index = monthly_sales.index.astype(str)
plt.plot(
  monthly_sales.index,
  monthly_sales.values,
  marker="o",
  linewidth=2,
  label="Monthly Revenue")
plt.title("Monthly Retail Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 5))
category_sales.plot(
  kind="bar",
  color="lightgreen",
  edgecolor="black")
plt.title("Category-wise Revenue Comparison")
plt.xlabel("Product Category")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
plt.figure(figsize=(7, 7))
plt.pie(
  region_sales,
  labels=region_sales.index,
  autopct="%1.1f%%",
  startangle=90)
plt.title("Region-wise Revenue Distribution")
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 5))
plt.scatter(
  df["Units_Sold"],
  df["Revenue"],
  color="red",
  marker="o")
plt.title("Units Sold vs Revenue")
plt.xlabel("Units Sold")
plt.ylabel("Revenue (Rs.)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
print("\nData Visualization Completed Successfully!")
