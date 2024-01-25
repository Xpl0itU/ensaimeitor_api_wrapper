from ensaimeitor.base_batch_request import BaseBatchRequest


class ChomskyText(BaseBatchRequest):
    endpoint = "https://ensaimeitor.apsl.net/chomsky/{amount}/?format=json&num={amount}"
