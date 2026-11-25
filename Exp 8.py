import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
df = pd.read_csv(Path(__file__).with_name("experiment_8_student_performance.csv"))
print("----- ORIGINAL DATASET -----")
print(df.head())
print("\nDataset Shape:", df.shape)
print("\n----- MISSING VALUES -----")
print(df.isnull().sum())
print("\nDuplicate Records:", df.duplicated().sum())
num_cols = df.select_dtypes(include=np.number).columns
for col in num_cols:
  df[col] = df[col].fillna(df[col].median())
cat_cols = df.select_dtypes(include="object").columns
for col in cat_cols:
  df[col] = df[col].fillna(df[col].mode()[0])
df.drop_duplicates(inplace=True)
df["Average_Score"] = df[
  ["Assignment_Score", "Exam_Score"]
].mean(axis=1)
df["Performance"] = pd.cut(
  df["Average_Score"],
  bins=[-1, 50, 70, 85, 100],
  labels=[
     "Needs Improvement",
     "Average",
     "Good",
     "Excellent"
  ]
)
print("\n----- CLEANED DATASET -----")
print(df.head(10))
print("\nCleaned Dataset Shape:", df.shape)
print("\n----- STATISTICAL SUMMARY -----")
print(df.describe().round(2))
dept_analysis = df.groupby(
  "Department"
)["Exam_Score"].mean()
print("\n----- DEPARTMENT-WISE AVERAGE -----")
print(dept_analysis.round(2))
print("\n----- PERFORMANCE DISTRIBUTION -----")
print(df["Performance"].value_counts())
plt.figure(figsize=(8, 5))
dept_analysis.plot(
  kind="bar",
  color="skyblue",
  edgecolor="black"
)
plt.title("Department-wise Average Exam Score")
plt.xlabel("Department")
plt.ylabel("Average Exam Score")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 5))
df["Performance"].value_counts().plot(
  kind="bar",
  color="orange",
  edgecolor="black"
)
plt.title("Student Performance Distribution")
plt.xlabel("Performance Category")
plt.ylabel("Number of Students")
plt.xticks(rotation=15)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
print("\nData Cleaning and EDA Completed Successfully!")
