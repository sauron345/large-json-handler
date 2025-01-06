import re


class IpAddressValidator:

    _MIN_OCTET_NUM = 0
    _MAX_OCTET_NUM = 255

    _IP_PATTERN = r"(\d{1,3}\.){3}\d{1,3}"

    def __init__(self, ip):
        self._ip = ip

    def is_correct(self) -> bool:
        if not self._is_compatible_with_pattern():
            return False

        if not self._check_octets_correctness():
            return False

        return True

    def _is_compatible_with_pattern(self):
        if re.fullmatch(self._IP_PATTERN, self._ip):
            return True
        return False

    def _check_octets_correctness(self):
        octets = self._ip.split('.')
        for octet in octets:
            octet_num = int(octet)
            if not self._is_octet_proper_size(octet_num):
                return False
        return True

    def _is_octet_proper_size(self, octet):
        return self._MIN_OCTET_NUM <= octet <= self._MAX_OCTET_NUM
