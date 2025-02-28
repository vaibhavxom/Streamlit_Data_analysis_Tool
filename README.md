# Automatic CSV Data Analysis App

This is a Streamlit application that allows users to perform automatic data analysis on CSV files. The app provides a user-friendly interface to visualize and analyze data, making it easier to understand datasets quickly.

## Features

- **CSV File Upload**: Users can upload CSV files for analysis.
- **Data Preview**: Displays the first few rows of the uploaded dataset.
- **Basic Statistics**: Provides summary statistics for numeric columns.
- **Data Types**: Shows the data types of each column in the dataset.
- **Missing Values**: Displays the count of missing values for each column.
- **Automatic Data Visualization**:
  - Histograms and Box Plots for numeric columns.
  - Bar Charts for categorical columns.
- **Correlation Heatmap**: Visualizes the correlation between numeric columns.
- **Interactive Visualizations**: Users can interact with the visualizations for better insights.

## Installation Steps

To run this app locally, follow these steps:

1. **Clone the Repository**:
```bash
   git clone https://github.com/vaibhavxom/Streamlit_Data_analysis_Tool.git
   cd Streamlit_Data_analysis_Tool
```
Set Up a Virtual Environment (Optional but Recommended):

```bash

python -m venv venv
```
```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
Install Required Packages: You can install the required packages using the requirements.txt file provided in the repository. Run:

```bash
pip install -r requirements.txt
```
Alternatively, you can install the packages individually:

```bash
pip install streamlit pandas matplotlib seaborn plotly
```
Run the App: Execute the following command in your terminal:

```bash
streamlit run main.py
```
Open in Browser: After running the command, a new tab will open in your default web browser displaying the app. If it doesn't open 

automatically, you can access it at `http://localhost:8501`.

**Usage**
Upload a CSV file using the file uploader.

- Explore the data preview, basic statistics, and data types.
- Visualize the data using the automatic visualizations provided.
- Click the button to view the correlation heatmap for numeric columns.
**Requirements**
The following packages are required to run this application. You can find them in the requirements.txt file:

```plaintext

matplotlib==3.10.1
pandas==2.2.3
plotly==6.0.0
seaborn==0.13.2
streamlit==1.42.2
```
**Contributing**
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

**Acknowledgments**
- Streamlit - The framework used to build this app.
- Pandas - For data manipulation and analysis.
- Matplotlib and Seaborn - For data visualization.