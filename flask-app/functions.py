from sklearn.preprocessing import LabelEncoder
import pandas as pd
from flask import request
import requests

categorical_features = ['zipcode','neighbourhood','property_type','room_type']
numeric_features = ['price', 'beds', 'bedrooms', 'bathrooms','accommodates','guests_included','minimum_nights','instant_bookable']
bool_features =  ['Cable TV', 'Wifi', 'Kitchen', 'Air conditioning', 'Pool', 'Hot tub', 'grill', 'Washer', 'Dryer']

def pull_data():
    user_features = request.json('https://airbnb-bw.herokuapp.com/api/dsListings')
    return user_features

def transform_json(jsondata):
    data = pd.DataFrame.from_dict([jsondata])
    return data

def encode_data(df):
    label_encoder = LabelEncoder()
    for feature in categorical_features:
        df[feature] = label_encoder.fit_transform(df[feature])
    return df
