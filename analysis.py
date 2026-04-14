import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("prosthetic_data.csv")

# Show data
print(df.head())
print(df.describe())

# Correlation
print("\nCorrelation:")
print(df[['accuracy', 'comfort']].corr())
corr = df[['accuracy', 'comfort']].corr().iloc[0,1]
print(f"Correlation: {corr*100:.2f}%")

# 🔥 Scatter Plot (ADD HERE)
sns.scatterplot(x='accuracy', y='comfort', data=df)
plt.title("Accuracy vs Comfort")
plt.xlabel("Accuracy")
plt.ylabel("Comfort")
plt.show()
sns.regplot(x='accuracy', y='comfort', data=df)
plt.title("Accuracy vs Comfort with Trend Line")
plt.show()
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()