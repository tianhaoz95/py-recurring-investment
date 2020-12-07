from src.core.stock_context import StockContext
import alpaca_trade_api as tradeapi


def should_consider_invest(context: StockContext) -> bool:
    return False

def is_available_for_investment(context: StockContext) -> bool:
    return False

def is_better_investment(lhs: StockContext, rhs: StockContext) -> int:
    return 0

def maybe_invest(api: tradeapi.REST) -> None:
    target_symbols = ['AAPL', 'VOO']
    context_list = [
        StockContext(target_symbol) for target_symbol in target_symbols
    ]
    # Populate stock context list for potential investment.
    for context in context_list:
        last_trade = api.get_last_trade(context.symbol)
        context.set_last_trade(last_trade)
    # Filter out a list of stocks that should be considered
    # for investment at the moment.
    filtered_context_list = filter(should_consider_invest, context_list)
    # Rank the potential list of stocks to invest based on
    # the potential growth.
    ranked_context_list = sorted(filtered_context_list, key=is_better_investment)
    # Send order to invest if fund is sufficient
    for ranked_context in ranked_context_list:
        # Maybe send order
        pass
