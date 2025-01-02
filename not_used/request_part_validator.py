from abc import ABC, abstractmethod


class RequestPartValidator(ABC):

    def __init__(self, request):
        if request is dict:
            self.__request = request

        raise TypeError("Request should be an object of dict.")

    @abstractmethod
    def is_correct(self) -> bool:
        pass

    @abstractmethod
    def __is_key_name_correct(self):
        pass
