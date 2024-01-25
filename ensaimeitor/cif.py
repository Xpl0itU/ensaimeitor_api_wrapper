from ensaimeitor.base_batch_request import BaseBatchRequest


class Cif(BaseBatchRequest):
    endpoint = "https://ensaimeitor.apsl.net/cif/{amount}/?format=json&num={amount}"
