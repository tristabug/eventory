from flask_pymongo import PyMongo
import logging

mongo = PyMongo()

def init_mongo(app):
    try:
        mongo.init_app(app)
        
        # validate connection
        with app.app_context():
            mongo.cx.admin.command('ping')
        logging.info("MongoDB connection established successfully.")
    except Exception as e:
        logging.error(f"MongoDB connection failed: {e}")
        raise ConnectionError("Failed to connect to MongoDB.")
