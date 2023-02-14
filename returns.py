# app.py, run with 'streamlit run app.py'
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Create a form to collect the user's input
with st.form(key='my_form', clear_on_submit=True):
    sku = st.text_input(label='SKU')
    quantity = st.number_input(label='Quantity', min_value=1, value=1)
    # Create a dropdown menu to select the reason for the return
    reason = st.selectbox(label='Reason', options=['Damaged', 'Wrong item', 'Too Small', ' Too Large','Changed Mind'])
    # Save and Append the user's input to a csv file and clear the user's input afeter saving
    if st.form_submit_button(label='Submit'):
        df = pd.DataFrame({'SKU': [sku], 'Quantity': [quantity], 'Reason': [reason]})
        df.to_csv('returns.csv', mode='a', header=False, index=False)
        st.success('Submitted successfully')

# Read the csv file and display the data in a table
df = pd.read_csv('returns.csv')

# Display how many returns were made for each reason by sku and quantity in a table
st.table(df.groupby(['sku', 'reason'])['quantity'].sum().head(10))

# Plot a bar of how many returns were made for each reason by sku and quantity
st.bar_chart(df.groupby(['sku', 'reason'])['quantity'].sum().unstack().head(10))



