import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("Prosthetic Performance Analysis Dashboard")

# Load data
df = pd.read_csv("prosthetic_data.csv")

# Show data
st.subheader("Dataset Preview")
st.write(df.head())

# Correlation
corr = df[['accuracy', 'comfort']].corr().iloc[0,1]
st.subheader("Correlation between Accuracy and Comfort")
st.write(f"{corr*100:.2f}%")

# Scatter Plot
st.subheader("Accuracy vs Comfort")
fig1, ax1 = plt.subplots()
sns.scatterplot(x='accuracy', y='comfort', data=df, ax=ax1)
st.pyplot(fig1)

# Regression Plot
st.subheader("Trend Line")
fig2, ax2 = plt.subplots()
sns.regplot(x='accuracy', y='comfort', data=df, ax=ax2)
st.pyplot(fig2)

# Heatmap
st.subheader("Correlation Heatmap")
fig3, ax3 = plt.subplots()
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax3)
st.pyplot(fig3)

# Final Insight
st.subheader("Final Insight")
st.write("Accuracy has only a weak impact (~10%) on user comfort.")