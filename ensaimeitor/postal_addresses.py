from ensaimeitor.base_batch_request import BaseBatchRequest


class PostalAddresses(BaseBatchRequest):
    endpoint = (
        "https://ensaimeitor.apsl.net/direccion/{amount}/?format=json&num={amount}"
    )
