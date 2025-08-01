from datetime import datetime

def test_post_event_valid(client):
    response = client.post('/events', json={
        "event_type": "page_view",
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "user_id": "user123",
        "source_url": "https://example.com"
    })
    assert response.status_code == 201
    assert b"Event added successfully" in response.data

def test_post_event_missing_fields(client):
    response = client.post('/events', json={
        "event_type": "page_view",
        "user_id": "user123"
    })
    assert response.status_code == 400
    assert b"errors" in response.data

def test_post_event_empty_fields(client):
    response = client.post('/events', json={
        "event_type": "",
        "timestamp": "",
        "user_id": "",
        "source_url": ""
    })
    assert response.status_code == 400
    assert b"errors" in response.data

def test_post_event_null_fields(client):
    response = client.post('/events', json={
        "event_type": None,
        "timestamp": None,
        "user_id": None,
        "source_url": None
    })
    assert response.status_code == 400
    assert b"errors" in response.data

def test_post_event_invalid_url(client):
    response = client.post('/events', json={
        "event_type": "click",
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "user_id": "user123",
        "source_url": "not-a-url"
    })
    assert response.status_code == 400
    assert b"source_url" in response.data

def test_post_event_invalid_user_id(client):
    response = client.post('/events', json={
        "event_type": "click",
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "user_id": "invalid user!",
        "source_url": "https://example.com"
    })
    assert response.status_code == 400
    assert b"user_id" in response.data

def test_post_event_invalid_timestamp(client):
    response = client.post('/events', json={
        "event_type": "click",
        "timestamp": "not-a-date",
        "user_id": "user123",
        "source_url": "https://example.com"
    })
    assert response.status_code == 400
    assert b"timestamp" in response.data

def test_post_event_payload_too_large(client):
    large_string = "x" * (2 * 1024 * 1024 + 1)  # >2MB

    response = client.post('/events', json={
        "event_type": "page_view",
        "timestamp": "2025-07-23T20:00:00Z",
        "user_id": large_string,
        "source_url": "https://example.com"
    })

    assert response.status_code == 413 or response.status_code == 400
