from sklearn.preprocessing import LabelEncoder
import pandas as pd
from flask import request
import requests

categorical_features = ['zipcode','property_type','room_type']
numeric_features = ['price', 'beds', 'bedrooms', 'bathrooms', 'accommodates','guests_included', 'instant_bookable', 'cleaning_fee']
bool_features = ['tv', 'wifi', 'kitchen', 'air conditioning', 'pool', 'hot tub', 'washer', 'dryer', 'refrigerator', 'iron', 'free parking on premises', 'dishes and silverware', 'microwave']


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
