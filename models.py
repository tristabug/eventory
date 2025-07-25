from datetime import datetime
from cerberus import Validator

event_schema = {
    "event_type": {"type": "string", "required": True, "allowed": ["page_view", "click"]}, 
    "timestamp": {"type": "datetime", "required": True},
    "user_id": {"type": "string", "required": True, "regex": r"^user\d+$"}, # ex: user1, user123
    "source_url":  {"type": "string", "required": True, "regex": r"^(https?|ftp)://[^\s/$.?#].[^\s]*$"}
}

# validates new events (POST)
validator = Validator(event_schema)

def validate_event(data):
    iso_errors = None

    try:
        data['timestamp'] = datetime.strptime(data['timestamp'], "%Y-%m-%dT%H:%M:%SZ")
    except Exception as e:
        iso_errors = str(e)

    is_valid = validator.validate(data)
    errors = validator.errors

    if not is_valid or iso_errors:
        return False, {"schema_errors": errors, "timestamp_error": iso_errors}
    return True, None
