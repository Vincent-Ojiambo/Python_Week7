# TASK 1: LOAD AND EXPLORE THE DATASET

# Make sure to install required packages before running:
# pip install pandas matplotlib

import sys  # Import for exiting the script
import pandas as pd  # Import libraries
import matplotlib.pyplot as plt  # Import for plotting

try:
    df = pd.read_csv("iris.csv")   # Load dataset with error handling
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("File not found. Please check the path or filename.")
    sys.exit(1)  # Exit if file not found

print(df.head()) # Display first few rows
print(df.info()) # Info about dataset
print(df.isnull().sum()) # Check missing values

# Clean Dataset
df = df.dropna() # Drop missing values (if any)


# TASK 2: BASIC DATA ANALYSIS
print(df.describe()) # Compute descriptive statistics
grouped = df.groupby("species").mean() # Group by species and compute mean
print(grouped) # Display grouped means
print(df.groupby("species")["petal_length"].mean()) # Example: Average petal length per species


# TASK 3: VISUALIZATION
# 1. Line Chart
plt.plot(df.index, df["sepal_length"], label="Sepal Length", color="blue")
plt.title("Line Chart of Sepal Length")
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.legend()
plt.show()

# 2. Bar Chart
df.groupby("species")["petal_length"].mean().plot(kind="bar", color="skyblue")
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length")
plt.show()

# 3. Histogram
plt.hist(df["sepal_length"], bins=20, color="orange", alpha=0.7) # Corrected to histogram
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot
plt.scatter(df["sepal_length"], df["petal_length"], c="green", alpha=0.6)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()





