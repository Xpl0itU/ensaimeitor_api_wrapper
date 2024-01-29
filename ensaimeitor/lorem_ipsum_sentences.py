from ensaimeitor.base_batch_request import BaseBatchRequest


class LoremIpsumSentences(BaseBatchRequest):
    endpoint = (
        "https://ensaimeitor.apsl.net/li_sentence/{amount}/?format=json&num={amount}"
    )
