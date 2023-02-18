import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create a title for the page
st.title('Returns Reason Dashboard - 2022')
st.write('Amazon Data from January 2022 to December 2022.')


# Create a dropdown to select the month of the data to display
month = st.selectbox(label='Select Month', options=['January'])

# If January is selected, display the data for January
if month == 'January':
    df_2022 = pd.read_csv('pages/data/2022/January-2022.csv')
    df_2023 = pd.read_csv('pages/data/2023/January-2023.csv')


st.subheader('Data from ' + month + ' 2022 vs 2023')
st.write('Total Returns 2022: ' + str(df_2022['Quantity'].sum())) 
st.write('Total Returns 2023: ' + str(df_2023['Quantity'].sum()))

# Calulate the percentage difference between 2022 and 2023
st.write('Percentage Difference: ' + str(round(((df_2023['Quantity'].sum() - df_2022['Quantity'].sum()) / df_2022['Quantity'].sum()) * 100, 2)) + '%')


# Create a bar chart to Compare the Total Quantity of Returns for 2022 and 2023 for the selected month
fig, ax = plt.subplots()
ax.bar(x=['2022', '2023'], height=[df_2022['Quantity'].sum(), df_2023['Quantity'].sum()])
ax.set_title('Total Quantity of Returns for ' + month + ' 2022 and 2023')
st.pyplot(fig)













