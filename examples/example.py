from webhooked import WebhookEEmbed, WebhookEMessage, WebhookER

# Replace the URL below with your Discord webhook URL
webhook_url = "<webhook_url>"

# Create an embedded message
embed = WebhookEEmbed(
    title="Example Title",
    description="This is an example embedded message.",
    color=0x3498db  # Replace with your desired color code
)

# Create a message with the embedded content
message = WebhookEMessage(
    content="Hello, World!",
    username="ExampleBot",
    avatar_url="http://example.com/avatar.jpg",  # Replace with your bot's avatar URL
    embeds=[embed]
)

# Initialize WebhookER with the webhook URL
webhook = WebhookER(url=webhook_url)

# Send the message to the Discord channel
sent_message = webhook.send(message)

# Print the ID of the sent message
print("Message sent with ID:", sent_message.id)
