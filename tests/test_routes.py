
from datetime import datetime, timedelta

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
