from ensaimeitor.base_batch_request import BaseBatchRequest


class Company(BaseBatchRequest):
    endpoint = (
        "https://ensaimeitor.apsl.net/empresas/{amount}/?format=json&num={amount}"
    )
