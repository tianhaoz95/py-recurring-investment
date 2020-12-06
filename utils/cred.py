import os
import alpaca_trade_api as tradeapi
from abc import ABC, abstractmethod


class AlpacaCred(ABC):
    @abstractmethod
    def get_cred_mapping(self):
        pass

    def get_cred(self, cred_type):
        cred_mapping = self.get_cred_mapping()
        if (cred_type not in cred_mapping):
            raise RuntimeError('{cred_type} not found in cred mapping.'.format(
                cred_type=cred_type))
        env_var_id = cred_mapping[cred_type]
        if (env_var_id not in os.environ):
            raise RuntimeError('{env_var_id} not found in envrionment.'.format(
                env_var_id=env_var_id))
        return os.environ[env_var_id]


class DevAlpacaCred(AlpacaCred):
    def get_cred_mapping(self):
        return {
            'endpoint': 'ALPACA_API_DEV_ENDPOINT',
            'key': 'ALPACA_API_DEV_KEY',
            'secret': 'ALPACA_API_DEV_SECRET'
        }


class ProdAlpacaCred(AlpacaCred):
    def get_cred_mapping(self):
        return {
            'endpoint': 'ALPACA_API_PROD_ENDPOINT',
            'key': 'ALPACA_API_PROD_KEY',
            'secret': 'ALPACA_API_PROD_SECRET'
        }


def get_alpaca_cred():
    alpaca_api_mode_key = 'ALPACA_API_MODE'
    allowed_alpaca_api_mode = ['dev', 'prod']
    if (alpaca_api_mode_key not in os.environ):
        raise RuntimeError('{alpaca_api_mode_key} not found.'.format(
            alpaca_api_mode_key=alpaca_api_mode_key))
    alpaca_api_mode = os.environ[alpaca_api_mode_key]
    if (alpaca_api_mode not in allowed_alpaca_api_mode):
        raise RuntimeError(
            'Mode {alpaca_api_mode} not allowed. Allowed modes are {allowed_alpaca_api_mode}'
            .format(alpaca_api_mode=alpaca_api_mode,
                    allowed_alpaca_api_mode=allowed_alpaca_api_mode))
    if alpaca_api_mode == 'dev':
        return DevAlpacaCred()
    elif alpaca_api_mode == 'prod':
        return ProdAlpacaCred()
    else:
        raise RuntimeError('Should not reach $0 mode'.format(alpaca_api_mode))
