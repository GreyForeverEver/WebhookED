
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

But wait, there's more! Enhance your embedded messages with fields using the `WebhookEField` class. Fields allow you to display information in a structured and organized way. Here's how you can level up your embedding game:

```python
# Create a WebhookEField instance
field = WebhookEField(name="Field Name", value="Field Value", inline=True)

# Include the field in your WebhookEEmbed instance
embed_with_field = WebhookEEmbed(title="My Title", fields=[field], color=0xFF5733)

# Obtain the updated dictionary representation
dict_data_with_field = embed_with_field.get_dict()
```

### 2. WebhookEMessage

`WebhookEMessage` is a class for creating messages. You can include content, a username, an avatar URL, and embeds. Use the `get_dict` method to get the dictionary representation.

```python
message = WebhookEMessage(content="Hello, World!", username="MyBot", avatar_url="http://example.com/avatar.jpg", embeds=[embed])
dict_data = message.get_dict()
```

### 3. Load from Dict

Both `WebhookEEmbed` and `WebhookEMessage` classes include a method named `load_from_dict`. This method is designed to populate the instance's attributes based on the information provided in a dictionary.

#### 3.1. WebhookEEmbed

`load_from_dict` in the `WebhookEEmbed` class allows you to initialize an instance using a dictionary. This is particularly useful when you have the data in a serialized format, and you want to recreate the object.

Example:

```python
# Assuming dict_data is a dictionary with the necessary attributes
embed = WebhookEEmbed()
embed.load_from_dict(dict_data)
```

#### 3.2. WebhookEMessage

Similarly, `load_from_dict` in the `WebhookEMessage` class populates the instance's attributes based on the provided dictionary. This method is handy when you want to reconstruct a message object from saved data.

Example:

```python
# Assuming dict_data is a dictionary with the necessary attributes
message = WebhookEMessage()
message.load_from_dict(dict_data)
```

By using `load_from_dict`, you can easily recreate instances of `WebhookEEmbed` and `WebhookEMessage` from serialized data, providing flexibility and convenience in your application.

---

### 4. WebhookER

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

1. Clone the repository: `git clone https://github.com/GreyForeverEver/WebhookED.git`
2. Import the library into your project.
3. Follow the usage examples above.

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests to enhance the library.

---
