import ijson
import ipaddress


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class KnowledgeBaseHandler(metaclass=SingletonMeta):

    _STORAGE_PATH = 'knowledge_base.json'

    def get_tags_by(self, ip):
        uniq_ip_tags = set()

        ip_obj = ipaddress.IPv4Address(ip)

        ips_tags_sorted_file = open(self._STORAGE_PATH, 'rb')

        for item in ijson.items(ips_tags_sorted_file, 'item'):
            net_obj = ipaddress.IPv4Network(item['ip_network'], strict=False)

            if ip_obj in net_obj:
                uniq_ip_tags.add(item['tag'])

        ips_tags_sorted_file.close()

        return sorted(list(uniq_ip_tags))
