# Show Events
URL: /events/
Method: GET
Auth Required: No

## Show ALL Events
### Manual Testing
CLI: curl http://127.0.0.1:5001/events
BROWSER: http://127.0.0.1:5001/events

## Show Filtered Events 
Events can be filtered by event type and timerange.

### Manual Testing
#### Filter by Event Type
Params: Replace <event_type> with the type of event enclosed in double quotes.

CLI: curl "http://127.0.0.1:5001/events?type=<event_type>"
    - EX (event_type = page_view): curl "http://127.0.0.1:5001/events?type=page_view"
BROWSER: http://127.0.0.1:5001/events?type=<event_type>
    - EX (event_type = page_view): http://127.0.0.1:5001/events?type=page_view

#### Filter by a Timerange
Params: Replace <YYYY-MM-DDThh:mm:ss> with the date (YYYY-MM-DD) and ISO 8601 time (hh:mm:ss).

CLI: curl "http://127.0.0.1:5001/events?start=<YYYY-MM-DDThh:mm:ss>&end=<YYYY-MM-DDThh:mm:ss>"
    - EX (start = 7/1/2025 @ 12AM, end = 7/31/2025 @ 11:59pm): curl "http://127.0.0.1:5001/events?start=2025-07-01T00:00:00&end=2025-07-31T23:59:59"

BROWSER: http://127.0.0.1:5001/events?start=<YYYY-MM-DDThh:mm:ss>&end=<YYYY-MM-DDThh:mm:ss>
    - EX (start = 7/1/2025 @ 12AM, end = 7/31/2025 @ 11:59pm): http://127.0.0.1:5001/events?start=2025-07-01T00:00:00&end=2025-07-31T23:59:59

## Show Filtered Events 
Show all web events by type with their count.

CLI: curl http://127.0.0.1:5001/events/stats
BROWSER: http://127.0.0.1:5001/events/stats

## Success Response
Condition: User can't see any events, because no events exist.
Code: 200 OK
Content: {[]}

Condition: User can see events.
Code: 200 OK
Content: {[]}