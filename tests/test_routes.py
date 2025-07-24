
from datetime import datetime, timedelta

# POST event tests
def test_post_event(client):
    response = client.post('/events', json={
        "event_type": "page_view",
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": "test_user",
        "source_url": "https://example.com"
    })
    
    assert response.status_code == 201
    assert b"Event added successfully" in response.data

def test_post_event_missing_fields(client):
    response = client.post('/events', json={
        "event_type": "page_view",
        "user_id": "test_user"
    })
    
    assert response.status_code == 400

def test_post_event_empty_fields(client):
    response = client.post('/events', json={
        "event_type": "",
        "timestamp": "",
        "user_id": "",
        "source_url": ""
    })
    
    assert response.status_code == 400
    assert b"Empty field" in response.data

def test_post_event_null_fields(client):
    response = client.post('/events', json={
        "event_type": None,
        "timestamp": None,
        "user_id": None,
        "source_url": None
    })
    
    assert response.status_code == 400
    assert b"Empty field" in response.data

def test_post_event_invalid_url(client):
    response = client.post('/events', json={
        "event_type": "click",
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": "user123",
        "source_url": "not-a-url"
    })
    
    assert response.status_code == 400
    assert b"Invalid source_url" in response.data

# GET event tests
def test_get_events(client):
    response = client.get('/events')
    
    assert response.status_code == 200

def test_get_events_with_filters(client):
    now = datetime.utcnow()
    start = (now - timedelta(days=1)).isoformat()
    end = (now + timedelta(days=1)).isoformat()
    response = client.get(f'/events?type=page_view&start={start}&end={end}')
    
    assert response.status_code == 200

def test_get_event_stats(client):
    response = client.get('/events/stats')

    assert response.status_code == 200

def test_post_event_invalid_user_id(client):
    response = client.post('/events', json={
        "event_type": "click",
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": "invalid user!",
        "source_url": "https://example.com"
    })

    assert response.status_code == 400
    assert b"Invalid user_id" in response.data

# Test timestamp, start date, end date
def test_post_event_invalid_timestamp(client):
    response = client.post('/events', json={
        "event_type": "click",
        "timestamp": "not-a-date",
        "user_id": "user123",
        "source_url": "https://example.com"
    })
    
    assert response.status_code == 400
    assert b"Invalid timestamp format" in response.data
    
def test_get_events_start_after_end(client):
    start = (datetime.utcnow() + timedelta(days=1)).isoformat()
    end = datetime.utcnow().isoformat()
    response = client.get(f'/events?start={start}&end={end}')

    assert response.status_code == 400
    assert b"Start date cannot be after end date" in response.data

def test_get_events_invalid_start_date(client):
    response = client.get('/events?start=not-a-date')

    assert response.status_code == 400
    assert b"Invalid date range" in response.data

def test_get_events_invalid_end_date(client):
    response = client.get('/events?end=2025-13-01T00:00:00')

    assert response.status_code == 400
    assert b"Invalid date range" in response.data

def test_get_events_only_start_date(client):
    start = (datetime.utcnow() - timedelta(days=1)).isoformat()
    response = client.get(f'/events?start={start}')

    assert response.status_code == 200

def test_get_events_only_end_date(client):
    end = (datetime.utcnow() + timedelta(days=1)).isoformat()
    response = client.get(f'/events?end={end}')

    assert response.status_code == 200

def test_get_events_same_start_end(client):
    now = datetime.utcnow().replace(microsecond=0).isoformat()
    response = client.get(f'/events?start={now}&end={now}')

    assert response.status_code == 200

