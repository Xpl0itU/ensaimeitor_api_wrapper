from ensaimeitor.base_batch_request import BaseBatchRequest


class PersonNames(BaseBatchRequest):
    endpoint = (
        "https://ensaimeitor.apsl.net/personas/{amount}/?format=json&num={amount}"
    )
