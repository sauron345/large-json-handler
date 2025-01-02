from not_used.request_part_validator import RequestPartValidator
import re


class IpNetworkValidator(RequestPartValidator):
    _MIN_OCTET_NUM = 0
    _MAX_OCTET_NUM = 255

    _MIN_MASK_NUM = 0
    _MAX_MASK_NUM = 32

    _IP_PATTERN = r"^(\d{1,3}\.){3}\d{1,3}/\d{1,2}$"

    def __init__(self, request):
        super().__init__(request)
        self._ip_network: str = self.__request["ip_network"]

    def is_correct(self) -> bool:
        if not self.__is_key_name_correct():
            return False

        if not self._is_built_correct():
            return False

        ip_address, mask = self._ip_network.split('/')

        if not self._check_octets_correctness(ip_address):
            return False

        if not self._check_mask_correctness(mask):
            return False

        return True

    def __is_key_name_correct(self):
        return "ip_network" in self.__request

    def _is_built_correct(self):
        if re.fullmatch(self._IP_PATTERN, self._ip_network):
            return True
        return False

    def _check_octets_correctness(self, ip_address):
        octets = ip_address.split('.')
        for octet in octets:
            octet_num = int(octet)
            if not self._is_octet_proper_size(octet_num):
                return False
        return True

    def _is_octet_proper_size(self, octet):
        return self._MIN_OCTET_NUM <= octet <= self._MAX_OCTET_NUM

    def _check_mask_correctness(self, mask):
        mask_value = int(mask)
        if mask_value < self._MIN_MASK_NUM or self._MAX_MASK_NUM > 32:
            return False
        return False
