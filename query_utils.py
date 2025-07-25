from datetime import datetime

# GET Query Validation
def build_query(args):
    query = {}
    
    allowed_types = {"page_view", "click"}

    # event type - validate and filter
    if 'type' in args:
        event_type = args.get("type")

        if event_type not in allowed_types:
            raise ValueError(f"Invalid event type: {event_type}")
        
        query['event_type'] = args['type']

    # date range - validate and filter
    start = args.get('start')
    end = args.get('end')
    timestamp_filter = {}

    try:
        if start:
            start_dt = datetime.fromisoformat(start)
            timestamp_filter['$gte'] = start_dt
        if end:
            end_dt = datetime.fromisoformat(end)
            timestamp_filter['$lte'] = end_dt

        # check if start > end
        if start and end and start_dt > end_dt:
            raise ValueError("Start date cannot be after end date")

        if timestamp_filter:
            query['timestamp'] = timestamp_filter

    except ValueError as e:
        raise ValueError(f"Invalid date range: {e}")

    return query

def build_stats_pipeline():
    return [
        {"$group": {"_id": "$event_type", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
