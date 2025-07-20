from flask import Flask
from extensions import mongo
from routes import events_bp

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://mongo:27017/eventsdb"
    mongo.init_app(app)
    app.register_blueprint(events_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)