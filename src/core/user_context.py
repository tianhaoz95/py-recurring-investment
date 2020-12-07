from alpaca_trade_api.entity import Account


class UserContext():
    def __init__(self) -> None:
        self.account = None

    def set_account(self, account: Account):
        self.account = account
