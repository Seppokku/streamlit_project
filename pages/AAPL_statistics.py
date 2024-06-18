import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns


st.write("""
         
     # Simple visualized statistics of AAPL

     ## Click on checkboxes to see simple statistics!
         
         """)

ticker_data = yf.Ticker('AAPL')
ticker_df = ticker_data.history(period='5y')

but1 = st.sidebar.checkbox('Show OPEN/CLOSE statictics')
if but1:
    st.write('### OPEN STATISTICS')
    st.line_chart(ticker_df['Open'], color='#80ff00')
    st.write('### CLOSE STATISTICS')
    st.line_chart(ticker_df['Close'], color='#ff4000')


but2 = st.sidebar.checkbox('Show HIGH/LOW statictics')
if but2:
    st.write('### HIGH STATISTICS')
    st.line_chart(ticker_df['High'], color='#80ff00')
    st.write('### LOW STATISTICS')
    st.line_chart(ticker_df['Low'], color='#ff4000')

but3 = st.sidebar.checkbox('Show VOLUME statictics')
if but3:
    st.write('### VOLUME STATISTICS')
    st.line_chart(ticker_df['Volume'])





