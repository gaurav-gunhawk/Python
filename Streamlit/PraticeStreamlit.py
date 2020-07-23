import streamlit as st
import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt

st.title("Exploratory Data Analysis")

selectedDataSet = st.sidebar.selectbox("Select DataSet" , ("Corona virus" , "States" , "India"))
checkBoxPreviewData = st.sidebar.checkbox("Preview Data")
checkBoxVisualization = st.sidebar.checkbox("Visualization")

def DataSet(selectedDataSet):
    if selectedDataSet == "Corona virus":
        st.write("Corona virus DataSet")
        data = pd.read_csv('E:/Jupyter Notebook Data/datasets_557629_1337247_StatewiseTestingDetails.csv')

        if checkBoxPreviewData:
            st.write(data.head())

        data['Negative'] = data['TotalSamples'] - data['Positive']
        data = data.fillna(0)  # Filling the remaining values as 0

        data['Date'] = pd.to_datetime(data['Date'])
        data['State'] = data['State'].astype(str)

        india = data.groupby(data['Date'].dt.strftime('%B'))['TotalSamples'].sum().sort_values()
        india = india.reset_index()

        if checkBoxVisualization:
            plt.bar(india['Date'], india["TotalSamples"])
            plt.xlabel("Months")
            plt.ylabel("Tests")
            plt.title("Corona Testing in India")
            st.pyplot(plt)

            d = data.groupby('State').sum().reset_index()
            d = d.sort_values("TotalSamples")
            positive = d['Positive']
            negative = d['Negative']
            width = 0.45
            plt.figure(figsize=(100, 10))
            plt.bar(d['State'], negative, width, color='r')
            plt.bar(d['State'], positive, width, bottom=negative, color='b')
            plt.legend(['Negative', 'Positive'])
            plt.xlabel("States")
            plt.ylabel("Total Test Cases")
            plt.title("Number of Test Samples taken according to State-wise (where no. of Positive People -> Blue , Negative -> Red)")
            st.pyplot(plt)

    elif selectedDataSet == "States":
        st.write("Hello! Working on States Dataset")
        if checkBoxPreviewData:
            st.write("No data yet! to preview")
        if checkBoxVisualization:
            st.write("No data yet! to visualize")
    else:
        st.write("Hello! Working on India Dataset")
        if checkBoxPreviewData:
            st.write("No data yet! to preview")
        if checkBoxVisualization:
            st.write("No data yet! to visualize")

DataSet(selectedDataSet)
