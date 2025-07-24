import pytest
from app import create_app
from db import mongo

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['MONGO_URI'] = "mongodb://mongo:27017/test_eventsdb"
    mongo.init_app(app)
    
    with app.app_context():
        mongo.db.events.delete_many({})  # Clear test data

    with app.test_client() as client:
        yield client

    with app.app_context():
        mongo.db.events.delete_many({})
