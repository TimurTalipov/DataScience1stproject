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
    GlobalTemp = pd.read_csv("https://github.com/TimurTalipov/DataScience1stproject/blob/main/GlobalTemperatures.csv",)
    GlobalTempCountry = pd.read_csv("https://github.com/TimurTalipov/DataScience1stproject/blob/main/GlobalLandTemperaturesByCountry.csv",)
    GlobalTempState = pd.read_csv("https://github.com/TimurTalipov/DataScience1stproject/blob/main/GlobalLandTemperaturesByState.csv",)

    st.write(GlobalTemp)

