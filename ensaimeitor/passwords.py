from ensaimeitor.base_batch_request import BaseBatchRequest


class Passwords(BaseBatchRequest):
    endpoint = "https://ensaimeitor.apsl.net/gpw/{amount}/?format=json&num={amount}"
