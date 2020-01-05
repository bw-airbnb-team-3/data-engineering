import pandas as pd
from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
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

    @app.route('/data', methods=['POST'])
    @app.route('/data/getdata', methods=['GET'])
    def data():
        test_dict = {'ideal_price': 99.99, 'nearby_listings':
                                            {'neighborhood_a': 'address1',
                                             'neighborhood_b': 'address2',
                                              'neighborhood_c': 'address3'}
                                            }
        return jsonify(test_dict)


    @app.route('/predict', methods=['GET', 'POST'])
    def prediction():
        """GET user inputs and then POST them """
        user_features = request.get_json(force=True, silent=True) # Force = mimetype ignored, silent = returns None if fails
        features = ['TBD']
        # Get pickle data - xgbpipe = pickle.load(open('xgbpipe.pkl', 'rb'))
        df = pd.read_csv('tbd')
        # Run prediction from pickle data ?
        # Import function from whatever py file we end up making and call it here
        # Store results
        results = None
        return jsonify(results)

    return app
