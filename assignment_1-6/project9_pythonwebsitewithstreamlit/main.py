import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    column = df.columns.tolist()
    selected_column = st.selectbox("Select a column to filter", column)
    unique_values = df[selected_column].unique()
    selected_values = st.selectbox("Select values to filter", unique_values, index=0, format_func=lambda x: str(x))
    filtered_df = df[df[selected_column] == selected_values]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", column)
    y_column = st.selectbox("Select y-axis column", column)
    
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

    else:
        st.write("Waiting on file upload....")    




