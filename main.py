import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title of the app
st.title("Automatic CSV Data Analysis App")

# File uploader for CSV files
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Display the first few rows of the dataframe
    st.subheader("Data Preview")
    st.write(df.head())

    # Display basic statistics
    st.subheader("Basic Statistics")
    st.write(df.describe())

    # Display data types
    st.subheader("Data Types")
    st.write(df.dtypes)

    # Display missing values
    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    # Automatic analysis
    st.subheader("Automatic Data Visualization")

    # Loop through each column and generate appropriate visualizations
    for column in df.columns:
        column_type = df[column].dtype

        if pd.api.types.is_numeric_dtype(column_type):
            # Histogram and Box Plot for numeric columns
            st.write(f"### Histogram and Box Plot of {column}")

            # Determine figure size based on unique values
            num_unique_values = df[column].nunique()
            fig, axes = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

            # Histogram
            sns.histplot(df[column], bins=min(30, num_unique_values), kde=True, ax=axes[0], color='skyblue')
            axes[0].set_title(f"Histogram of {column}")
            axes[0].set_ylabel("Frequency")
            axes[0].tick_params(axis='x', rotation=45)

            # Box Plot
            sns.boxplot(x=df[column], ax=axes[1], color='lightgreen')
            axes[1].set_title(f"Box Plot of {column}")
            axes[1].set_xlabel(column)

            plt.tight_layout()  # Adjust layout to prevent overlap
            st.pyplot(fig)

        elif pd.api.types.is_categorical_dtype(column_type) or pd.api.types.is_object_dtype(column_type):
            # Bar chart for categorical columns
            st.write(f"### Bar Chart of {column}")

            # Limit to top N categories
            top_n = 10
            top_categories = df[column].value_counts().nlargest(top_n)
            plt.figure(figsize=(12, 6))
            sns.barplot(x=top_categories.index, y=top_categories.values, palette='viridis')
            plt.title(f"Top {top_n} Categories in {column}")
            plt.xlabel(column)
            plt.ylabel("Count")
            plt.xticks(rotation=45)  # Rotate x-axis labels
            plt.tight_layout()  # Adjust layout to prevent overlap
            st.pyplot(plt)

    # Plot correlation heatmap for numeric columns
    if st.button("Show Correlation Heatmap"):
        numeric_df = df.select_dtypes(include=['number'])
        
        if numeric_df.empty:
            st.write("No numeric columns available for correlation.")
        else:
            plt.figure(figsize=(12, 10))  # Increase figure size
            sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap='coolwarm', square=True)
            plt.title("Correlation Heatmap")
            plt.tight_layout()  # Adjust layout to prevent overlap
            st.pyplot(plt)

# Run the app with: streamlit run data_analysis_app.py