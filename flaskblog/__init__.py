from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

application = Flask(__name__)
application.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234567aA@twitterelection.c3kxgaaw4op6.us-east-1.rds.amazonaws.com:3306/election_sentiment_analysis'
db = SQLAlchemy(application)

# Imported here to avoid circular import error
from flaskblog import routes
