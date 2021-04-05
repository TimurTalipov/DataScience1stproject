import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components
import pandas as pd
import plotly.graph_objects as go
from celluloid import Camera
from pandas import read_csv
# Based on this recipe:
# https://discuss.streamlit.io/t/matplotlib-animation-in-streamlit-through-html-js/5587
with st.echo(code_location='below'):
    st.title("Hello, World!")
    """
    This is a test.
    """
    GlobalTemp = pd.read_csv("https://github.com/TimurTalipov/DataScience1stproject/blob/main/GlobalTemperatures.csv")
    GlobalTempCountry = pd.read_csv("https://github.com/TimurTalipov/DataScience1stproject/blob/main/GlobalLandTemperaturesByCountry.csv")
    GlobalTempState = pd.read_csv("https://github.com/TimurTalipov/DataScience1stproject/blob/main/GlobalLandTemperaturesByState.csv")


    GlobalTemp.head(5)

    GlobalTemp.rename(columns={'dt': 'Date'}, inplace=True)
    Year_Temp = GlobalTemp.groupby(GlobalTemp['Date'].dt.year)['LandAverageTemperature', 'LandMaxTemperature',
                                                               'LandMinTemperature', 'LandAndOceanAverageTemperature'].mean().reset_index()
    Year_Temp.rename(columns={'Date': 'Year'}, inplace=True)

    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Scatter(x=Year_Temp.Year, y=Year_Temp.LandAverageTemperature,
                             mode='lines',
                             name='LandAvgTemp',
                             marker_color='#A9A9A9'))
    fig.add_trace(go.Scatter(x=Year_Temp.Year, y=Year_Temp.LandMaxTemperature,
                             mode='lines',
                             name='LandMaxAvgTemp',
                             marker_color='#BDB76B'))
    fig.add_trace(go.Scatter(x=Year_Temp.Year, y=Year_Temp.LandMinTemperature,
                             mode='lines',
                             name='LandMinAvgTemp',
                             marker_color='#45CE30'))

    fig.add_trace(go.Scatter(x=Year_Temp.Year, y=Year_Temp.LandAndOceanAverageTemperature,
                             mode='lines',
                             name='Land&OceanAvgTemp',
                             marker_color='#FFA07A'))
    fig.update_layout(
        height=800,
        xaxis_title="Years",
        yaxis_title='Temperatures in degree',
        title_text='Average Land, Ocean, Minimun, and Maximum Temperatures over the years'
    )
    fig.add_annotation(
        x=1950,
        y=2.7,
        text="1950")
    fig.add_annotation(
        x=1972,
        y=8.4,
        text="1972")
    fig.add_annotation(
        x=1978,
        y=14.28,
        text="1978")
    fig.add_annotation(
        x=1969,
        y=15.31,
        text="1969")
    fig.update_annotations(dict(
        xref="x",
        yref="y",
        showarrow=True,
        arrowhead=7,
        ax=0,
        ay=-40
    ))

    fig.update_layout(showlegend=True)

    fig.show()
