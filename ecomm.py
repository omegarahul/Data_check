import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns


def main():
    st.title("This is a app for ecomm I am creating")
    st.sidebar.title("You can upload your file here")

    upload_file = st.sidebar.file_uploader("upload your file", type=['csv','xlsx'])

    if upload_file is not None:
        try:
            if upload_file.name.endswith('.csv'):
                data = pd.read_csv(upload_file)
            elif upload_file.name.endswith('.xlsx')
                data = pd.read_excel(upload_file)

            st.sidebar.success("File uploaded successfully")

            st.subheader("I am going to show you a data details")
            st.dataframe(data.head())

            st.subheader("Let's see some more details in data")
            st.write("Shape of the data", data.shape)
            st.write("The column inside the data is", data.columns)
            st.write("missing value into column", data.isnull().sum())

            st.subheader("I will show you the bit of stats")

            st.write(data.describe())
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()

    
