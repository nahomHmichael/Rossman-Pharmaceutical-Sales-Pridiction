import streamlit as st
import awesome_streamlit as ast
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def app():
    with st.spinner("Loading Plots ..."):
        st.title('Data Visualisation')
        st.subheader('The distribution of Promotions and Customers')
        st.image('plots/promo_and_customers.png')
        
        st.subheader('The distribution of Promotions and Sales')
        st.image('plots/promo_and_sales.png')
        st.subheader('Average Sales')
        st.image('plots/average_sales.png')
        st.subheader('Sales on Holidays')
        st.image('plots/sales_during_holidays.png')
        st.write("Here we can see sales in ordinary days are high") 
                                                                         
        st.subheader('Seasonality Check')
        st.image('plots/seasonality.png')
        st.write('AS we can see there is no seasonality on sales. Sales follows a similar trend in all the months. ')
        
        st.subheader('Christmas Sales of 2013/14')
        st.image('plots/xmass_sales_13-14.jpg')
        
        st.subheader('Christmas Sales of 2014/15')
        st.image('plots/xmass_sales_14-15.jpg')

        st.subheader('Easter Sales of 2013/14')
        st.image('plots/easter_sales_13-14.jpg')

        st.subheader('Easter Sales of 2014/15')
        st.image('plots/easter_sales_14-15.jpg')
        
        st.subheader('Correlation Between Sales and Promo')
        st.image('plots/sales_promo_corr.png')
        st.write('There is a strong correlation between sales and promo.')
        
        st.subheader('Correlation Between Sales and Customers')
        st.image('plots/corr_bn_sales_and_customers.png')
        st.write('There is a strong correlation between sales and customer number.')
        
        st.subheader('Yearly Sales vs Promotions')
        st.image('plots/yearly_sales_vs_promo_factor.png')
        
        st.subheader('Weekly Sales Trend per Store Types')
        st.image('plots/customer_vs_week_viz.jpg')
        
        st.subheader('Assortment Type Effect on Sales')
        st.image('plots/assortment.jpg')

        st.subheader('Yearly Sales per Assortment Type')
        st.image('plots/sales_assortment_factoralPlot.jpg')
        
        st.subheader('Correlation Between Features')
        st.image('plots/corr_competition_vs_sales.png')

        
        
        
        