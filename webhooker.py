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

    def get_dict(self):
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
        data = {
            "content":self.content,
            "username":self.username,
            "avatar_url":self.avatar_url,
            "tts":self.tts,
            "embeds":[e.get_dict() for e in self.embeds]
        }
        return data 

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
            if response.json()["code"] == 50006:
                raise WebhookEError("Message Cannot Be Empty.")
        return response
    
    def _edit(self, data: json,id: str):
        response = requests.post(self.url+f"/messages/{id}", json = data)
        print(response.content)
        if response.status_code != 200:
            if response.json()["code"] == 0:
                raise WebhookEError("Cannot edit this message, unknown or not allowed.")
        return response
    
    def send(self, message: WebhookEMessage) -> WebhookEMessageSent:
        response =  self._post(message.get_dict())
        return WebhookEMessageSent(response.json()["id"], self)
    
    def edit(self, sent_message: WebhookEMessageSent, new_message: WebhookEMessage) -> WebhookEMessageSent:
        response = self._edit(new_message.get_dict(), sent_message.id)
        return WebhookEMessageSent(response.json()["id"], self)
    
