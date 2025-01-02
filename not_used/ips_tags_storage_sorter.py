from knowledge_base_extractor import KnowledgeBaseExtractor
import json
import ijson
import ipaddress


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class IpsTagsStorageSorter(metaclass=SingletonMeta):

    _STORAGE_PATH = 'ips_tags_storage_sorted.json'

    def __init__(self):
        self._is_first_iter = True
        self._is_ip_founded = False
        self._subnet_founded = ''
        self._tags_founded = []
        try:
            self._sort_content()
        except json.decoder.JSONDecodeError:
            pass

    def _sort_content(self):

        ips_tags_storage_extractor = KnowledgeBaseExtractor()

        while ips_tags_storage_extractor.has_next():
            ip_and_tags_str = ips_tags_storage_extractor.next_item()
            ip_and_tags_dict = dict(json.loads(ip_and_tags_str))

            extracted_subnet = ip_and_tags_dict['ip_network']
            extracted_tag = ip_and_tags_dict['tag']

            if self._is_first_iter:
                self._write_first_content(extracted_subnet, extracted_tag)
                self._is_first_iter = False

            ips_tags_sorted_file = open(self._STORAGE_PATH, 'r', encoding='utf8')

            for tags in ijson.items(ips_tags_sorted_file, extracted_subnet):
                self._subnet_founded = extracted_subnet
                self._tags_founded.extend(tags)
                self._tags_founded.append(extracted_tag)
                self._write_next_content(self._subnet_founded, self._tags_founded)
                break
            else:
                ips_tags_sorted_file.close()
                self._write_next_content(extracted_subnet, extracted_tag)

            ips_tags_sorted_file.close()

    def _write_first_content(self, subnet, tag):
        with open(self._STORAGE_PATH, 'rb+') as ips_tags_sorted_file:
            ips_tags_sorted_file.seek(0)
            ips_tags_sorted_file.truncate()
            ips_tags_sorted_file.write('{\n'.encode('utf-8'))
            ips_tags_sorted_file.write(f'    {json.dumps(subnet)}: [{json.dumps(tag)}]'.encode('utf-8'))
            ips_tags_sorted_file.write('\n}'.encode('utf-8'))

    def _write_next_content(self, subnet, tags):
        with open(self._STORAGE_PATH, 'rb+') as ips_tags_sorted_file:
            ips_tags_sorted_file.seek(-1, 2)
            ips_tags_sorted_file.truncate()
            if isinstance(tags, list):
                ips_tags_sorted_file.write(f',\n    {json.dumps(subnet)}: {json.dumps(tags)}'.encode('utf-8'))
            else:
                ips_tags_sorted_file.write(f',\n    {json.dumps(subnet)}: [{json.dumps(tags)}]'.encode('utf-8'))
            ips_tags_sorted_file.write('\n}'.encode('utf-8'))

    def get_tags_by(self, ip):
        uniq_ip_tags = []

        ip_obj = ipaddress.IPv4Address(ip)

        for subnet, tags in ijson.kvitems(self._STORAGE_PATH, ''):
            subnet_obj = ipaddress.IPv4Network(subnet, strict=False)

            if ip_obj in subnet_obj:
                if tags and isinstance(tags, list):
                    for tag in tags:
                        if tag not in uniq_ip_tags:
                            uniq_ip_tags.extend(tag)
                elif tags not in uniq_ip_tags:
                    uniq_ip_tags.append(tags)

        return sorted(uniq_ip_tags)


IpsTagsStorageSorter()
