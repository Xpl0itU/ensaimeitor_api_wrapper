from ensaimeitor.base_batch_request import BaseBatchRequest


class AmexNumbers(BaseBatchRequest):
    endpoint = (
        "https://ensaimeitor.apsl.net/gen_amex/{amount}/?format=json&num={amount}"
    )
