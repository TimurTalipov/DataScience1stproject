import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from celluloid import Camera
from pandas import read_csv
import seaborn as sns
import plotly.offline as py

with st.echo(code_location='below'):
    st.title("Hello, World!")
    """
    Добро пожаловать! Сегодня мы будем исследовать температуру и все что с ней связано
    """
    #GlobalTemp = pd.read_csv(r"C:\Users\Xiaomi\PycharmProjects\DataScience1stproject/GlobalTemperatures.csv")
    GlobalTempCountry = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
    GlobalTempState = pd.read_csv("GlobalLandTemperaturesByState.csv")
    GlobalTempMajorCity = pd.read_csv("GlobalLandTemperaturesByMajorCity.csv")
    GlobalTempMajorCity.dropna(axis=0, inplace=True)
    GlobalTempState.dropna(axis=0, inplace=True)
    countries = np.unique(GlobalTempCountry['Country'])
    majorcities = np.unique(GlobalTempMajorCity['City'])

    """ 
   Сначала посмотрим на среднюю температуру стран
    """

    GlobalTempCountry.dropna(axis=0, inplace=True)
    ### FROM: https://www.kaggle.com/benthecoder/exploratory-data-analysis-with-python ( я менял параметры но смысл отсюда)
    mean_temp = []
    for country in countries:
        mean_temp.append(GlobalTempCountry[GlobalTempCountry['Country'] == country]['AverageTemperature'].mean())

    mean_temp_bar, countries_bar = (list(x) for x in zip(*sorted(zip(mean_temp, countries),
                                                                 reverse=True)))
    sns.set(font_scale=0.7)
    f, ax = plt.subplots(figsize=(5, 50))
    colors_cw = sns.color_palette('magma', len(countries))
    sns.barplot(mean_temp_bar, countries_bar, palette=colors_cw[::-1])
    Text = ax.set(xlabel='Average temperature', title='Average  temperature in countries and lands')  ### END FROM
    st.pyplot(f)

    """ Посмотрим на среднюю температуру крупных городов
    """
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

    st.subheader("А теперь давайте займемся Россией и интерактивными штуками")
    """
    Для того чтобы получить данные пришлось повозиться, так как изначанльый размер >30 МБ, но я успешно справился с задачей
    РАБОТАЕТ МЕДЛЕННО,но ведь работает(невероятно), лучше выбирать более поздние года, для более точных данных.
    """
    GlobalTempState = GlobalTempState.rename(columns={'1743-11-01':'Date','4.537':'AverageTemperature','Adygey':'State'})
    oblast = np.unique(GlobalTempState['State'])
    select = st.selectbox('Выберите область', oblast)
    god= st.slider("выберите год начала отсчета",min_value=1750,max_value=2010)
    GlobalTempState['Date'] = pd.to_datetime(GlobalTempState['Date'])
    GlobalTempState['year'] = GlobalTempState['Date'].dt.year
    GlobalTempState['month'] = GlobalTempState['Date'].dt.month_name()
    GlobalTempState['day'] = GlobalTempState['Date'].dt.day
    select_temp = GlobalTempState[GlobalTempState['State'] == select]
    yearly_avg_temperature = pd.DataFrame(select_temp.groupby('year')['AverageTemperature'].mean()).reset_index()
    yearly_avg_temperature = yearly_avg_temperature[yearly_avg_temperature['year'] > god]
    fig3=plt.figure(figsize=(13, 7))
    plt.plot(yearly_avg_temperature['year'], yearly_avg_temperature['AverageTemperature'], label='Average Temperature')
    plt.legend()
    st.pyplot(fig3)
    st.subheader("Как вам глобальное потепление,друзья?")

    """"Настало время красотыs"""

