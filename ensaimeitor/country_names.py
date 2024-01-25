from ensaimeitor.base_batch_request import BaseBatchRequest


class CountryNames(BaseBatchRequest):
    endpoint = "https://ensaimeitor.apsl.net/country/{amount}/?format=json&num={amount}"
