from flask import Blueprint, request, jsonify
from datetime import datetime
from bson.json_util import dumps
from query_utils import build_query, build_stats_pipeline
from models import validate_event
from db import mongo

events_bp = Blueprint('events', __name__)

# POST /events
@events_bp.route('/events', methods=['POST'])
def add_event():
    data = request.get_json()
    valid, message = validate_event(data)
    if not valid:
        return jsonify({"error": message}), 400
    data['timestamp'] = datetime.fromisoformat(data['timestamp'])
    mongo.db.events.insert_one(data)
    return jsonify({"message": "Event added successfully"}), 201

# GET /events
@events_bp.route('/events', methods=['GET'])
def get_events():
    query = build_query(request.args)
    events = mongo.db.events.find(query)
    return dumps(events), 200

# GET /events/stats
@events_bp.route('/events/stats', methods=['GET'])
def get_event_stats():
    pipeline = build_stats_pipeline()
    stats = list(mongo.db.events.aggregate(pipeline))
    return dumps(stats), 200