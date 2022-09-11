import streamlit as st
from multiapp import MultiApp
from dashboard import data,home,insights,predict,predict_view # import your app modules here

app = MultiApp()

st.sidebar.markdown('# **Pharmaceutical Sales forcasting**')
st.sidebar.markdown("""
The aim of this project is to predict the sales six weeks ahead across all the stores of the Rossman Pharmaceutical company using Machine and Deep Learning. The different factors affecting the sales are: promotions, competitions, school-state holiday, seasonality, and locality.

""")

# Add all your application here
app.add_app("Home page", home.app)
app.add_app("Data sets", data.app)
app.add_app("Insights", insights.app)
app.add_app("Predicting page", predict.app)
app.add_app("Prediction display", predict_view.app)
# The main app
app.run()