# Create an Event
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
**Manual Testing**
- **CLI**: 
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
    
    **Example** if event type is page_view, timestamp is "2025-07-19T14:00:00", user is user1, and the source url is google: 
    ``` 
    curl -X POST http://127.0.0.1:5001/events \
        -H "Content-Type: application/json" \
        -d '{
            "event_type": "page_view",
            "timestamp": "2025-07-19T14:00:00",
            "user_id": "user1",
            "source_url": "https://www.google.com/"
        }'
    ```

- **BROWSER** /Dev Tools/Inspect/Console:    
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

    **Example** if event type is page_view, timestamp is "2025-07-19T14:00:00", user is user1, and the source url is google: 
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

## Success Response
**Condition**: If all params were provided and in the correct format.
- Code: ```201``` ```CREATED```
- Content: 
    ```json 
    { "message": "Event added successfully" } 
    ```

## Error Response
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

