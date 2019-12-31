from flask_sqlalchemy import SQLAlchemy

# Just in case we will be using our own DB

DB = SQLAlchemy()

class Listing(DB.Model):
	id = DB.Column(DB.BigInteger, primary_key=True)
    neighborhood = DB.Column(DB.String(20), nullable=False)
    zipcode = DB.Column(DB.String(20), nullable=False)
	bedrooms = DB.Column(DB.BigInteger, nullable=False)
	bathrooms = DB.Column(DB.BigInteger, nullable=False)

	def __repr__(self):
		return f'<Listing in {self.neighborhood}>'
