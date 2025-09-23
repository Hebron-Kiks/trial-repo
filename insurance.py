# %%


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load dataset
df=pd.read_csv("insurance.csv")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean dataset (drop rows with missing values, if any)
df = df.dropna()

# -----------------------------
# Task 2: Basic Data Analysis
# -----------------------------

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Group by region and compute mean charges
avg_charges_by_region = df.groupby("region")["charges"].mean()
print("\nAverage Charges by Region:")
print(avg_charges_by_region)

# Group by smoker status and compute mean charges
avg_charges_by_smoker = df.groupby("smoker")["charges"].mean()
print("\nAverage Charges by Smoker Status:")
print(avg_charges_by_smoker)

# Observations
print("\nObservations:")
print("- Smokers generally have much higher charges than non-smokers.")
print("- BMI and age seem to influence charges.")
print("- Average charges vary slightly across regions.")

# -----------------------------
# Task 3: Data Visualization
# -----------------------------
sns.set(style="whitegrid")

# 1. Line chart: Charges trend across records
plt.figure(figsize=(8,5))
plt.plot(df.index, df["charges"], label="Charges")
plt.title("Charges Trend Across Records")
plt.xlabel("Record Index")
plt.ylabel("Charges")
plt.legend()
plt.show()

# 2. Bar chart: Average charges by smoker status
plt.figure(figsize=(6,4))
sns.barplot(x="smoker", y="charges", data=df, estimator="mean")
plt.title("Average Charges by Smoker Status")
plt.xlabel("Smoker")
plt.ylabel("Average Charges")
plt.show()

# 3. Histogram: Distribution of BMI
plt.figure(figsize=(6,4))
sns.histplot(df["bmi"], bins=20, kde=True)
plt.title("Distribution of BMI")
plt.xlabel("BMI")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot: BMI vs Charges (colored by smoker)
plt.figure(figsize=(6,4))
sns.scatterplot(x="bmi", y="charges", hue="smoker", data=df)
plt.title("BMI vs Charges")
plt.xlabel("BMI")
plt.ylabel("Charges")
plt.show()