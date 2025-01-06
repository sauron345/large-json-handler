import ijson
import ipaddress

from tags_requests_handlers.ip_address_validator import IpAddressValidator
from django.conf import settings


class KnowledgeBaseHandler:

    _DEFAULT_STORAGE_PATH = settings.BASE_DIR / 'knowledge_base.json'

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

        ip_tags_list = list(self._uniq_ip_tags)
        return sorted(ip_tags_list)

    def _init_state(self, ip):
        self._uniq_ip_tags = set()
        self._ip_obj = ipaddress.IPv4Address(ip)
        self._file_obj.seek(0)

    def _find_ip_tags(self):
        for item in ijson.items(self._file_obj, 'item'):
            net_obj = ipaddress.IPv4Network(item['ip_network'], strict=False)

            if self._ip_obj in net_obj:
                self._uniq_ip_tags.add(item['tag'])

    def close(self):
        if self._file_obj and not self._file_obj.closed:
            self._file_obj.close()

    def is_closed(self):
        return self._file_obj.closed
