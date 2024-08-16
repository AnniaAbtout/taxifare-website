import streamlit as st

# '''
# # TaxiFareModel front
# '''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

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

# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

# url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''
st.write("Hello, here you can get an approximation for your taxi ride fare !")

url = 'https://taxifare.lewagon.ai/predict'

import datetime

#set the ride date
d = st.date_input(
    "Date",
    datetime.date(2019, 7, 6))

#set the ride time
t = st.time_input('Ride start time', datetime.time(8, 45))

#set the position of the start and drop off
pickup_lon = st.number_input('Pickup Longitude')
pickup_lat = st.number_input('Pickup Latitude')
dropoff_lon = st.number_input('Drop off Longitude')
dropoff_lat = st.number_input('Drop off Latitude')

#set passenger count
pass_count = st.number_input('Passenger count')

#endpoints dict
endpt_dict = {
    "pickup_datetime" : f"{str(d)} {t}",
    "pickup_longitude" : pickup_lon,
    "pickup_latitude" : pickup_lat,
    "dropoff_longitude" : dropoff_lon,
    "dropoff_latitude" : dropoff_lat,
    "passenger_count" : int(pass_count)
}

import requests

if st.button('predict'):

    #endpt_dict

    prediction = requests.get(url=url, params={
    "pickup_datetime" : f"{str(d)} {t}",
    "pickup_longitude" : pickup_lon,
    "pickup_latitude" : pickup_lat,
    "dropoff_longitude" : dropoff_lon,
    "dropoff_latitude" : dropoff_lat,
    "passenger_count" : int(pass_count)
}).json()

    st.write("the fare is", prediction["fare"])
    #st.json(prediction["fare"])
    #st.json(endpt_dict)
