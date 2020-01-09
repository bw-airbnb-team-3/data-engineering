from flask import Flask, jsonify, render_template
from .functions import *
import pandas as pd
import pickle
import requests



def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template('flask.html', title='Get some data!')

    @app.route('/predict', methods=['GET', 'POST'])
    def prediction():
        """GETS user input then predicts with it """

        user_features = requests.get('https://airbnb-bw.herokuapp.com/api/dsListings')
        # This returns a dict from the front-end
        user_features = user_features.text.strip('[]')
        print(user_features)

        xgb_model = pickle.load(open('xgb_reg.pkl', 'rb'))

        sample = {'beds': 1, 'bedrooms': 1.0, 'bathrooms': 1.0, 'accommodates': 2, 'guests_included': 1,
                 'minimum_nights': 2, 'instant_bookable': 0, 'zipcode': 90706, 'neighbourhood': 'Bellflower',
                  'property_type': 'Apartment', 'room_type': 'Entire home/apt'
                  }
        # Change this to user features once we are sure what we're getting #################################################
        data = transform_json(sample)
        df = encode_data(data)

        prediction = xgb_model.predict(df)
        predict_dict = {}
        predict_dict['Optimal Price'] = round(float(prediction[0]), 2)
        #results = None
        return jsonify(predict_dict)


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
