import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create a title for the page
st.title('Returns by Year Comparison')


# Create a dropdown to select the month of the data to display
month = st.selectbox(label='Select Month', options=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

# Read in the data for the selected month
if month == 'January':
    df_2021 = pd.read_csv('pages/data/2021/January-2021.csv')
    df_2022 = pd.read_csv('pages/data/2022/January-2022.csv')
    df_2023 = pd.read_csv('pages/data/2023/January-2023.csv')
elif month == 'February':
    df_2021 = pd.read_csv('pages/data/2021/February-2021.csv')
    df_2022 = pd.read_csv('pages/data/2022/February-2022.csv')
    df_2023 = pd.read_csv('pages/data/2023/February-2023.csv')
elif month == 'March':
    df_2021 = pd.read_csv('pages/data/2021/March-2021.csv')
    df_2022 = pd.read_csv('pages/data/2022/March-2022.csv')
    df_2023 = pd.read_csv('pages/data/2023/March-2023.csv')
elif month == 'April':
    df_2021 = pd.read_csv('pages/data/2021/April-2021.csv')
    df_2022 = pd.read_csv('pages/data/2022/April-2022.csv')
    df_2023 = pd.read_csv('pages/data/2023/April-2023.csv')
elif month == 'May':
    df_2021 = pd.read_csv('pages/data/2021/May-2021.csv')
    df_2022 = pd.read_csv('pages/data/2022/May-2022.csv')
    df_2023 = pd.read_csv('pages/data/2023/May-2023.csv')
elif month == 'June':
    df_2021 = pd.read_csv('pages/data/2021/June-2021.csv')
    df_2022 = pd.read_csv('pages/data/2022/June-2022.csv')
    df_2023 = pd.read_csv('pages/data/2023/June-2023.csv')
elif month == 'July':
    df_2021 = pd.read_csv('pages/data/2021/July-2021.csv')
    df_2022 = pd.read_csv('pages/data/2022/July-2022.csv')
    df_2023 = pd.read_csv('pages/data/2023/July-2023.csv')
elif month == 'August':
    df_2021 = pd.read_csv('pages/data/2021/August-2021.csv')
    df_2022 = pd.read_csv('pages/data/2022/August-2022.csv')
    df_2023 = pd.read_csv('pages/data/2023/August-2023.csv')
elif month == 'September':
    df_2021 = pd.read_csv('pages/data/2021/September-2021.csv')
    df_2022 = pd.read_csv('pages/data/2022/September-2022.csv')
    df_2023 = pd.read_csv('pages/data/2023/September-2023.csv')
elif month == 'October':
    df_2021 = pd.read_csv('pages/data/2021/October-2021.csv')
    df_2022 = pd.read_csv('pages/data/2022/October-2022.csv')
    df_2023 = pd.read_csv('pages/data/2023/October-2023.csv')
elif month == 'November':
    df_2021 = pd.read_csv('pages/data/2021/November-2021.csv')
    df_2022 = pd.read_csv('pages/data/2022/November-2022.csv')
    df_2023 = pd.read_csv('pages/data/2023/November-2023.csv')
elif month == 'December':
    df_2021 = pd.read_csv('pages/data/2021/December-2021.csv')
    df_2022 = pd.read_csv('pages/data/2022/December-2022.csv')
    df_2023 = pd.read_csv('pages/data/2023/December-2023.csv')

st.markdown("---")

st.header('Data from ' + month)

# Display the total quantity of returns for the selected month in a table name the first column 'Year' and the second column 'Quantity' and remove the index
st.table(pd.DataFrame({'Year': ['2021', '2022', '2023'], 'Quantity Returned': [df_2021['Quantity'].sum(), df_2022['Quantity'].sum(), df_2023['Quantity'].sum()]}).set_index('Year'))


# Create a bar chart to Compare the Total Quantity of Returns for 2021, 2022, and 2023 for the selected month
fig, ax = plt.subplots()
ax.bar(x=['2021', '2022', '2023'], height=[df_2021['Quantity'].sum(), df_2022['Quantity'].sum(), df_2023['Quantity'].sum()])
ax.set_title('Total Quantity of Returns for ' + month + ' 2021, 2022, and 2023')
st.pyplot(fig)

st.markdown('---')

st.header('Total Returns per Year')

# Concatenate the dataframe for all 2021 months and display total returns for 2021
df_2021 = pd.concat([pd.read_csv('pages/data/2021/January-2021.csv'), pd.read_csv('pages/data/2021/February-2021.csv'), pd.read_csv('pages/data/2021/March-2021.csv'), pd.read_csv('pages/data/2021/April-2021.csv'), pd.read_csv('pages/data/2021/May-2021.csv'), pd.read_csv('pages/data/2021/June-2021.csv'), pd.read_csv('pages/data/2021/July-2021.csv'), pd.read_csv('pages/data/2021/August-2021.csv'), pd.read_csv('pages/data/2021/September-2021.csv'), pd.read_csv('pages/data/2021/October-2021.csv'), pd.read_csv('pages/data/2021/November-2021.csv'), pd.read_csv('pages/data/2021/December-2021.csv')])

# Concatenate the dataframe for all 2022 months and display total returns for 2022
df_2022 = pd.concat([pd.read_csv('pages/data/2022/January-2022.csv'), pd.read_csv('pages/data/2022/February-2022.csv'), pd.read_csv('pages/data/2022/March-2022.csv'), pd.read_csv('pages/data/2022/April-2022.csv'), pd.read_csv('pages/data/2022/May-2022.csv'), pd.read_csv('pages/data/2022/June-2022.csv'), pd.read_csv('pages/data/2022/July-2022.csv'), pd.read_csv('pages/data/2022/August-2022.csv'), pd.read_csv('pages/data/2022/September-2022.csv'), pd.read_csv('pages/data/2022/October-2022.csv'), pd.read_csv('pages/data/2022/November-2022.csv'), pd.read_csv('pages/data/2022/December-2022.csv')])

# Concatenate the dataframe for all 2023 months and display total returns for 2023
df_2023 = pd.concat([pd.read_csv('pages/data/2023/January-2023.csv'), pd.read_csv('pages/data/2023/February-2023.csv'), pd.read_csv('pages/data/2023/March-2023.csv'), pd.read_csv('pages/data/2023/April-2023.csv'), pd.read_csv('pages/data/2023/May-2023.csv'), pd.read_csv('pages/data/2023/June-2023.csv'), pd.read_csv('pages/data/2023/July-2023.csv'), pd.read_csv('pages/data/2023/August-2023.csv'), pd.read_csv('pages/data/2023/September-2023.csv'), pd.read_csv('pages/data/2023/October-2023.csv'), pd.read_csv('pages/data/2023/November-2023.csv'), pd.read_csv('pages/data/2023/December-2023.csv')])

# Display the total quantity of returns for the selected month in a table name the first column 'Year' and the second column 'Quantity' and remove the index
st.table(pd.DataFrame({'Year': ['2021', '2022', '2023'], 'Quantity Returned': [df_2021['Quantity'].sum(), df_2022['Quantity'].sum(), df_2023['Quantity'].sum()]}).set_index('Year'))


# Create a bar chart to Compare the Total Quantity of Returns for 2021, 2022, and 2023 for the selected month
fig, ax = plt.subplots()
ax.bar(x=['2021', '2022', '2023'], height=[df_2021['Quantity'].sum(), df_2022['Quantity'].sum(), df_2023['Quantity'].sum()])
ax.set_title('Total Quantity of Returns for 2021, 2022, and 2023')
st.pyplot(fig)














