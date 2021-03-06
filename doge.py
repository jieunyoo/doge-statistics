import streamlit as st
import pandas as pd
import numpy as np
import datetime
import altair as alt
from PIL import Image

#image = Image.open('https://github.com/jieunyoo/doge-statistics/blob/main/dogecoinSmall.jpg')
image = Image.open('dogecoinSmall.jpg')

st.title('Doge Coin Stats!')
st.text('Currency used: Indian INR')
st.image(image)

st.text('Use your mouse to interact with this graph!')
st.text('Data from Nov. 11 2017 to Jan. 28 2022')

DATA_URL = ('https://raw.githubusercontent.com/jieunyoo/doge-statistics/main/doge.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state = st.text('Loading data...')
data = load_data(1540)
data_load_state.text("Done loading data!")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

nearest = alt.selection(type='single', nearest=True, on='mouseover', fields=['Date'], empty='none')

line0 = alt.Chart().mark_line(interpolate='basis').encode(
    alt.X('Date:T', axis=alt.Axis(title='')),
    alt.Y('Open:Q', axis=alt.Axis(title='',format='$f'))
)
selectors0 = alt.Chart().mark_point().encode(
    x='Date:T',
    opacity=alt.value(0),
).add_selection(
    nearest
)
points0 = line0.mark_point().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)
text0 = line0.mark_text(align='left', dx=5, dy=-5).encode(
    text=alt.condition(nearest, 'Volume:Q', alt.value(' '))
)
rules0 = alt.Chart().mark_rule(color='gray').encode(
    x='Date:T',
).transform_filter(
    nearest
)


##Volume + Toolbar
st.subheader('Volume')
chart = alt.layer(line0, selectors0, points0, rules0, text0, data=DATA_URL, width=600, height=300,title='Stock Volume').interactive()
st.altair_chart(chart, use_container_width=True)


##Open Price + Toolbar
nearest = alt.selection(type='single', nearest=True, on='mouseover', fields=['Date'], empty='none')

line1 = alt.Chart().mark_line(interpolate='basis').encode(
    alt.X('Date:T', axis=alt.Axis(title='')),
    alt.Y('Open:Q', axis=alt.Axis(title='',format='$f'))
)

selectors1 = alt.Chart().mark_point().encode(
    x='Date:T',
    opacity=alt.value(0),
).add_selection(
    nearest
)
points1 = line1.mark_point().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)
text1 = line1.mark_text(align='left', dx=5, dy=-5).encode(
    text=alt.condition(nearest, 'Open:Q', alt.value(' '))
)
rules1 = alt.Chart().mark_rule(color='gray').encode(
    x='Date:T',
).transform_filter(
    nearest
)

st.subheader('Open Price')
#chartOpenValue = alt.Chart(data).mark_circle().encode( x='Date:T', y = 'Open').interactive()
#st.altair_chart(chartOpenValue, use_container_width=True)

chartOpenValue = alt.layer(line1, selectors1, points1, rules1, text1, data=DATA_URL, width=600, height=300,title='Stock Open Price').interactive()
st.altair_chart(chartOpenValue,use_container_width=True)


##Close Price + Toolbar
line = alt.Chart().mark_line(interpolate='basis').encode(
    alt.X('Date:T', axis=alt.Axis(title='')),
    alt.Y('Close:Q', axis=alt.Axis(title='',format='$f'))
)

selectors = alt.Chart().mark_point().encode(
    x='Date:T',
    opacity=alt.value(0),
).add_selection(
    nearest
)
points = line.mark_point().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)
text = line.mark_text(align='left', dx=5, dy=-5).encode(
    text=alt.condition(nearest, 'Close:Q', alt.value(' '))
)
rules = alt.Chart().mark_rule(color='gray').encode(
    x='Date:T',
).transform_filter(
    nearest
)

st.subheader('Close Price')
stockChart = alt.layer(line, selectors, points, rules, text, data=DATA_URL, width=600, height=300,title='Stock Close Price').interactive()
st.altair_chart(stockChart,use_container_width=True)
