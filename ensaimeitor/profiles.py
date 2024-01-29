import requests


class Profiles:
    endpoint = "https://ensaimeitor.apsl.net/perfil/?format=json"

    def fetch(self, timeout=30):
        return requests.get(self.endpoint, timeout=timeout).json()
