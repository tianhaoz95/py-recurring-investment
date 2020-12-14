from src.utils.cred.from_env_impl import AlpacaCredFromEnv
from abc import abstractmethod


class AlpacaCredFromYamlConfig(AlpacaCredFromEnv):
    @abstractmethod
    def read_config_content(self):
        pass

    def get_cred_internal(self, cred_type):
        raise NotImplementedError()