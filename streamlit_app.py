# Import required libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the title and the sidebar options
st.set_page_config(page_title="Data Manipulation and Visualization", layout="wide")

# Add a title to the app
st.title("Data Manipulation and Visualization")

# Upload a file
uploaded_file = st.file_uploader("Choose a file")

# Load the dataset
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Display the dataset
    st.write(df.head())

    # Filter the data by column
    column = st.selectbox("Select a column", df.columns)
    value = st.text_input("Enter a value")
    filtered_data = df[df[column] == value]
    st.write(filtered_data)

    # Show a histogram of the data
    st.subheader("Histogram")
    col1, col2 = st.columns(2)
    with col1:
        bins = st.slider("Number of bins", min_value=1, max_value=50, value=10)
    with col2:
        x_axis = st.selectbox("Select an x-axis", df.columns)
    fig, ax = plt.subplots()
    ax.hist(df[x_axis], bins=bins)
    st.pyplot(fig)

    # Show a chart of the data
    st.subheader("Chart")
    chart_type = st.selectbox("Select a chart type", ["line", "bar", "scatter"])
    if chart_type == "line":
        x_axis_key = "selectbox_x_axis"
        y_axis_key = "selectbox_y_axis"
        x_axis = st.selectbox("Select an x-axis", df.columns, key=x_axis_key)
        y_axis = st.selectbox("Select a y-axis", df.columns, key=y_axis_key)

        fig, ax = plt.subplots()
        ax.plot(df[x_axis], df[y_axis])
        st.pyplot(fig)
    elif chart_type == "bar":
        x_axis_key = "selectbox_x_axis"
        y_axis_key = "selectbox_y_axis"
        x_axis = st.selectbox("Select an x-axis", df.columns, key=x_axis_key)
        y_axis = st.selectbox("Select a y-axis", df.columns, key=y_axis_key)

        fig, ax = plt.subplots()
        ax.bar(df[x_axis], df[y_axis])
        st.pyplot(fig)
    elif chart_type == "scatter":
        x_axis_key = "selectbox_x_axis"
        y_axis_key = "selectbox_y_axis"
        x_axis = st.selectbox("Select an x-axis", df.columns, key=x_axis_key)
        y_axis = st.selectbox("Select a y-axis", df.columns, key=y_axis_key)

        fig, ax = plt.subplots()
        ax.scatter(df[x_axis], df[y_axis])
        st.pyplot(fig)
