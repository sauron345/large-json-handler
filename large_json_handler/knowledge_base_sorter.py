import json

import ijson

from django.conf import settings


class KnowledgeBaseHandlerSorter:

    _DEFAULT_STORAGE_PATH = settings.BASE_DIR / 'large_json_handler/knowledge_base.json'
    _DEFAULT_SORTED_STORAGE_PATH = settings.BASE_DIR / 'large_json_handler/sorted_knowledge_base.json'
    _MAX_IP_NET_TAGS = 10

    _sorted_ip_nets = ''
    _file_obj = None
    _sorted_file_obj = None

    def __init__(
        self,
        storage_path=_DEFAULT_STORAGE_PATH,
        sorted_storage_path=_DEFAULT_SORTED_STORAGE_PATH
    ):
        self._file_obj = open(storage_path, 'rb')
        self._sorted_file_obj = open(sorted_storage_path, 'wb')

    def execute(self):
        self._init_state()
        self._find_and_sort_ip_net_with_tags()
        self._close_sorted_storage()
        self._close_files()

    def _init_state(self):
        self._start_position()
        self._sorted_file_write("{\n")

    def _start_position(self):
        self._file_obj.seek(0)
        self._sorted_file_obj.seek(0)

    def _find_and_sort_ip_net_with_tags(self):
        for item in ijson.items(self._file_obj, 'item'):

            if item['ip_network'] not in self._sorted_ip_nets:
                ip_net = item['ip_network']
            else:
                continue

            found_tags = self._get_tags_for(ip_net)
            self._add_to_sorted(ip_net)
            self._add_new_item(ip_net, sorted(found_tags))

    def _get_tags_for(self, ip_net):
        self._file_obj.seek(0)
        uniq_tags = set()

        for item in ijson.items(self._file_obj, 'item'):
            if len(uniq_tags) >= self._MAX_IP_NET_TAGS:
                break
            if ip_net == item['ip_network']:
                uniq_tags.add(item['tag'])

        return uniq_tags

    def _add_to_sorted(self, ip_net):
        self._sorted_ip_nets += ip_net + ','

    def _add_new_item(self, ip_net, tags):
        ip_net_with_tags = f'\t"{ip_net}": {json.dumps(tags)},\n'
        self._sorted_file_write(ip_net_with_tags)

    def _sorted_file_write(self, text):
        self._sorted_file_obj.write(text.encode('utf-8'))

    def _close_sorted_storage(self):
        self._sorted_file_obj.seek(-2, 2)
        self._sorted_file_obj.truncate()
        self._sorted_file_write("\n}")

    def _close_files(self):
        self._sorted_file_obj.close()
        self._file_obj.close()
