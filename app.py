import streamlit as st

import datetime
import requests


# '''
# # TaxiFareModel front

# This front queries the Le Wagon [taxi fare model API](https://taxifare.lewagon.ai/predict?pickup_datetime=2012-10-06%2012:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2)
# '''

# H2 title
'''## Taxicab Fare Predictor'''

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''

# Add user entry form
with st.form(key='params_for_api'):

    pickup_date = st.date_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
    pickup_time = st.time_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
    pickup_datetime = f'{pickup_date} {pickup_time}'
    pickup_longitude = st.number_input('pickup longitude', value=40.7614327)
    pickup_latitude = st.number_input('pickup latitude', value=-73.9798156)
    dropoff_longitude = st.number_input('dropoff longitude', value=40.6413111)
    dropoff_latitude = st.number_input('dropoff latitude', value=-73.7803331)
    passenger_count = st.number_input('passenger_count', min_value=1, max_value=8, step=1, value=1)

    st.form_submit_button('Make prediction')


# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''

# 2. Let's build a dictionary containing the parameters for our API...
# Define the user parameters data structure
params = dict(
    pickup_datetime=pickup_datetime,
    pickup_longitude=pickup_longitude,
    pickup_latitude=pickup_latitude,
    dropoff_longitude=dropoff_longitude,
    dropoff_latitude=dropoff_latitude,
    passenger_count=passenger_count)

# 3. Let's call our API using the `requests` package...
response = requests.get(url, params=params)

# 4. Let's retrieve the prediction from the **JSON** returned by the API...
prediction = response.json()

## Finally, we can display the prediction to the user
# '''
pred = prediction['fare']

st.header(f'Fare amount: ${round(pred, 2)}')