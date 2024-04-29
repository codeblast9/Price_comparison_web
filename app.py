import pandas as pd
import numpy as np
import streamlit as st

flipkart = pd.read_csv('flipkart_products.csv')
amazon = pd.read_csv('amazon_products.csv')

def preprocess(flipkart, amazon):
    flipkart = flipkart.drop('Original Price', axis=1)
    amazon = amazon.dropna()

    flipkart.rename(columns={'Rating':'flipkart_rating', 'Selling Price':'flipkart_price'}, inplace=True) 
    amazon.rename(columns={'Ratings':'amazon_rating', 'Selling price':'amazon_price'}, inplace=True) 

    df = pd.merge(flipkart, amazon, on=['Brand', 'Model', 'Color', 'Memory', 'Storage'])
    df['Model_name'] = df['Brand'] + '-' + df['Model'] + '-' + df['Color'] + '-' + df['Memory'] + '-' + df['Storage']

    return df

df = preprocess(flipkart, amazon)

st.header('Price Comparison Website', divider='red')

options = st.multiselect(
    label='Select Models',
    options=df['Model_name'],
    key='model_options')

# Display details of selected models in one row
if options:
    col1, col2, col3 = st.columns(3)
    for index, model_name in enumerate(options):
        selected_model = df[df['Model_name'] == model_name].iloc[0]
        with eval(f"col{index + 1}"):
            st.subheader(model_name)
            st.write('Brand:', selected_model['Brand'])
            st.write('Model:', selected_model['Model'])
            st.write('Color:', selected_model['Color'])
            st.write('Memory:', selected_model['Memory'])
            st.write('Storage:', selected_model['Storage'])
            st.write('Flipkart Rating:', selected_model['flipkart_rating'])
            st.write('Flipkart Price:', selected_model['flipkart_price'])
            st.write('Amazon Rating:', selected_model['amazon_rating'])
            st.write('Amazon Price:', selected_model['amazon_price'])
