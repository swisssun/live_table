import streamlit as st
import requests
import pandas as pd
import time
import os
API_KEY = os.getenv("d180r99r01qteuvqhmk0d180r99r01qteuvqhmkg")
#API_KEY = 'd180r99r01qteuvqhmk0d180r99r01qteuvqhmkg'
symbols = {
    'Apple': 'AAPL',
    'Tesla': 'TSLA',
    'Microsoft': 'MSFT',
    'Google': 'GOOGL'
}

def get_quote(symbol):
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}"
    r = requests.get(url)
    data = r.json()
    return {
        'Current': data.get('c'),
        'Open': data.get('o'),
        'High': data.get('h'),
        'Low': data.get('l'),
        'Prev Close': data.get('pc'),
        'Change': round(data.get('c') - data.get('pc'), 2),
        'Change %': round(((data.get('c') - data.get('pc')) / data.get('pc')) * 100, 2)
    }

st.title("📈 Live Market Quotes")

placeholder = st.empty()

while True:
    rows = []
    for name, symbol in symbols.items():
        quote = get_quote(symbol)
        row = [name] + list(quote.values())
        rows.append(row)

    df = pd.DataFrame(rows, columns=["Instrument", "Current", "Open", "High", "Low", "Prev Close", "Change", "Change %"])
    placeholder.dataframe(df)
    time.sleep(5)
