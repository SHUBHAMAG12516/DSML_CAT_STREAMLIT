import yfinance as yf
import streamlit as st
import datetime
stock=st.text_input("MSFT","GOOG")
data = yf.Ticker(stock)
st.header("This is a Analysing APP")
st.write("Currently Analyzing",stock)
# get historical market data
col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Enter the start date", datetime.date(2019, 7, 6))


with col2:
    end_date = st.date_input("Enter the end date", datetime.date(2020, 4, 6))



hist = data.history(period="1d",start=start_date,end=end_date)


st.write(hist)
st.bar_chart(hist['High'])
st.header("This is a Close Trend Chart")
st.line_chart(hist['Close'])