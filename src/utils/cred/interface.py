from abc import ABC, abstractmethod

class AlpacaCred(ABC):
    @abstractmethod
    def get_cred(self, cred_type):
        pass