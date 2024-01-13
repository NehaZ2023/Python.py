import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the shipment dataset (replace with your actual file path)
data = pd.read_csv("shipment_data.csv")

# Explore the dataset
print(data.head())
print(data.info())

# Check for missing values
print(data.isnull().sum())

# Identify outliers
z_scores = np.abs(stats.zscore(data))
outliers = data[z_scores > 3].index
print("Outliers:", outliers)

# Analyze pricing trends
data.plot(kind="line", x="Date", y="Price", figsize=(10, 6))
plt.title("Shipment Price Trends")
plt.show()

# Analyze price distribution
sns.boxplot(data["Price"])
plt.show()

# Calculate summary statistics
summary_stats = data.describe()
print("Summary Statistics:\n", summary_stats)