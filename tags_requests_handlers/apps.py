from django.apps import AppConfig

from recruitment_task_nask.startup import open_knowledge_base


class RequestsTagsHandlersConfig(AppConfig):
    name = 'tags_requests_handlers'

    def ready(self):
        open_knowledge_base()
