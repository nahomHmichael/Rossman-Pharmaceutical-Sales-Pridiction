import streamlit as st
import pandas as pd
import numpy as np
import datetime

def app():
    with st.spinner("Loading Home ..."):
        
        st.markdown("<p style='padding:2rem;text-align:center; background-color:#3761B5;color:#FFFFFF;font-size:1.8rem;border-radius:0.8rem;'>Prediction display</p>", unsafe_allow_html=True)
    
        # read the data
        data = pd.read_csv('dashboard/datasets/prediction_df.csv', index_col = 'Date')

       
        st.sidebar.subheader('Enter date ranges')

        # make the index a datetime object
        data['Date'] = data.index
        data.Date = pd.to_datetime(data.Date)

        # create inputs for date ranges
        start_date = st.sidebar.text_input('start date', "2015-9-10")
        end_date = st.sidebar.text_input('end date', "2015-9-20")
        # convert the inputs to timestamps
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

        # filter the data using the inputs
        date_slice = np.logical_and(data.Date >= start_date, data.Date <= end_date)
        sliced_df = data[date_slice]

        # create an input for store id
        st.sidebar.subheader('Input Store ID')
        store_id = st.sidebar.number_input('Store ID', 1)
        store_data = sliced_df.loc[sliced_df.Store == store_id]
        #display data
        st.write(store_data)