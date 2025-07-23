# GET
*get events*

- URL: ``` /events ```
- Method: ``` GET ```
- Auth Required: no

### Query Templates
**Events by event type** ( <event_type> )
- curl: ``` curl "http://127.0.0.1:5001/events?type=<event_type>" ```
- url: ``` http://127.0.0.1:5001/events?type=<event_type> ```

**Events within a date range** ( <YYYY-MM-DDThh:mm:ss> )
*Note: dates must be in ISO 8601 date and time*

- curl: ``` curl "http://127.0.0.1:5001/events?start=<YYYY-MM-DDThh:mm:ss>&end=<YYYY-MM-DDThh:mm:ss>" ```
- url: ``` http://127.0.0.1:5001/events?start=<YYYY-MM-DDThh:mm:ss>&end=<YYYY-MM-DDThh:mm:ss> ```

## Examples
**To Get**: all events.
curl
```
curl http://127.0.0.1:5001/events
``` 

url: ``` http://127.0.0.1:5001/events ```

**To Get**: all 'page view' event types.
curl
```
curl "http://127.0.0.1:5001/events?type=page_view"
``` 

url: ``` http://127.0.0.1:5001/events?type=page_view ```

**To Get**: all 'click' event types.
curl
```
curl "http://127.0.0.1:5001/events?type=click"
``` 

url: ``` http://127.0.0.1:5001/events?type=click ```

**To Get**: all events within a date range (7/1/2025 @12:00:00 am - 7/31/2025 @11:59:59 pm).
```
curl "http://127.0.0.1:5001/events?start=2025-07-01T00:00:00&end=2025-07-31T23:59:59"
``` 

url: ``` http://127.0.0.1:5001/events?start=2025-07-01T00:00:00&end=2025-07-31T23:59:59 ```

## Aggregations 
*get summarized views of data*

**Aggregation**: get event counts by event type.
curl
```
curl http://127.0.0.1:5001/events/stats
``` 

url: ``` http://127.0.0.1:5001/events/stats ``` 

# Success Responses
**Condition**: User can't see any events, because no events exist.
- Code: ```200``` ```OK```
- Content:
    ```json 
    {[]} 
    ```

**Condition**: User can see events.
- Code: ```200``` ```OK```
- Content: 
    ```json 
    {[]} 
    ```