import requests


class Pictures:
    endpoint = "http://ensaimeitor.apsl.net/imatge/{width}/{height}/"

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def fetch(self, timeout=30):
        return requests.get(
            self.endpoint.format(width=self.width, height=self.height), timeout=timeout
        ).content
