import pandas as pd
from flask import Flask, render_template, jsonify
import requests
from flask_sqlalchemy import SQLAlchemy
import pickle
from .functions import *
#from ML page import model

def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    # These comments are left until we're sure we're not using our own DB
    # app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('flask.html', title='Get some data!') #listings=Listing.query.all())


    @app.route('/predict', methods=['GET', 'POST'])
    def prediction():
        """Get user inputs POSTed to us and then predict with them them """
        user_features = pull_data()

        # Force = mimetype ignored, silent = returns None if fails
        print(user_features)
        #user_features = ['TBD']
        xgb_model = pickle.load(open('xgb_reg.pkl', 'rb'))

        sample = {'price': 122.0, 'beds': 3, 'bedrooms': 3, 'bathrooms': 2.0, 'zipcode': 90230,
                'neighbourhood': 'Culver City', 'property_type': 'Condominium', 'room_type': 'Entire home/apt',
                'accommodates': 6, 'guests_included': 3, 'minimum_nights': 30, 'instant_bookable': 0 }
        data = transform_json(sample)
        df = encode_data(data)

        #prediction = xgb_model.predict(df)
        #print(prediction)
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
