import time

from django.test import TestCase
from django.conf import settings

from large_json_handler.knowledge_base_sorted_handler import KnowledgeBaseSortedHandler
from large_json_handler.knowledge_base_sorter import KnowledgeBaseHandlerSorter
from tags_requests_handlers.test_resources import expected_results, ips_with_tags, ips_without_tags, invalid_ips


class TestKnowledgeBaseHandler(TestCase):

    _knowledge_base_handler = None
    _start = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        storage_path = settings.BASE_DIR / 'tags_requests_handlers/simple_knowledge_base.json'
        sorted_storage_path = settings.BASE_DIR / 'tags_requests_handlers/sorted_simple_knowledge_base.json'

        knowledge_base_sorter = KnowledgeBaseHandlerSorter(storage_path, sorted_storage_path)
        knowledge_base_sorter.execute()

        cls._knowledge_base_handler = KnowledgeBaseSortedHandler(sorted_storage_path)
        cls._knowledge_base_handler.open()

        cls._start = time.time()

    def test_ips_with_tags(self):
        for ip in ips_with_tags:
            ip_tags = self._knowledge_base_handler.get_sorted_tags_by(ip)
            self.assertEqual(ip_tags, expected_results[ip])

    def test_ips_without_tags(self):
        for ip in ips_without_tags:
            ip_tags = self._knowledge_base_handler.get_sorted_tags_by(ip)
            self.assertEqual(ip_tags, [])

    def test_with_invalid_ips(self):
        for ip in invalid_ips:
            ip_tags = self._knowledge_base_handler.get_sorted_tags_by(ip)
            self.assertEqual(ip_tags, None)

    @classmethod
    def tearDownClass(cls):
        print(f"\n\nTesting time: {time.time() - cls._start:.4f} seconds\n")
        cls._knowledge_base_handler.close()
        super().tearDownClass()
