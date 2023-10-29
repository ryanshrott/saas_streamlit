# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Title of our app
st.title("Data Display with Streamlit")

# Creating a sample DataFrame
data = {
    "A": np.random.randn(50),
    "B": np.random.randn(50),
    "C": np.random.randn(50)
}
df = pd.DataFrame(data)

# Displaying a table with Streamlit
st.header("Displaying Tables in Streamlit")
st.table(df.head(25))

# Displaying a DataFrame with Streamlit (more interactive than table)
st.header("Displaying DataFrames in Streamlit")
st.write(df.head(25))

# Using line_chart to visualize the data
st.header("Using Built-in Line Chart")
st.bar_chart(df)


# Using Matplotlib and Seaborn for custom visualizations
st.header("Custom Visualizations with Matplotlib and Seaborn")

# Creating a correlation heatmap using seaborn
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
st.pyplot(plt)

# Displaying dynamic content
st.header("Dynamic Content: Markdown, Images, and Videos")
st.markdown("This is **Markdown** in action in Streamlit!")
st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit Logo", use_column_width=True)
st.video("https://www.youtube.com/watch?v=yJEUOZC8FKY&ab_channel=carwow")
