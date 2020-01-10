from decouple import config
from flask import Flask, jsonify, redirect, render_template, session, url_for
from .functions import *
import pandas as pd
import pickle
import requests



def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config('FLASK_KEY')

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

        sample = {'beds': 2, 'bedrooms': 2.0, 'bathrooms': 1.0, 'accommodates': 2, 'guests_included': 1,
                'instant_bookable': 0, 'cleaning_fee': 70.0, 'zipcode': 90706, 'property_type': 'Apartment', 'room_type': 'Entire home/apt',
                'tv': True, 'wifi': True, 'kitchen': True, 'air_conditioning': True, 'pool': True,
                'hot_tub': True, 'washer': True, 'dryer': False, 'refrigerator': True, 'iron' :True, 'free_parking' :True,
                'dishes_and_silverware': False, 'microwave': True
                  }
        # Transforms the json received from users
        data = transform_json(sample)
        df = encode_data(data)

        prediction = xgb_model.predict(df)
        predict_dict = {}
        predict_dict['Optimal Price'] = round(float(prediction[0]), 2)

        # Stores predict_dict in the session, so it can be gotten from /data
        # session['price'] = predict_dict

        return jsonify(preict_dict)


    @app.route('/data', methods=['POST']) #Getting data posted to us
    @app.route('/data/getdata', methods=['GET']) #Serving Data
    def data():
        price = session.get('price')

        return jsonify(price)



    return app
