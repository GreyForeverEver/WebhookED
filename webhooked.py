import json
import requests
        
class WebhookEEmbed(object):
    def __init__(self, title = None, type = None, description = None, url = None, timestamp = None, color = None, footer = None, image = None, thumbnail = None, video = None, provider = None, author = None, fields = None):
        self.title = title
        self.type = type
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
        self.fields = fields

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
            "fields":self.fields
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

class WebhookEMessage(object):
    def __init__(self, content: str = None, username: str = None, avatar_url: str = None, tts: bool = None, embeds: list[WebhookEEmbed] or WebhookEEmbed = []):
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


class WebhookEMessageSent(WebhookEMessage):
    def __init__(self, id: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id

class WebhookEError(Exception):
    def __init__(self, message="Invalid Message"):
        self.message = message
        super().__init__(self.message)

class WebhookER(object):
    def __init__(self, url):
        self.url = url

    def _post(self, data: json):
        response = requests.post(self.url+"?wait=true", json = data)
        if response.status_code != 200:
            if response.status_code == 400:
                raise WebhookEError("Wrong Webhook URL.")
            if response.json()["code"] == 50006:
                raise WebhookEError("Message Cannot Be Empty.")
        return response
    
    def _edit(self, data: json,id: str):
        response = requests.post(self.url+f"/messages/{id}", json = data)
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
        return WebhookEMessageSent(response.json()["id"], self)
    
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
        response = self._edit(new_message.get_dict(), sent_message.id)
        return WebhookEMessageSent(response.json()["id"], self)
