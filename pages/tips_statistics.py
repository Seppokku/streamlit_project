import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import random

def give_time():
    date = datetime.date(2023, 1, random.randint(1, 31))
    return date.strftime("%Y-%m-%d")



st.write("""
         
     # Simple visualized statistics of tips

     ## Click on checkboxes to see simple plots!
         
         """)

def load_data(url):
    df = pd.read_csv(url) 
    return df


df = load_data("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

df['time_order'] = [give_time() for _ in range(len(df))]


but1 = st.sidebar.checkbox('Show total bill count statictics')
if but1:
    fig, ax = plt.subplots()
    sns.histplot(data=df, x="total_bill", kde=True)
    ax.set_title('total bill count')
    ax.set_ylabel('totall bill')
    ax.set_xlabel('count')
    st.pyplot(fig)


but2 = st.sidebar.toggle('Tips heatmap')
if but2:
    img = st.image('heatmap_tips.png', caption='Tips heatmap')
    st.write('### Also you can download it!!!')

    with open("heatmap_tips.png", "rb") as file:
        downld_btn = st.download_button(
                label="Download image",
                data=file,
                file_name="heat_map.png",
                mime="image/png"
            )
    