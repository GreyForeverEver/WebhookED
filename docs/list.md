# WebhookED Documentation

## Introduction

The `WebhookER` class provides a simple interface for interacting with Discord webhooks, allowing you to send and edit messages.

## Classes

### 1. WebhookER

#### Constructor
```python
WebhookER(url: str)
```
- Initializes a `WebhookER` instance with the Discord webhook URL.

#### Methods

##### 1. `send(message: WebhookEMessage) -> WebhookEMessageSent`
- Sends a message to the Discord webhook.
    - Parameters:
        - `message`: An instance of `WebhookEMessage` representing the message to be sent.
    - Returns:
        - An instance of `WebhookEMessageSent` representing the sent message with its ID.
    - Raises:
        - `WebhookEError`: If there is an issue with the request.

##### 2. `edit(sent_message: WebhookEMessageSent or str, new_message: WebhookEMessage) -> WebhookEMessageSent`
- Edits a previously sent message on the Discord webhook.
    - Parameters:
        - `sent_message`: An instance of `WebhookEMessageSent` or the ID of the message to be edited.
        - `new_message`: An instance of `WebhookEMessage` representing the updated message.
    - Returns:
        - An instance of `WebhookEMessageSent` representing the edited message with its updated ID.
    - Raises:
        - `WebhookEError`: If there is an issue with the request.

### 2. WebhookEMessage

#### Constructor
```python
WebhookEMessage(content: str = None, username: str = None, avatar_url: str = None, tts: bool = None, embeds: List[WebhookEEmbed] or WebhookEEmbed = [])
```
- Initializes a `WebhookEMessage` instance with optional parameters.

#### Methods

##### 1. `get_dict() -> dict`
- Returns a dictionary representation of the `WebhookEMessage` instance.

##### 2. `load_from_dict(dict: dict) -> None`
- Populates the `WebhookEMessage` instance's attributes from a dictionary.

### 3. WebhookEMessageSent (Inherits from WebhookEMessage)

#### Constructor
```python
WebhookEMessageSent(id: str, *args, **kwargs)
```
- Initializes a `WebhookEMessageSent` instance with the ID of the sent message.

#### Methods

##### 1. `get_dict() -> dict`
- Returns a dictionary representation of the `WebhookEMessageSent` instance.

### 4. WebhookEEmbed

#### Constructor
```python
WebhookEEmbed(title=None, e_type=None, description=None, url=None, timestamp=None, color=None, footer=None, image=None, thumbnail=None, video=None, provider=None, author=None, fields: List[WebhookEField] or WebhookEField = [])
```
- Initializes a `WebhookEEmbed` instance with optional parameters.

#### Methods

##### 1. `get_dict() -> dict`
- Returns a dictionary representation of the `WebhookEEmbed` instance.

##### 2. `load_from_dict(dict: dict) -> None`
- Populates the `WebhookEEmbed` instance's attributes from a dictionary.

### 5. WebhookEField

#### Constructor
```python
WebhookEField(name: str, value: str, inline: bool = False)
```
- Initializes a `WebhookEField` instance with the provided parameters.

#### Methods

##### 1. `get_dict() -> dict`
- Returns a dictionary representation of the `WebhookEField` instance.

## Conclusion

The `WebhookER` class and its associated classes provide a convenient way to interact with Discord webhooks, allowing you to send and edit messages with ease.
