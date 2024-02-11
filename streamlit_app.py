import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
country = st.text_input('Country?')
path = 'https://raw.githubusercontent.com/TheEconomist/big-mac-data/master/output-data/big-mac-raw-index.csv'
bigmac_df = pd.read_csv(path)
bigmac_df_filtered = bigmac_df.loc[bigmac_df['name'] == country][['date', 'name', 'dollar_price']]
st.line_chart(data=bigmac_df_filtered, x='date', y='dollar_price')
