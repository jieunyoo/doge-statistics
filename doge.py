import streamlit as st
import pandas as pd
import numpy as np
import datetime
import re
import base64
import altair as alt

st.title('Doge Coin Stats!')

st.text('Use your mouse to interact with this graph!')
st.text('Data from Nov. 11 2017 to Jan. 28 2022')

DATA_URL = ('https://raw.githubusercontent.com/jieunyoo/doge-statistics/main/doge.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state = st.text('Loading data...')
data = load_data(1540)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Volume')
chart = alt.Chart(data).mark_circle().encode( x='Date:T', y = 'Volume').interactive()
st.altair_chart(chart, use_container_width=True)

st.subheader('Open Price')
chartOpenValue = alt.Chart(data).mark_circle().encode( x='Date:T', y = 'Open').interactive()
st.altair_chart(chartOpenValue, use_container_width=True)

st.subheader('Close Price')
chartCloseValue = alt.Chart(data).mark_circle().encode( x='Date:T', y = 'Close').interactive()
st.altair_chart(chartCloseValue, use_container_width=True)
