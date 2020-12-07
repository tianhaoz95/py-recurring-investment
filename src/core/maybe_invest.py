from core.user_context import UserContext
from src.core.stock_context import StockContext
import alpaca_trade_api as tradeapi


class StockFeasibilityChecker():
    def __init__(self, user_context: UserContext) -> None:
        self.user_context = user_context

    def __call__(self, stock_context: StockContext) -> bool:
        return False


class StockComparator():
    def __init__(self, user_context: UserContext) -> None:
        self.user_context = user_context

    def __call__(self, lhs: StockContext, rhs: StockContext) -> int:
        return 0


class StockActionExecutor():
    def __init__(self, user_context: UserContext) -> None:
        self.user_context = user_context

    def __call__(self, stock_context: StockContext) -> None:
        pass


def maybe_invest(api: tradeapi.REST) -> None:
    target_symbols = ['AAPL', 'VOO']
    user_context = UserContext()
    user_context.set_account(api.get_account())
    stock_context_list = [
        StockContext(target_symbol) for target_symbol in target_symbols
    ]
    # Populate stock context list for potential investment.
    for stock_context in stock_context_list:
        last_trade = api.get_last_trade(stock_context.symbol)
        stock_context.set_last_trade(last_trade)
    # Filter out a list of stocks that should be considered
    # for investment at the moment.
    stock_feasibility_checker = StockFeasibilityChecker(user_context)
    filtered_stock_context_list = filter(stock_feasibility_checker,
                                         stock_context_list)
    # Rank the potential list of stocks to invest based on
    # the potential growth.
    stock_comparator = StockComparator(user_context)
    ranked_stock_context_list = sorted(filtered_stock_context_list,
                                       key=stock_comparator)
    # Send order to invest if fund is sufficient
    stock_action_executor = StockActionExecutor(user_context)
    for ranked_stock_context in ranked_stock_context_list:
        stock_action_executor(ranked_stock_context)
