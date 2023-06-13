import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import requests
import plotly.express as px


st.set_page_config(page_title='Indicador MACD', page_icon='https://avatars.githubusercontent.com/u/127362849?s=200&v=4', layout="wide")
st.sidebar.header("Indicador MACD")

coin_gecko_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd&include_24hr_change=true').json()
xrp_val = coin_gecko_response['ripple']['usd']
xrp_delta = coin_gecko_response['ripple']['usd_24h_change']

cripto_col1, cripto_col2, cripto_col3, cripto_col4 = st.columns(4)

# Add an icon to the first metric
with cripto_col1:
    # Set the columns to have no space between them
    col1, col2 = st.columns([1, 2])
    col1.image('assets/xrp-logo.png', use_column_width=True)
    # Grab only 2 characters from the string (0.00%)
    col2.metric(label="XRP", value="$"+str(xrp_val), delta=str(xrp_delta)[:4]+"%")

st.write('---')

'''
# Indicador MACD
'''

########### MACD 30 minutos ###########
macd_30_min = pd.read_csv('https://raw.githubusercontent.com/TICsonomics/Deployment/main/pdfs_output/ripple-macd-30%20minutos.csv')
with st.container():
    fig = go.Figure(data=go.Ohlc(x=macd_30_min.index,
                                 open=macd_30_min['open'],
                                 high=macd_30_min['high'],
                                 low=macd_30_min['low'],
                                 close=macd_30_min['close']))
    # Set a title for the chart
    fig.update_layout(
        title_text='MACD 30 minutos',
        xaxis_title="Index",
        yaxis_title="Price",
    )
    st.plotly_chart(fig, use_container_width=True)

with st.container():
    fig = px.line(macd_30_min, x=macd_30_min.index, y=macd_30_min['macd'])
    fig.update_layout(
        xaxis_title="Index",
        yaxis_title="MACD",
    )
    st.plotly_chart(fig, use_container_width=True)

st.dataframe(macd_30_min, use_container_width=True)

st.write('---')

########### MACD 4 horas ###########
macd_4_horas = pd.read_csv('https://raw.githubusercontent.com/TICsonomics/Deployment/main/pdfs_output/ripple-macd-4%20horas.csv')
with st.container():
    fig = go.Figure(data=go.Ohlc(x=macd_4_horas['date_price'],
                                    open=macd_4_horas['open'],
                                    high=macd_4_horas['high'],
                                    low=macd_4_horas['low'],
                                    close=macd_4_horas['close']))
    fig.update_layout(
        title_text='MACD 4 horas',
        xaxis_title="Date",
        yaxis_title="Price",
    )

    st.plotly_chart(fig, use_container_width=True)

with st.container():
    fig = px.line(macd_4_horas, x=macd_4_horas['date_price'], y=macd_4_horas['volume'])
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="MACD",
    )
    st.plotly_chart(fig, use_container_width=True)

st.dataframe(macd_4_horas, use_container_width=True)

st.write('---')

########### MACD 4 días ###########
macd_4_dias = pd.read_csv('https://raw.githubusercontent.com/TICsonomics/Deployment/main/pdfs_output/ripple-macd-4%20d%C3%ADas.csv')
with st.container():
    fig = go.Figure(data=go.Ohlc(x=macd_4_dias['date_price'],
                                    open=macd_4_dias['open'],
                                    high=macd_4_dias['high'],
                                    low=macd_4_dias['low'],
                                    close=macd_4_dias['close']))
    fig.update_layout(
        title_text='MACD 4 días',
        xaxis_title="Date",
        yaxis_title="Price",
    )
    st.plotly_chart(fig, use_container_width=True)

with st.container():
    fig = px.line(macd_4_dias, x=macd_4_dias['date_price'], y=macd_4_dias['volume'])
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="MACD",
    )
    st.plotly_chart(fig, use_container_width=True)

st.dataframe(macd_4_dias, use_container_width=True)