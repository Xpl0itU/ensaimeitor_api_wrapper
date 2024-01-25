import requests


class BaseBatchRequest:
    endpoint = None

    def __init__(self, amount):
        self.amount = amount

    def set_amount(self, amount):
        self.amount = amount

    def fetch(self, timeout=30):
        return requests.get(
            self.endpoint.format(amount=self.amount), timeout=timeout
        ).json()
