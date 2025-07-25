import json
from flask import Blueprint, request, jsonify, Response
from datetime import datetime
from bson import ObjectId
from query_utils import build_query, build_stats_pipeline
from models import validate_event
from db import mongo

# json encoder
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

events_bp = Blueprint('events', __name__)

# POST /events
@events_bp.route('/events', methods=['POST'])
def add_event():
    data = request.get_json()
    valid, errors = validate_event(data)
    
    if not valid:
        return jsonify({"errors": str(errors)}), 400
    else: # insert into mongodb
        mongo.db.events.insert_one(data)
        return jsonify({"message": "Event added successfully"}), 201

# GET /events
@events_bp.route('/events', methods=['GET'])
def get_events():
    try:
        query = build_query(request.args)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
    events = list(mongo.db.events.find(query))
    return Response(json.dumps(events, cls=JSONEncoder), mimetype='application/json'), 200

# GET /events/stats
@events_bp.route('/events/stats', methods=['GET'])
def get_event_stats():
    pipeline = build_stats_pipeline()
    stats = list(mongo.db.events.aggregate(pipeline))
    return Response(json.dumps(stats, cls=JSONEncoder), mimetype='application/json'), 200
