import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the FIFA 19 dataset (download from a reliable source like Kaggle)
data = pd.read_csv("fifa19.csv")

# Explore the dataset
print(data.head())
print(data.info())

# Analyze how different attributes affect overall rating
sns.scatterplot(x="Overall", y="Age", data=data)
plt.show()

sns.heatmap(data.corr(), annot=True)
plt.show()

# Identify players with the highest overall rating
top_players = data.sort_values("Overall", ascending=False).head(10)
print("Top 10 Players:")
print(top_players[["Name", "Overall", "Club"]])

# Determine most important attributes for overall rating
correlations = data.corr()["Overall"]
important_attributes = correlations.sort_values(ascending=False)[1:6]
print("Most Important Attributes:")
print(important_attributes)