import json


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class KnowledgeBaseExtractor(metaclass=SingletonMeta):

    _STORAGE_PATH = '../knowledge_base.json'
    _EXCLUDED_CHARS = [']', '[', ',', ' ', '\n']
    _MAX_CHARS_IN_ROW = 127

    def __init__(self):
        self._storage_obj = open(self._STORAGE_PATH, 'r', encoding='utf8')
        self._row_chars = ''
        self._end_occurred = False

    def next_item(self):
        while self.has_next():
            char = self._storage_obj.read(1)

            if char == '':
                self._end_extraction()
                return ''
            elif len(self._row_chars) > self._MAX_CHARS_IN_ROW:
                self._clear_row_chars()
                return ''
            elif self._is_item_seperator(char):
                self._add_to_found_chars(char)
            elif char not in self._EXCLUDED_CHARS:
                self._add_to_found_chars(char)

            if char == '}' and self._is_start_dict_occurred():
                temp_row_chars = self._row_chars
                self._clear_row_chars()
                return temp_row_chars

    def has_next(self):
        return not self._end_occurred

    def _set_end_occurred(self, choice: bool):
        self._end_occurred = choice

    def _add_to_found_chars(self, char):
        self._row_chars += char

    def _clear_row_chars(self):
        self._row_chars = ''

    def _is_start_dict_occurred(self):
        return self._row_chars.find('{') != -1

    def _is_item_seperator(self, char):
        return char == ',' and self._is_start_dict_occurred() and self._is_end_dict_occurred()

    def _is_end_dict_occurred(self):
        return self._row_chars.find('}') == -1

    def _end_extraction(self):
        self._storage_obj.close()
        self._set_end_occurred(True)
