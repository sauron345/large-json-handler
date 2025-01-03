import ijson
import ipaddress

from tags_request_handlers.singleton_meta import SingletonMeta


class KnowledgeBaseHandler(metaclass=SingletonMeta):

    _FILE_PATH = 'knowledge_base.json'

    _uniq_ip_tags = set()
    _file_obj = None
    _ip_obj = None

    def get_sorted_tags_by(self, ip):
        self._init_state(ip)
        self._find_ip_tags()
        self._file_obj.close()
        ip_tags_list = list(self._uniq_ip_tags)
        return sorted(ip_tags_list)

    def _init_state(self, ip):
        self._uniq_ip_tags = set()
        self._ip_obj = ipaddress.IPv4Address(ip)
        self._file_obj = open(self._FILE_PATH, 'rb')

    def _find_ip_tags(self):
        for item in ijson.items(self._file_obj, 'item'):
            net_obj = ipaddress.IPv4Network(item['ip_network'], strict=False)

            if self._ip_obj in net_obj:
                self._uniq_ip_tags.add(item['tag'])
