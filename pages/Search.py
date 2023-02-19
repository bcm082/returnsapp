import streamlit as st
import pandas as pd

# Create a title for the page
st.title('Search by SKU')

# Search for SKU
sku = st.text_input(label='Enter SKU')

# Drop down to select the year of the data to display
year = st.selectbox(label='Select Year', options=['2021', '2022', '2023'])

# Search for SKU on the selected year in the csv file Column SKU
if year == '2021':
    # Concatenate all the csv files in the folder 2021
    df_2021_files = pd.concat(map(pd.read_csv, ['pages/data/2021/January-2021.csv', 'pages/data/2021/February-2021.csv', 'pages/data/2021/March-2021.csv', 'pages/data/2021/April-2021.csv', 'pages/data/2021/May-2021.csv', 'pages/data/2021/June-2021.csv', 'pages/data/2021/July-2021.csv', 'pages/data/2021/August-2021.csv', 'pages/data/2021/September-2021.csv', 'pages/data/2021/October-2021.csv', 'pages/data/2021/November-2021.csv', 'pages/data/2021/December-2021.csv']))
    
    # read the csv file for the year 2021 total sold
    df_2021_total_sold = pd.read_csv('pages/data/2021/2021-Total-Sold.csv')

    # Filter the data based on the SKU entered based on partial match
    df_2021 = df_2021_files[df_2021_files['SKU'].str.contains(sku)]

    # Filter the data based on the SKU entered based on partial match on the total sold
    df_2021_total_sold = df_2021_total_sold[df_2021_total_sold['SKU'].str.contains(sku)]

    # Display in one table the total return quantity and total sold quantity for the sku searched and display the whole number for Total Sold Quantity
    df_2021_total = df_2021.groupby('SKU')['Quantity'].sum().reset_index().sort_values('Quantity', ascending=False).merge(df_2021_total_sold.groupby('SKU')['Quantity'].sum().reset_index().sort_values('Quantity', ascending=False), on='SKU', how='left').fillna(0).astype({'Quantity_x': 'int64', 'Quantity_y': 'int64'}).rename(columns={'Quantity_x': 'Returned Quantity', 'Quantity_y': 'Sold Quantity'})
    
    # if the SKU is not found, display a message
    if df_2021.empty:
        st.write('SKU not found')
    else:
        # Display df_2021_total in a table
        st.subheader('Total Return Quantity' + ' - ' + year)
        st.table(df_2021_total)
        st.subheader('Reason of the Return')
        # Display the total return by Sku and reason
        st.table(df_2021.groupby(['SKU', 'Reason'])['Quantity'].sum().reset_index().sort_values('Quantity', ascending=False).head(10))



################################
# Start 2022

elif year == '2022':
    # Concatenate all the csv files in the folder 2022
    df_2022_files = pd.concat(map(pd.read_csv, ['pages/data/2022/January-2022.csv', 'pages/data/2022/February-2022.csv', 'pages/data/2022/March-2022.csv', 'pages/data/2022/April-2022.csv', 'pages/data/2022/May-2022.csv', 'pages/data/2022/June-2022.csv', 'pages/data/2022/July-2022.csv', 'pages/data/2022/August-2022.csv', 'pages/data/2022/September-2022.csv', 'pages/data/2022/October-2022.csv', 'pages/data/2022/November-2022.csv', 'pages/data/2022/December-2022.csv']))

    # Filter the data based on the SKU entered based on partial match
    df_2022 = df_2022_files[df_2022_files['SKU'].str.contains(sku)]

    # read the csv file for the year 2022 total sold
    df_2022_total_sold = pd.read_csv('pages/data/2022/2022-Total-Sold.csv')

    df_2022_total_sold = df_2022_total_sold[df_2022_total_sold['SKU'].str.contains(sku)]

    df_2022_total = df_2022.groupby('SKU')['Quantity'].sum().reset_index().sort_values('Quantity', ascending=False).merge(df_2022_total_sold.groupby('SKU')['Quantity'].sum().reset_index().sort_values('Quantity', ascending=False), on='SKU', how='left').fillna(0).astype({'Quantity_x': 'int64', 'Quantity_y': 'int64'}).rename(columns={'Quantity_x': 'Returned Quantity', 'Quantity_y': 'Sold Quantity'})

    # if the SKU is not found, display a message
    if df_2022.empty:
        st.write('SKU not found')
    else:
        # Display df_2021_total in a table
        st.subheader('Total Return Quantity'+ ' - ' + year)
        st.table(df_2022_total)
        st.subheader('Reason of the Return')
        # Display the total return by Sku and reason
        st.table(df_2022.groupby(['SKU', 'Reason'])['Quantity'].sum().reset_index().sort_values('Quantity', ascending=False).head(10))



#####################################

# Start 2023

elif year == '2023':
    # Concatenate all the csv files in the folder 2023
    df_2023_files = pd.concat(map(pd.read_csv, ['pages/data/2023/January-2023.csv', 'pages/data/2023/February-2023.csv', 'pages/data/2023/March-2023.csv', 'pages/data/2023/April-2023.csv', 'pages/data/2023/May-2023.csv', 'pages/data/2023/June-2023.csv', 'pages/data/2023/July-2023.csv', 'pages/data/2023/August-2023.csv', 'pages/data/2023/September-2023.csv', 'pages/data/2023/October-2023.csv', 'pages/data/2023/November-2023.csv', 'pages/data/2023/December-2023.csv']))

    # Filter the data based on the SKU entered based on partial match
    df_2023 = df_2023_files[df_2023_files['SKU'].str.contains(sku)]

    df_2023_total_sold = pd.read_csv('pages/data/2023/2023-Total-Sold.csv')

    df_2023_total_sold = df_2023_total_sold[df_2023_total_sold['SKU'].str.contains(sku)]

    df_2023_total = df_2023.groupby('SKU')['Quantity'].sum().reset_index().sort_values('Quantity', ascending=False).merge(df_2023_total_sold.groupby('SKU')['Quantity'].sum().reset_index().sort_values('Quantity', ascending=False), on='SKU', how='left').fillna(0).astype({'Quantity_x': 'int64', 'Quantity_y': 'int64'}).rename(columns={'Quantity_x': 'Returned Quantity', 'Quantity_y': 'Sold Quantity'})

    # if the SKU is not found, display a message
    if df_2023.empty:
        st.write('SKU not found')
    else:
        # Display df_2021_total in a table
        st.subheader('Total Return Quantity'+ ' - ' + year)
        st.table(df_2023_total)
        st.subheader('Reason of the Return')
        # Display the total return by Sku and reason
        st.table(df_2023.groupby(['SKU', 'Reason'])['Quantity'].sum().reset_index().sort_values('Quantity', ascending=False).head(10))


