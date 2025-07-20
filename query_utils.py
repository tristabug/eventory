from datetime import datetime

def build_query(args):
    query = {}
    if 'type' in args:
        query['event_type'] = args['type']
    if 'start' in args or 'end' in args:
        query['timestamp'] = {}
        if 'start' in args:
            query['timestamp']['$gte'] = datetime.fromisoformat(args['start'])
        if 'end' in args:
            query['timestamp']['$lte'] = datetime.fromisoformat(args['end'])
    return query

def build_stats_pipeline():
    return [
        {"$group": {"_id": "$event_type", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]