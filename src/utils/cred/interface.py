from abc import ABC, abstractmethod


class AlpacaCred(ABC):
    def get_cred(self, cred_type, cli_args):
        if cred_type in cli_args:
            return cli_args[cred_type]
        else:
            return self.get_cred_internal(cred_type)

    @abstractmethod
    def get_cred_internal(self, cred_type):
        pass
