from alpaca_trade_api.entity import Quote, Trade


class StockContext():
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol
        self.last_trade = None
        self.last_quote = None

    def set_last_trade(self, last_trade: Trade) -> None:
        self.last_trade = last_trade

    def set_last_quote(self, last_quote: Quote) -> None:
        self.last_quote = last_quote
