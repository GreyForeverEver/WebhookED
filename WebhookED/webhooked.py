import requests

class WebhookEField(object):
    def __init__(self, name: str, value: str, inline: bool = False):
        """
        Initializes a WebhookEField instance with the provided parameters.

        Parameters:
        - name (str): The name/title of the field.
        - value (str): The value/content of the field.
        - inline (bool, optional): Whether the field should be displayed inline or not. Default is False.
        """
        self.name = name
        self.value = value
        self.inline = inline

    def get_dict(self) -> dict:
        """
        Returns a dictionary representation of the WebhookEField instance.

        Returns:
        - dict: A dictionary containing the attributes of the WebhookEField instance.
        """
        data = {
            "name":self.name,
            "value":self.value,
            "inline":self.inline
        }
        return data
        
class WebhookEEmbed(object):
    def __init__(self, title = None, e_type = None, description = None, url = None, timestamp = None, color = None, footer = None, image = None, thumbnail = None, video = None, provider = None, author = None, fields : [WebhookEField] or WebhookEField = []):
        """
        Initializes a WebhookEEmbed instance with optional parameters.

        Parameters:
        - title: The title of the embed.
        - e_type: The type of the embed.
        - description: The description text of the embed.
        - url: The URL of the embed.
        - timestamp: The timestamp of the embed.
        - color: The color code of the embed.
        - footer: The footer of the embed.
        - image: The image of the embed.
        - thumbnail: The thumbnail of the embed.
        - video: The video of the embed.
        - provider: The provider of the embed.
        - author: The author of the embed.
        - fields: The fields of the embed.
        """
        self.title = title
        self.type = e_type
        self.description = description
        self.url = url
        self.timestamp = timestamp
        self.color = color
        self.footer = footer
        self.image = image
        self.thumbnail = thumbnail
        self.video = video
        self.provider = provider
        self.author = author
        if type(fields) is list:
            self.fields = fields
        else:
            self.fields = [fields]

    def get_dict(self) -> dict:
        """
        Returns a dictionary representation of the WebhookEEmbed instance.

        Returns:
        - dict: A dictionary containing the attributes of the WebhookEEmbed instance.
        """
        data = {
            "title":self.title,
            "type":self.type,
            "description":self.description,
            "url":self.url,
            "timestamp":self.timestamp,
            "color":self.color,
            "footer":self.footer,
            "image":self.image,
            "thumbnail":self.thumbnail,
            "video":self.video,
            "provider":self.provider,
            "author":self.author,
            "fields":[f.get_dict() for f in self.fields]
        }
        return data
    
    def load_from_dict(self, dict: dict):
        """
        Populates the WebhookEEmbed instance's attributes from a dictionary.

        Parameters:
        - dict: A dictionary containing attributes to populate the WebhookEEmbed instance.

        Returns:
        - None
        """
        self.title = dict["title"]
        self.type = dict["type"]
        self.description = dict["description"]
        self.url = dict["url"]
        self.timestamp = dict["timestamp"]
        self.color = dict["color"]
        self.footer = dict["footer"]
        self.image = dict["image"]
        self.thumbnail = dict["thumbnail"]
        self.video = dict["video"]
        self.provider = dict["provider"]
        self.author = dict["author"]
        self.fields = dict["fields"]
    
    def add_field(self, field: WebhookEField):
        self.fields.append(field)


