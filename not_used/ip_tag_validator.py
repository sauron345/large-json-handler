from not_used.request_part_validator import RequestPartValidator


class IpTagValidator(RequestPartValidator):
    _MIN_TAG_LEN = 1
    _MAX_TAG_LEN = 16

    def __init__(self, request):
        super().__init__(request)
        self._tag: str = self.__request["tag"]

    def is_correct(self):
        if not self.__is_key_name_correct():
            return False
        if not self._is_proper_size():
            return False

        return True

    def __is_key_name_correct(self):
        return "tag" in self.__request

    def _is_proper_size(self):
        return self._MIN_TAG_LEN <= len(self._tag) <= self._MAX_TAG_LEN
