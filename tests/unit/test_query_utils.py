from datetime import datetime, timedelta
import pytest
from query_utils import build_query, build_stats_pipeline

# query_utils.py
def test_build_query_valid_type_only():
    args = {"type": "click"}
    expected = {"event_type": "click"}

    assert build_query(args) == expected

def test_build_query_invalid_type_raises():
    args = {"type": "invalid_type"}
    with pytest.raises(ValueError, match="Invalid event type: invalid_type"):
        build_query(args)

def test_build_query_valid_date_range_only():
    args = {"start": "2025-01-01T00:00:00", "end": "2025-01-02T00:00:00"}
    result = build_query(args)
    assert "timestamp" in result
    assert result["timestamp"]["$gte"] == datetime.fromisoformat("2025-01-01T00:00:00")
    assert result["timestamp"]["$lte"] == datetime.fromisoformat("2025-01-02T00:00:00")

def test_build_query_start_after_end_raises():
    args = {"start": "2025-01-03T00:00:00", "end": "2025-01-01T00:00:00"}
    with pytest.raises(ValueError, match="Start date cannot be after end date"):
        build_query(args)

def test_build_query_invalid_date_format_raises():
    args = {"start": "not-a-date"}
    with pytest.raises(ValueError, match="Invalid date range:"):
        build_query(args)

def test_build_query_type_and_date_combined():
    args = {
        "type": "page_view",
        "start": "2025-01-01T00:00:00",
        "end": "2025-01-02T00:00:00"
    }
    result = build_query(args)
    assert result["event_type"] == "page_view"
    assert result["timestamp"]["$gte"] == datetime.fromisoformat("2025-01-01T00:00:00")
    assert result["timestamp"]["$lte"] == datetime.fromisoformat("2025-01-02T00:00:00")

def test_build_stats_pipeline_structure():
    pipeline = build_stats_pipeline()
    assert isinstance(pipeline, list)
    assert pipeline[0] == {"$group": {"_id": "$event_type", "count": {"$sum": 1}}}
    assert pipeline[1] == {"$sort": {"count": -1}}
