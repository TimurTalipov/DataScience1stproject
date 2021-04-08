import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from celluloid import Camera
from pandas import read_csv
import cufflinks as cf


# Based on this recipe:
# https://discuss.streamlit.io/t/matplotlib-animation-in-streamlit-through-html-js/5587
with st.echo(code_location='below'):
    st.title("Hello, World!")
    """
    This is a test.
    """

    cf.go_offline()
    cf.set_config_file(offline=False, world_readable=True)
    GlobalTemp = pd.read_csv("https://gist.githubusercontent.com/TimurTalipov/68d7ca73f71349d63e685d7fb4c3b406/raw/35afc501060b9a53a79cad1ac8130df65748b3e4/GlobalTemperatures.csv", parse_dates= ['dt'])
    GlobalTempCountry = pd.read_csv("https://gist.githubusercontent.com/TimurTalipov/fb462f1045f4e227f2d3881cf864fb76/raw/eda82461e897b21a4cd729712293dee6e6994cef/GlobalLandTemperaturesByCountry.csv", parse_dates= ['dt'])
    GlobalTempState = pd.read_csv("https://gist.githubusercontent.com/TimurTalipov/1386e9213c52e49e93932efa2cb0cbea/raw/b7c2da931a3c23a41f44dcd380aab25464770ea8/GlobalLandTemperaturesByState.csv", parse_dates= ['dt'])
    GlobalTempMajorCity = pd.read_csv("https://gist.githubusercontent.com/TimurTalipov/7b1b830dbdec4fe9e6a3816ab5a0e08d/raw/eac257bb757be6d1a67eed11198bf64f257ccfb0/GlobalLandTemperaturesByMajorCity.csv", parse_dates= ['dt'])
    st.write(GlobalTemp)

    countries = np.unique(GlobalTempCountry['Country'])
    mean_temp = []
    for country in countries:
        mean_temp.append(GlobalTempCountry[GlobalTempCountry['Country'] == country]['AverageTemperature'].mean())
    fig = go.Figure(data=go.Choropleth(
        locations=countries,  # Spatial coordinates
        z=mean_temp,  # Data to be color-coded
        locationmode='country names',  # set of locations match entries in `locations`
        text=countries,
        colorscale='RdBu_r',
        colorbar_title="Average Temp",
    ))

    fig.update_layout(
        title_text='Average land temperature in countries',

    )

    fig.show()
