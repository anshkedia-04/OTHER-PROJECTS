import streamlit as st
import requests

# Function to get exchange rate from an API
def get_exchange_rate(from_currency, to_currency):
    api_key = "070db7808912f271a0d3d309"  
    url = f"https://v6.exchan+gerate-api.com/v6/070db7808912f271a0d3d309/latest/INR"
    
    response = requests.get(url)
    data = response.json()
    
    if data['result'] == 'success':
        return data['conversion_rates'].get(to_currency)
    else:
        st.error("Unable to fetch exchange rates.")
        return None

# Streamlit App UI
st.title("Currency Exchange and Converter")
st.markdown("Convert from one currency to another.")

# User inputs for the amount and currencies
from_currency = st.selectbox("From Currency", ["USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD", "CHF"])
to_currency = st.selectbox("To Currency", ["USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD", "CHF"])

amount = st.number_input("Enter Amount", min_value=0.0, format="%.2f")

# Convert the currency when the user clicks "Convert"
if st.button("Convert"):
    if amount > 0:
        # Fetch the exchange rate
        rate = get_exchange_rate(from_currency, to_currency)
        
        if rate:
            converted_amount = amount * rate
            st.success(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        st.warning("Please enter a valid amount.")
