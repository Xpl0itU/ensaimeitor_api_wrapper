from ensaimeitor.base_batch_request import BaseBatchRequest


class ProvinceNames(BaseBatchRequest):
    endpoint = (
        "https://ensaimeitor.apsl.net/provincias/{amount}/?format=json&num={amount}"
    )
