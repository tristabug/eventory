# POST 
*create an event*

- URL: ``` /events/ ```
- Method: ``` POST ```
- Auth Required: no

Data Constraints *(all fields are required)*
```json
{
    "event_type": "[string]",
    "timestamp": "[timestamp in ISO 8601 format]",
    "user_id": "[string]",
    "source_url": "[string]"
}
```

### Templates
curl
```
curl -X POST http://127.0.0.1:5001/events \
    -H "Content-Type: application/json" \
    -d '{
        "event_type": "<event_type>",
        "timestamp": "<YYYY-MM-DDThh:mm:ss>",
        "user_id": "<user_id>",
        "source_url": "<source_url>"
    }'
```

browser: /Dev Tools/Inspect/Console
```javascript
fetch("http://127.0.0.1:5001/events", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        "event_type": "<event_type>",
        "timestamp": "<YYYY-MM-DDThh:mm:ss>",
        "user_id": "<user_id>",
        "source_url": "<source_url>"
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error("Error:", error));
```

## Examples
**Trigger**: user1 viewed the page https://google.com/ on 7/19/2025 at 2pm.
curl
```
curl -X POST http://127.0.0.1:5001/events \
    -H "Content-Type: application/json" \
    -d '{
        "event_type": "page_view",
        "timestamp": "2025-07-19T14:00:00",
        "user_id": "user1",
        "source_url": "https://google.com/"
    }'
``` 

browser
```javascript
fetch("http://127.0.0.1:5001/events", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        "event_type": "page_view",
        "timestamp": "2025-07-19T14:00:00",
        "user_id": "user1",
        "source_url": "https://www.google.com/"
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error("Error:", error));
```

**Trigger**: user2 clicked on page https://yahoo.com/ on 7/20/2025 at 4pm.
curl
```
curl -X POST http://127.0.0.1:5001/events \
    -H "Content-Type: application/json" \
    -d '{
        "event_type": "click",
        "timestamp": "2025-07-20T16:00:00",
        "user_id": "user2",
        "source_url": "https://yahoo.com/"
    }'
``` 

browser
```javascript
fetch("http://127.0.0.1:5001/events", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        "event_type": "click",
        "timestamp": "2025-07-20T16:00:00",
        "user_id": "user2",
        "source_url": "https://yahoo.com/"
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error("Error:", error));
```

# Success Responses
**Condition**: If all params were provided and in the correct format.
- Code: ```201``` ```CREATED```
- Content: 
    ```json 
    { "message": "Event added successfully" } 
    ```

# Error Responses
**Condition**: If there's a missing parameter.
- Code: ```400``` ```BAD REQUEST```
- Content: 
    ```json 
    { "error": "Missing field: {field}" } 
    ```

**Condition**: If the timestamp isn't in ISO 8601 format.
- Code: ```400``` ```BAD REQUEST```
- Content: 
    ```json 
    { "error": "Invalid timestamp format" } 
    ```

