from ensaimeitor.base_batch_request import BaseBatchRequest


class PhoneNumbers(BaseBatchRequest):
    endpoint = (
        "https://ensaimeitor.apsl.net/spanish_phone/{amount}/?format=json&num={amount}"
    )
