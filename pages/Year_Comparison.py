import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create a title for the page
st.title('Returns by Year Comparison')

# Create a dropdown to select the month of the data to display
month = st.selectbox(label='Select Month', options=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

# Function to read data for the selected month and year
def read_data(year, month):
    file_path = f'pages/data/{year}/{month}-{year}.csv'
    return pd.read_csv(file_path)

# Read in the data for the selected month
try:
    df_2021 = read_data('2021', month)
    df_2022 = read_data('2022', month)
    df_2023 = read_data('2023', month)
except FileNotFoundError:
    st.header('No Data Available')

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


def read_and_concat_data(year):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    dataframes = []

    for month in months:
        file_path = f'pages/data/{year}/{month}-{year}.csv'
        df = pd.read_csv(file_path)
        dataframes.append(df)

    return pd.concat(dataframes)

# Concatenate the dataframe for all 2021 months and display total returns for 2021
df_2021 = read_and_concat_data('2021')

# Concatenate the dataframe for all 2022 months and display total returns for 2022
df_2022 = read_and_concat_data('2022')

# Concatenate the dataframe for all 2023 months and display total returns for 2023
df_2023 = read_and_concat_data('2023')


# Display the total quantity of returns for the selected month in a table name the first column 'Year' and the second column 'Quantity' and remove the index
st.table(pd.DataFrame({'Year': ['2021', '2022', '2023'], 'Quantity Returned': [df_2021['Quantity'].sum(), df_2022['Quantity'].sum(), df_2023['Quantity'].sum()]}).set_index('Year'))


# Create a bar chart to Compare the Total Quantity of Returns for 2021, 2022, and 2023 for the selected month
fig, ax = plt.subplots()
ax.bar(x=['2021', '2022', '2023'], height=[df_2021['Quantity'].sum(), df_2022['Quantity'].sum(), df_2023['Quantity'].sum()])
ax.set_title('Total Quantity of Returns for 2021, 2022, and 2023')
st.pyplot(fig)














