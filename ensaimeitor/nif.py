from ensaimeitor.base_batch_request import BaseBatchRequest


class Nif(BaseBatchRequest):
    endpoint = "https://ensaimeitor.apsl.net/fiscal/{amount}/?format=json&num={amount}"
