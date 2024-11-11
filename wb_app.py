import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Data Analysis App")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error reading the CSV file: {e}")
        st.stop()

    st.subheader("Raw Data")
    st.dataframe(df)

    st.subheader("Data Summary")
    st.write(df.describe())
    
    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    numeric_columns = df.select_dtypes(include=np.number).columns.tolist()
    if not numeric_columns:
        st.warning("No numeric columns available for visualization.")
    else:
        column = st.selectbox("Choose a numeric column to display", numeric_columns)

        st.subheader("Column Visualization")
        chart_type = st.selectbox("Select chart type", ["Line Chart", "Bar Chart", "Area Chart", "Histogram"])

        if chart_type == "Line Chart":
            st.line_chart(df[column])
        elif chart_type == "Bar Chart":
            st.bar_chart(df[column])
        elif chart_type == "Area Chart":
            st.area_chart(df[column])
        elif chart_type == "Histogram":
            fig, ax = plt.subplots()
            ax.hist(df[column].dropna(), bins=20)
            st.pyplot(fig)

        st.subheader("Filter Data")
        min_val, max_val = st.slider(
            "Select range",
            float(df[column].min()),
            float(df[column].max()),
            (float(df[column].min()), float(df[column].max()))
        )

        filtered_df = df[(df[column] >= min_val) & (df[column] <= max_val)]

        st.write("Filtered Data")
        st.dataframe(filtered_df)

        show_raw_data = st.checkbox("Show Raw Data")
        if show_raw_data:
            st.subheader("Raw Data")
            st.dataframe(df)

        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Filtered Data",
            data=csv,
            file_name="filtered_data.csv",
            mime="text/csv"
        )

        st.subheader("Multiple Column Visualization")
        selected_columns = st.multiselect("Choose columns to display", numeric_columns)

        if selected_columns:
            st.line_chart(df[selected_columns])

    st.sidebar.header("Options")

    if numeric_columns:
        sidebar_chart_type = st.sidebar.radio("Chart type for filtered data", ["Line Chart", "Bar Chart", "Area Chart", "Histogram"])

        st.sidebar.subheader("Filtered Data Visualization")
        if sidebar_chart_type == "Line Chart":
            st.sidebar.line_chart(filtered_df[column])
        elif sidebar_chart_type == "Bar Chart":
            st.sidebar.bar_chart(filtered_df[column])
        elif sidebar_chart_type == "Area Chart":
            st.sidebar.area_chart(filtered_df[column])
        elif sidebar_chart_type == "Histogram":
            fig, ax = plt.subplots()
            ax.hist(filtered_df[column].dropna(), bins=20)
            st.sidebar.pyplot(fig)

    st.sidebar.header("Additional Features")

    if st.sidebar.checkbox("Show Correlation Heatmap") and len(numeric_columns) > 1:
        st.subheader("Correlation Heatmap")
        correlation = df[numeric_columns].corr()
        fig, ax = plt.subplots()
        sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

    if st.sidebar.checkbox("Download Entire Data"):
        csv_all = df.to_csv(index=False).encode('utf-8')
        st.sidebar.download_button(
            label="Download All Data",
            data=csv_all,
            file_name="all_data.csv",
            mime="text/csv"
        )

    if st.sidebar.checkbox("Show Data Types"):
        st.subheader("Data Types")
        st.write(df.dtypes)

else:
    st.info("Awaiting for CSV file to be uploaded.")
