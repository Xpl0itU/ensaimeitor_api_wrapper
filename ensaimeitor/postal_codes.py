from ensaimeitor.base_batch_request import BaseBatchRequest


class PostalCodes(BaseBatchRequest):
    endpoint = (
        "https://ensaimeitor.apsl.net/cod_postal/{amount}/?format=json&num={amount}"
    )
