# Data Analysis App

![App Screenshot](/preview_1.png)
![App Screenshot](/preview_2.png)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Data](#sample-data)
- [Additional Information](#additional-information)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to the **Data Analysis App**, a user-friendly web application built with Streamlit that empowers you to perform comprehensive data analysis and visualization with ease. Whether you're a data scientist, analyst, or enthusiast, this app provides intuitive tools to explore your datasets, generate insightful visualizations, and extract meaningful information effortlessly.

## Features

- **CSV File Upload:** Easily upload your CSV files for analysis.
- **Raw Data Display:** View the entire dataset in a structured table format.
- **Data Summary:** Get statistical summaries of your data, including mean, median, standard deviation, and more.
- **Missing Values Detection:** Identify missing values across different columns.
- **Dynamic Visualization:**
  - Select numeric columns to visualize.
  - Choose from various chart types: Line Chart, Bar Chart, Area Chart, Histogram.
  - Visualize multiple columns simultaneously.
- **Data Filtering:**
  - Use sliders to filter data based on numeric column ranges.
  - View filtered datasets instantly.
- **Download Options:**
  - Download filtered data as a CSV file.
  - Download the entire dataset.
- **Advanced Features:**
  - Correlation Heatmap to understand relationships between numeric variables.
  - View data types of each column for better data understanding.

## Demo

![App Demo](/preview_3.png)

## Installation

Follow these steps to set up and run the Data Analysis App on your local machine.

### Prerequisites

- **Python 3.7 or higher**: Ensure you have Python installed. You can download it from [Python's official website](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/yourusername/data-analysis-app.git
cd data-analysis-app
```

### Create a Virtual Environment (Optional but Recommended)

Creating a virtual environment helps manage dependencies and avoid conflicts.

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

### Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install streamlit pandas numpy seaborn matplotlib
```

## Usage

Once the installation is complete, you can run the app using the following command:

```bash
streamlit run app.py
```

This command will launch the Streamlit app, and you can access it in your web browser at `http://localhost:8501`.

### Step-by-Step Guide

1. **Upload a CSV File:**
   - Click on the "Browse files" button.
   - Select your CSV file from your local machine.

2. **View Raw Data:**
   - After uploading, the raw data will be displayed in a table format.

3. **Data Summary:**
   - View statistical summaries such as mean, median, standard deviation, etc.

4. **Missing Values:**
   - Identify the count of missing values in each column.

5. **Select a Numeric Column:**
   - Use the dropdown to select a numeric column for visualization.

6. **Choose Chart Type:**
   - Select your preferred chart type (Line, Bar, Area, Histogram).

7. **Visualize Data:**
   - The selected chart will be displayed based on your choices.

8. **Filter Data:**
   - Use the slider to set a range for the selected numeric column.
   - The dataset will be filtered accordingly and displayed.

9. **Download Filtered Data:**
   - Click the "Download Filtered Data" button to download the filtered dataset as a CSV file.

10. **Multiple Column Visualization:**
    - Select multiple columns to visualize them simultaneously using line charts.

11. **Sidebar Options:**
    - **Chart Type for Filtered Data:** Choose different chart types for the filtered data.
    - **Additional Features:**
      - **Show Correlation Heatmap:** Visualize the correlation between numeric columns.
      - **Download Entire Data:** Download the entire dataset as a CSV file.
      - **Show Data Types:** View the data types of each column.

## Sample Data

To help you get started, a sample CSV file is provided. This dataset includes various columns such as dates, sales figures, expenses, profit, and regions to demonstrate the app's capabilities.

### Sample CSV Data

```csv
Date,Sales,Expenses,Profit,Region
2023-01-01,1000,800,200,North
2023-01-02,1500,900,600,South
2023-01-03,2000,1000,1000,East
2023-01-04,1300,850,450,West
2023-01-05,1700,950,750,North
2023-01-06,1600,920,680,South
2023-01-07,1800,980,820,East
2023-01-08,1900,1050,850,West
2023-01-09,2100,1100,1000,North
2023-01-10,2200,1150,1050,South
2023-01-11,2300,1200,1100,East
2023-01-12,2400,1250,1150,West
2023-01-13,2500,1300,1200,North
2023-01-14,2600,1350,1250,South
2023-01-15,2700,1400,1300,East
```

### How to Use the Sample Data

1. **Download the Sample Data:**
   - Save the above CSV content into a file named `sample_data.csv`.

2. **Upload to the App:**
   - Use the "Choose a CSV file" uploader in the app to select and upload `sample_data.csv`.

3. **Explore the Features:**
   - Follow the usage guide to explore different features and visualizations using the sample data.

## Additional Information

### Customizing the App

Feel free to customize the app to better suit your specific needs. You can add more visualization types, incorporate additional data preprocessing steps, or enhance the user interface for a better user experience.

### Error Handling

The app includes basic error handling for file uploads. If an invalid CSV file is uploaded, an error message will be displayed, and the app will halt further execution until a valid file is provided.

### Extending Functionality

Consider adding the following features to enhance the app further:

- **Interactive Filtering:** Allow users to apply multiple filters on different columns simultaneously.
- **Export Visualizations:** Enable users to download the generated charts and plots.
- **Data Transformation:** Provide options for data cleaning, such as handling missing values, encoding categorical variables, etc.
- **Advanced Analytics:** Incorporate machine learning models for predictive analysis directly within the app.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software as per the terms of the license.
