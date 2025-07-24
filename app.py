from flask import Flask, jsonify
from db import init_mongo
from routes import events_bp

def create_app():
    app = Flask(__name__)

    # mongodb config
    app.config["MONGO_URI"] = "mongodb://mongo:27017/eventsdb"

    # limit request payload to 2MB
    app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024

    # monogo and routes
    init_mongo(app)         
    app.register_blueprint(events_bp)

    # handle large payloads
    @app.errorhandler(413)
    def request_entity_too_large(error):
        return jsonify({"error": "Payload too large"}), 413

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
