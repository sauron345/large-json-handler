import ijson
import ipaddress

from tags_requests_handlers.ip_address_validator import IpAddressValidator
from django.conf import settings


class KnowledgeBaseSortedHandler:

    _DEFAULT_STORAGE_PATH = settings.BASE_DIR / 'sorted_knowledge_base.json'

    _uniq_ip_tags = set()
    _file_obj = None
    _ip_obj = None
    _storage_path = ''

    def __init__(self, storage_path=_DEFAULT_STORAGE_PATH):
        self._storage_path = storage_path

    def open(self):
        if self._file_obj is None or self._file_obj.closed:
            self._file_obj = open(self._storage_path, 'rb')

    def get_sorted_tags_by(self, ip):
        if IpAddressValidator(ip).is_correct():
            return self._execute_with_proper_ip(ip)
        return None

    def _execute_with_proper_ip(self, ip):
        self._init_state(ip)
        self._find_ip_tags()
        return sorted(self._uniq_ip_tags)

    def _init_state(self, ip):
        self._uniq_ip_tags = set()
        self._ip_obj = ipaddress.IPv4Address(ip)
        self._file_obj.seek(0)

    def _find_ip_tags(self):
        for ip_network, tags in ijson.kvitems(self._file_obj, ''):
            net_obj = ipaddress.IPv4Network(ip_network, strict=False)

            if self._ip_obj in net_obj:
                self._uniq_ip_tags.update(tags)

    def close(self):
        if self._file_obj and not self._file_obj.closed:
            self._file_obj.close()

    def is_closed(self):
        return self._file_obj.closed
