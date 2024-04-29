import pandas as pd
import numpy as np
import streamlit as st

# Load data
flipkart = pd.read_csv('flipkart_products.csv')
amazon = pd.read_csv('amazon_products.csv')

# Preprocess data
def preprocess(flipkart, amazon):
    flipkart = flipkart.drop('Original Price', axis=1)
    amazon = amazon.dropna()

    flipkart.rename(columns={'Rating':'Flipkart Rating', 'Selling Price':'Flipkart Price'}, inplace=True) 
    amazon.rename(columns={'Ratings':'Amazon Rating', 'Selling price':'Amazon Price'}, inplace=True) 

    df = pd.merge(flipkart, amazon, on=['Brand', 'Model', 'Color', 'Memory', 'Storage'])
    df['Model_name'] = df['Brand'] + '-' + df['Model'] + '-' + df['Color'] + '-' + df['Memory'] + '-' + df['Storage']

    return df

df = preprocess(flipkart, amazon)

# Page layout
st.set_page_config(layout="wide")

# Header
st.title('Price Comparison Website')
st.markdown('---')

# Sidebar
st.sidebar.title('Select Model')
model_name = st.sidebar.selectbox(
    label='',
    options=df['Model_name'])

# Main content
if model_name:
    st.sidebar.markdown('---')
    selected_model = df[df['Model_name'] == model_name].iloc[0]
    st.header(model_name)

    # Basic details
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Basic Details')
        st.write(f"**Brand:** {selected_model['Brand']}")
        st.write(f"**Model:** {selected_model['Model']}")
        st.write(f"**Color:** {selected_model['Color']}")
        st.write(f"**Memory:** {selected_model['Memory']}")
        st.write(f"**Storage:** {selected_model['Storage']}")

    # Ratings and Prices
    with col2:
        st.subheader('Ratings and Prices')
        st.write(f"**Flipkart Rating:** {selected_model['Flipkart Rating']}")
        st.write(f"**Flipkart Price:** {selected_model['Flipkart Price']}")
        st.write(f"**Amazon Rating:** {selected_model['Amazon Rating']}")
        st.write(f"**Amazon Price:** {selected_model['Amazon Price']}")
