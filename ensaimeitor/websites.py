from ensaimeitor.base_batch_request import BaseBatchRequest


class Websites(BaseBatchRequest):
    endpoint = (
        "https://ensaimeitor.apsl.net/gen_urls/{amount}/?format=json&num={amount}"
    )
