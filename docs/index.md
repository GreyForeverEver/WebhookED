## WebhookER: A Python Library for Discord Webhooks

### Introduction

WebhookER is a Python library designed to simplify the process of interacting with Discord webhooks. Whether you want to send messages or edit previously sent messages, this library provides an easy-to-use interface for working with Discord webhooks.

### Installation

To install WebhookER, you can use pip:

```bash
pip install WebhookER
```

### Quick Start

```python
from WebhookER import WebhookER, WebhookEMessage, WebhookEEmbed

# Initialize the WebhookER instance with your Discord webhook URL
webhook = WebhookER("your_discord_webhook_url_here")

# Create a message with an embed
embed = WebhookEEmbed(title="Hello, Discord!", description="This is an example message.")
message = WebhookEMessage(content="Greetings!", embeds=[embed])

# Send the message to Discord
sent_message = webhook.send(message)

# Edit the sent message
edited_message = webhook.edit(sent_message, WebhookEMessage(content="Updated Greetings!"))
```

### Classes

#### `WebhookER`

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
  # Create a message
  message = WebhookEMessage(content="Hello, Discord!")

  # Send the message
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
  # Edit the sent message
  edited_message = webhook.edit(sent_message, WebhookEMessage(content="Updated Greetings!"))

  print(f"Message edited with ID: {edited_message.id}")
  ```

#### `WebhookEMessage`

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
  # Get the dictionary representation of the message
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
  # Load attributes from a dictionary
  message.load_from_dict(data)
  ```

#### `WebhookEEmbed`

##### Initialization

```python
embed = WebhookEEmbed(title="Hello, Discord!", description="This is an example message.")
```

##### Methods

- `get_dict() -> dict`

  Returns a dictionary representation of the `WebhookEEmbed` instance.

  ```python
  data = embed.get_dict()
  ```

  Example:
  ```python
  # Get the dictionary representation of the embed
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
  # Load attributes from a dictionary
  embed.load_from_dict(data)
  ```

### Examples

#### Sending Multiple Messages

```python
# Create multiple messages with different content
messages = [
    WebhookEMessage(content="Message 1"),
    WebhookEMessage(content="Message 2"),
    WebhookEMessage(content="Message 3"),
]

# Send each message to Discord
for msg in messages:
    sent_message = webhook.send(msg)
    print(f"Message sent with ID: {sent_message.id}")
```

#### Editing Multiple Messages

```python
# Assume you have a list of message IDs to edit
message_ids = ["id1", "id2", "id3"]

# Create a new message to update the content
new_message = WebhookEMessage(content="Updated Message!")

# Edit each message with the new content
for msg_id in message_ids:
    edited_message = webhook.edit(msg_id, new_message)
    print(f"Message edited with ID: {edited_message.id}")
```

### Conclusion

WebhookER simplifies Discord webhook interactions in Python, making it easy to send and edit messages. If you encounter any issues or have suggestions for improvement, feel free to [open an issue](link_to_repository_issues).

Happy coding!