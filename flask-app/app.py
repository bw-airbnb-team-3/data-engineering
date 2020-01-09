import pandas as pd
from flask import Flask, request, render_template, jsonify
import requests
from flask_sqlalchemy import SQLAlchemy
import pickle
from .functions import *
#from ML page import model

def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template('flask.html', title='Get some data!') #listings=Listing.query.all())

    @app.route('/api/dsListings', methods=['GET'])
    def api():
        #user_features=request.json['key']
        #loop over each feature
        user_features = request.get_json()
        return user_features

    @app.route('/predict', methods=['GET', 'POST'])
    def prediction():
        """Get user inputs POSTed to us and then predict with them them """
        #user_features = pull_data()

        # Force = mimetype ignored, silent = returns None if fails
        #print(user_features)

        xgb_model = pickle.load(open('xgb_reg.pkl', 'rb'))

        sample = {'beds': 1, 'bedrooms': 1.0, 'bathrooms': 1.0, 'accommodates': 2, 'guests_included': 1,
                 'minimum_nights': 30, 'instant_bookable': 0, 'zipcode': 90706, 'neighbourhood': 'Bellflower',
                  'property_type': 'Apartment', 'room_type': 'Entire home/apt'
                  }
        data = transform_json(sample)
        df = encode_data(data)

        prediction = xgb_model.predict(df)
        print(prediction)
        #results = None
        return  'Hi'


    @app.route('/data', methods=['POST']) #Getting data posted to us
    @app.route('/data/getdata', methods=['GET']) #Serving Data
    def data():
        test_dict = {'ideal_price': 99.99, 'nearby_listings':
                                            {'neighborhood_a': 'address1',
                                             'neighborhood_b': 'address2',
                                              'neighborhood_c': 'address3'}
                                            }
        return jsonify(test_dict)



    return app
