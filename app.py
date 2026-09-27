import requests
import streamlit as st

url = "https://open.er-api.com/v6/latest/USD"
data = requests.get(url).json()
rates = data["rates"]

st.title("อัตราแลกเปลี่ยนจาก USD")
st.header(f"1 USD = {rates['THB']:.2f} THB")

currencies = list(rates.keys())
currency = st.selectbox("เลือกสกุลเงินอื่น", currencies, index=currencies.index("THB"))

st.write(f"1 USD = {rates[currency]:.2f} {currency}")
