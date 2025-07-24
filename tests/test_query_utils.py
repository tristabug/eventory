
from datetime import datetime, timedelta

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
