from ensaimeitor.base_batch_request import BaseBatchRequest


class MastercardNumbers(BaseBatchRequest):
    endpoint = (
        "https://ensaimeitor.apsl.net/gen_mastercard/{amount}/?format=json&num={amount}"
    )
