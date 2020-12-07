import logging
import alpaca_trade_api as tradeapi
from src.utils.cred.from_env_impl import get_alpaca_cred


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('main')
    logger.setLevel(logging.DEBUG)
    cred = get_alpaca_cred()
    api = tradeapi.REST(cred.get_cred('key'),
                        cred.get_cred('secret'),
                        base_url=cred.get_cred('endpoint'))
    """
    watchlists = api.get_watchlists()
    logger.info('Retrieved the watchlists: {watchlists}'.format(
        watchlists=watchlists))
    """
    """
    account = api.get_account()
    logger.info('Retrieved the account: {account}'.format(account=account))
    """
    """
    example_bar = api.get_barset('AAPL', '1D')
    logger.info('Retrieved the example bar: ${example_bar}'.format(example_bar=example_bar))
    """
    example_last_trade = api.get_last_trade('AAPL')
    logger.info(
        'Retrieved the example last trade: ${example_last_trade}'.format(
            example_last_trade=example_last_trade))
    example_last_quote = api.get_last_quote('AAPL')
    logger.info(
        'Retrieved the example last quote: {example_last_quote}'.format(
            example_last_quote=example_last_quote))
    logger.info('Done!')


if __name__ == '__main__':
    main()
