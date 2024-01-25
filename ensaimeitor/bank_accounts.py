from ensaimeitor.base_batch_request import BaseBatchRequest


class BankAccounts(BaseBatchRequest):
    endpoint = "https://ensaimeitor.apsl.net/bancos/{amount}/?format=json&num={amount}"
