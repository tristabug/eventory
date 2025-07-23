
import re
from datetime import datetime
from urllib.parse import urlparse

def validate_event(data):
    required_fields = ['event_type', 'timestamp', 'user_id', 'source_url']

    # check for missing or empty fields
    for field in required_fields:
        if field not in data:
            return False, f"Missing field: {field}"
        
        if data[field] is None or (isinstance(data[field], str) and not data[field].strip()):
            return False, f"Empty field: {field}"

    # validate event_type
    if not isinstance(data['event_type'], str) or not data['event_type'].strip():
            return False, "Invalid event_type: must be a non-empty string"

    # validate timestamp format
    try:
        datetime.fromisoformat(data['timestamp'])
    except ValueError:
        return False, "Invalid timestamp format: must be ISO 8601"

    # validate user_id
    if not isinstance(data['user_id'], str) or not re.match(r'^[a-zA-Z0-9_-]+$', data['user_id']):
        return False, "Invalid user_id: must be alphanumeric with optional underscores or hyphens"

    # validate source_url
    parsed_url = urlparse(data['source_url'])
    if not all([parsed_url.scheme, parsed_url.netloc]):
        return False, "Invalid source_url: must be a valid URL"

    return True, "Valid"
