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
import seaborn as sns


# Based on this recipe:
# https://discuss.streamlit.io/t/matplotlib-animation-in-streamlit-through-html-js/5587
with st.echo(code_location='below'):
    st.title("Hello, World!")
    """
    Добро пожаловать! Сегодня мы будем исследовать температуру и все что с ней связано
    """
    GlobalTemp = pd.read_csv(r"C:\Users\Xiaomi\PycharmProjects\DataScience1stproject/GlobalTemperatures.csv")
    GlobalTempCountry = pd.read_csv(r"C:\Users\Xiaomi\PycharmProjects\DataScience1stproject/GlobalLandTemperaturesByCountry.csv")
    GlobalTempState = pd.read_csv(r"C:\Users\Xiaomi\PycharmProjects\DataScience1stproject/GlobalLandTemperaturesByState.csv")
    GlobalTempMajorCity = pd.read_csv(r"C:\Users\Xiaomi\PycharmProjects\DataScience1stproject/GlobalLandTemperaturesByMajorCity.csv")
    GlobalTempCountry.dropna(axis=0, inplace=True)
    GlobalTempMajorCity.dropna(axis=0, inplace=True)
    countries = np.unique(GlobalTempCountry['Country'])
    majorcities = np.unique(GlobalTempMajorCity['City'])
    st.write(countries)
    st.write(majorcities)
    mean_temp = []
    for country in countries:
        mean_temp.append(GlobalTempCountry[GlobalTempCountry['Country'] == country]['AverageTemperature'].mean())

    mean_temp_bar, countries_bar = (list(x) for x in zip(*sorted(zip(mean_temp, countries),
                                                                 reverse=True)))
    sns.set(font_scale=0.7)
    f, ax = plt.subplots(figsize=(5, 50))
    colors_cw = sns.color_palette('magma', len(countries))
    sns.barplot(mean_temp_bar, countries_bar, palette=colors_cw[::-1])
    Text = ax.set(xlabel='Average temperature', title='Average  temperature in countries and lands')
    st.pyplot(f)

    mean_temp_cities = []
    for city in majorcities:
        mean_temp_cities.append(GlobalTempMajorCity[GlobalTempMajorCity['City'] == city]['AverageTemperature'].mean())

    mean_temp_bar2, majorcities_bar = (list(x) for x in zip(*sorted(zip(mean_temp_cities, majorcities ),
                                                                 reverse=True)))
    sns.set(font_scale=1)
    f2, ax = plt.subplots(figsize=(10, 30))
    colors_cw = sns.color_palette('magma', len(majorcities))
    sns.barplot(mean_temp_bar2, majorcities_bar, palette=colors_cw[::-1])
    Text = ax.set(xlabel='Average temperature', title='Average temperature in cities')
    st.pyplot(f2)

    st.subheader("Из этих 2ух картинок мы можем сделать вывод об отрицательной корелляции средней температуры и уровня развития страны")
    st.subheader("Кому холодно, тот больше старается, получается:)")
    """
    P.S В Дании тепло! Просто она долгое время владела Гренландией
    """
    st.subheader("И вообще, кто-то из вас мог себе представить, что Рим теплее Мадрида, и что Богота(средняя высота над уровнем моря 2640 м), теплее чем Сан Пауло?")


