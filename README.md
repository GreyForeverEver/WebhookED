
---

# WebhookED: Discord Webhook Library

WebhookED is a Python library designed to simplify interactions with Discord webhooks. It allows you to send and edit messages, handle errors, and incorporate rich content seamlessly. Below are explanations on how to use its main features.

## Features

### 1. WebhookEEmbed

`WebhookEEmbed` is a class that represents an embedded message. You can create an instance of this class and use the `get_dict` method to obtain the dictionary representation.

```python
embed = WebhookEEmbed(title="My Title", description="Hello, World!", color=0xFF5733)
dict_data = embed.get_dict()
```

### 2. WebhookEMessage

`WebhookEMessage` is a class for creating messages. You can include content, a username, an avatar URL, and embeds. Use the `get_dict` method to get the dictionary representation.

```python
message = WebhookEMessage(content="Hello, World!", username="MyBot", avatar_url="http://example.com/avatar.jpg", embeds=[embed])
dict_data = message.get_dict()
```

### 3. WebhookER

`WebhookER` is the main class for interacting with Discord webhooks. Initialize it with the webhook URL.

```python
webhook = WebhookER(url="https://discord.com/api/webhooks/your_webhook_id/your_webhook_token")
```

#### Sending Messages

Use the `send` method to send a message.

```python
sent_message = webhook.send(message)
```

#### Editing Messages

To edit a previously sent message, use the `edit` method.

```python
edited_message = webhook.edit(sent_message, new_message)
```

### Error Handling

The library includes `WebhookEError` to handle specific errors. For example, when trying to send an empty message.

```python
try:
    response = webhook.send(empty_message)
except WebhookEError as e:
    print(f"Error: {e}")
```

## Getting Started

1. Clone the repository: `git clone https://github.com/GreyForeverEver/WebhookER.git`
2. Import the library into your project.
3. Follow the usage examples above.

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests to enhance the library.

---
