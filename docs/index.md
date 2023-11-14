## WebhookED: A Python Library for Discord Webhooks

WebhookED is a Python library designed to simplify the process of interacting with Discord webhooks. This library provides a convenient interface for sending and editing messages, as well as constructing embeds with fields for richer content.

### Installation

Install WebhookED using pip:

```bash
pip install git+https://github.com/GreyForeverEver/WebhookED.git
```

### Quick Start

```python
from WebhookED import WebhookER, WebhookEMessage, WebhookEEmbed, WebhookEField

# Initialize the WebhookER instance with your Discord webhook URL
webhook = WebhookER("your_discord_webhook_url_here")

# Create a message with an embed containing fields
field1 = WebhookEField(name="Field 1", value="Value 1", inline=True)
field2 = WebhookEField(name="Field 2", value="Value 2", inline=False)
embed = WebhookEEmbed(title="Hello, Discord!", fields=[field1, field2])
message = WebhookEMessage(content="Greetings!", embeds=[embed])

# Send the message to Discord
sent_message = webhook.send(message)

# Edit the sent message
edited_message = webhook.edit(sent_message, WebhookEMessage(content="Updated Greetings!"))
```

### Classes

#### `WebhookER`

The `WebhookER` class represents the main interface for interacting with Discord webhooks.

##### Initialization

```python
webhook = WebhookER("your_discord_webhook_url_here")
```

##### Methods

- `send(message: WebhookEMessage) -> WebhookEMessageSent`

  Sends a message to the Discord webhook.

  ```python
  sent_message = webhook.send(message)
  ```

  Example:
  ```python
  message = WebhookEMessage(content="Hello, Discord!")
  sent_message = webhook.send(message)
  print(f"Message sent with ID: {sent_message.id}")
  ```

- `edit(sent_message: WebhookEMessageSent or str, new_message: WebhookEMessage) -> WebhookEMessageSent`

  Edits a previously sent message on the Discord webhook.

  ```python
  edited_message = webhook.edit(sent_message, new_message)
  ```

  Example:
  ```python
  edited_message = webhook.edit(sent_message, WebhookEMessage(content="Updated Greetings!"))
  print(f"Message edited with ID: {edited_message.id}")
  ```

#### `WebhookEMessage`

The `WebhookEMessage` class represents a Discord message and can include content, a username, avatar URL, and embeds.

##### Initialization

```python
message = WebhookEMessage(content="Greetings!", embeds=[embed])
```

##### Methods

- `get_dict() -> dict`

  Returns a dictionary representation of the `WebhookEMessage` instance.

  ```python
  data = message.get_dict()
  ```

  Example:
  ```python
  data = message.get_dict()
  print(f"Message dictionary: {data}")
  ```

- `load_from_dict(dict: dict)`

  Populates the `WebhookEMessage` instance's attributes from a dictionary.

  ```python
  message.load_from_dict(data)
  ```

  Example:
  ```python
  message.load_from_dict(data)
  ```

#### `WebhookEEmbed`

The `WebhookEEmbed` class represents an embedded message within a Discord webhook. It can contain various attributes, including title, description, fields, and more.

##### Initialization

```python
embed = WebhookEEmbed(title="Hello, Discord!", fields=[field1, field2])
```

##### Methods

- `get_dict() -> dict`

  Returns a dictionary representation of the `WebhookEEmbed` instance.

  ```python
  data = embed.get_dict()
  ```

  Example:
  ```python
  data = embed.get_dict()
  print(f"Embed dictionary: {data}")
  ```

- `load_from_dict(dict: dict)`

  Populates the `WebhookEEmbed` instance's attributes from a dictionary.

  ```python
  embed.load_from_dict(data)
  ```

  Example:
  ```python
  embed.load_from_dict(data)
  ```

#### `WebhookEField`

The `WebhookEField` class represents a field within a Discord webhook embed. It allows you to include additional information in a structured manner, such as name, value, and whether the field should be displayed inline.

##### Initialization

```python
field = WebhookEField(name="Field Name", value="Field Value", inline=False)
```

##### Methods

- `get_dict() -> dict`

  Returns a dictionary representation of the `WebhookEField` instance.

  ```python
  data = field.get_dict()
  ```

  Example:
  ```python
  data = field.get_dict()
  print(f"Field dictionary: {data}")
  ```

### Examples

#### Sending Multiple Messages

```python
messages = [
    WebhookEMessage(content="Message 1"),
    WebhookEMessage(content="Message 2"),
    WebhookEMessage(content="Message 3"),
]

for msg in messages:
    sent_message = webhook.send(msg)
    print(f"Message sent with ID: {sent_message.id}")
```

#### Editing Multiple Messages

```python
message_ids = ["id1", "id2", "id3"]
new_message = WebhookEMessage(content="Updated Message!")

for msg_id in message_ids:
    edited_message = webhook.edit(msg_id, new_message)
    print(f"Message edited with ID: {edited_message.id}")
```

#### Using `WebhookEField` in an Embed

```python
field1 = WebhookEField(name="Field 1", value="Value 1", inline=True)
field2 = WebhookEField(name="Field 2", value="Value 2", inline=False)
embed_with_fields = WebhookEEmbed(title="Embed with Fields", fields=[field1, field2])
message_with_embed = WebhookEMessage(content="Check out this embed!", embeds=[embed_with_fields])
sent_message = webhook.send(message_with_embed)
```

#### Populating `WebhookEField` from a Dictionary

```python
field_data = {"name": "Dynamic Field", "value": "Dynamic Value", "inline": True}
dynamic_field = WebhookEField()
dynamic_field.load_from_dict(field_data)
field_dict = dynamic_field.get_dict()
print(f"Dynamic Field dictionary: {field_dict}")
```

### Conclusion

WebhookER simplifies Discord webhook interactions in Python, making it easy to send and edit messages and create rich content with embeds and fields. If you encounter any issues or have suggestions for improvement, feel free to [open an issue](https://github.com/GreyForeverEver/WebhookED/issues).

Happy coding!

Summary here -> [list](https://greyforeverever.github.io/WebhookED/list)
