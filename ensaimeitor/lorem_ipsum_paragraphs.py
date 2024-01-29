from ensaimeitor.base_batch_request import BaseBatchRequest


class LoremIpsumParagraphs(BaseBatchRequest):
    endpoint = (
        "https://ensaimeitor.apsl.net/li_paragraph/{amount}/?format=json&num={amount}"
    )
