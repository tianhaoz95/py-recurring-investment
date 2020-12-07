from src.utils.cred.from_env_impl import AlpacaCredFromEnv


class AlpacaCredFromYamlConfig(AlpacaCredFromEnv):
    def get_cred(self, cred_type):
        raise NotImplementedError()