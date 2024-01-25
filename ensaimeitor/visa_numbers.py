from ensaimeitor.base_batch_request import BaseBatchRequest


class VisaNumbers(BaseBatchRequest):
    endpoint = (
        "https://ensaimeitor.apsl.net/gen_visa/{amount}/?format=json&num={amount}"
    )
