from ensaimeitor.base_batch_request import BaseBatchRequest


class Emails(BaseBatchRequest):
    endpoint = (
        "https://ensaimeitor.apsl.net/gen_emails/{amount}/?format=json&num={amount}"
    )
