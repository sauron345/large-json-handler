from django.test import TestCase
from django.conf import settings

from tags_requests_handlers.knowledge_base_handler import KnowledgeBaseHandler
from tags_requests_handlers.test_resources import expected_results, ips_with_tags, ips_without_tags, invalid_ips


class TestKnowledgeBaseHandler(TestCase):

    _knowledge_base_handler = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        storage_path = settings.BASE_DIR / 'tags_requests_handlers/simple_knowledge_base.json'
        cls._knowledge_base_handler = KnowledgeBaseHandler(storage_path)
        cls._knowledge_base_handler.open()

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
        cls._knowledge_base_handler.close()
        super().tearDownClass()