class WebhookEMessage(object):
    def __init__(self, content: str = None, username: str = None, avatar_url: str = None, tts: bool = None, embeds: list[WebhookEEmbed] or WebhookEEmbed = []):
        """
        Initializes a WebhookEMessage instance with optional parameters.

        Parameters:
        - content: The content of the message.
        - username: The username of the message sender.
        - avatar_url: The avatar URL of the message sender.
        - tts: A boolean indicating if the message should be sent as a TTS (Text-to-Speech) message.
        - embeds: A list of WebhookEEmbed instances or a single WebhookEEmbed instance representing message embeds.
        """
        self.content = content
        self.username = username
        self.avatar_url = avatar_url
        self.tts = tts
        if type(embeds) is list:
            self.embeds = embeds
        else:
            self.embeds = [embeds]

    def get_dict(self):
        """
        Returns a dictionary representation of the WebhookEMessage instance.

        Returns:
        - dict: A dictionary containing the attributes of the WebhookEMessage instance.
        """
        data = {
            "content":self.content,
            "username":self.username,
            "avatar_url":self.avatar_url,
            "tts":self.tts,
            "embeds":[e.get_dict() for e in self.embeds]
        }
        return data 
    
    def load_from_dict(self, dict: dict):
        """
        Populates the WebhookEMessage instance's attributes from a dictionary.

        Parameters:
        - dict: A dictionary containing attributes to populate the WebhookEMessage instance.

        Returns:
        - None
        """
        self.content = dict["content"]
        self.username = dict["username"]
        self.avatar_url = dict["avatar_url"]
        self.tts = dict["tts"]
        self.embeds = [WebhookEEmbed().load_from_dict(e) for e in dict["embeds"]]

    def add_embed(self, embed: WebhookEEmbed):
        self.embeds.append(embed)


class WebhookEMessageSent(WebhookEMessage):
    def __init__(self, id: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id

    def get_dict(self):
        data = super().get_dict()
        data.update({"id":self.id})
        return data


class WebhookEError(Exception):
    def __init__(self, message="Invalid Message"):
        self.message = message
        super().__init__(self.message)

class WebhookER(object):
    def __init__(self, url):
        """
        Initializes a WebhookER instance with the Discord webhook URL.

        Parameters:
        - url: The URL of the Discord webhook.
        """
        self.url = url

    def _post(self, data: dict):
        response = requests.post(self.url+"?wait=true", json = data)
        if response.status_code != 200:
            if response.status_code == 400:
                raise WebhookEError("Wrong Webhook URL.")
            if response.json()["code"] == 50006:
                raise WebhookEError("Message Cannot Be Empty.")
        return response
    
    def _edit(self, data: dict, id: str):
        response = requests.patch(self.url+f"/messages/{id}?wait=true", json = data)
        if response.status_code != 200:
            if response.json()["code"] == 0:
                raise WebhookEError("Cannot edit this message, unknown or not allowed.")
        return response
    
    def send(self, message: WebhookEMessage) -> WebhookEMessageSent:
        """
        Sends a message to the Discord webhook.

        Parameters:
        - message: An instance of WebhookEMessage representing the message to be sent.

        Returns:
        - WebhookEMessageSent: An instance representing the sent message with its ID.

        Raises:
        - WebhookEError: If there is an issue with the request.
        """
        response =  self._post(message.get_dict())
        return WebhookEMessageSent(id = response.json()["id"], content = message.content, embeds = message.embeds, tts = message.tts, username = message.username, avatar_url = message.avatar_url)
    
    def edit(self, sent_message: WebhookEMessageSent or str, new_message: WebhookEMessage) -> WebhookEMessageSent:
        """
        Edits a previously sent message on the Discord webhook.

        Parameters:
        - sent_message: An instance of WebhookEMessageSent or the ID of the message to be edited.
        - new_message: An instance of WebhookEMessage representing the updated message.

        Returns:
        - WebhookEMessageSent: An instance representing the edited message with its updated ID.

        Raises:
        - WebhookEError: If there is an issue with the request.
        """
        if type(sent_message) is str:
            response = self._edit(new_message.get_dict(), sent_message)
        else:
            response = self._edit(new_message.get_dict(), sent_message.id)
        return WebhookEMessageSent(id = response.json()["id"], content = new_message.content, embeds = new_message.embeds, tts = new_message.tts, username = new_message.username, avatar_url = new_message.avatar_url)