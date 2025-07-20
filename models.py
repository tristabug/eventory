# Validate new events
def validate_event(data):
    required_fields = ['event_type', 'timestamp', 'user_id', 'source_url']
    for field in required_fields:
        if field not in data:
            return False, f"Missing field: {field}"
    try:
        from datetime import datetime
        datetime.fromisoformat(data['timestamp'])
    except ValueError:
        return False, "Invalid timestamp format"
    return True, "Valid"