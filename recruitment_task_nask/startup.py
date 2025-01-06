from tags_requests_handlers.knowledge_base_handler import KnowledgeBaseHandler

knowledge_base_handler = None


def open_knowledge_base():
    global knowledge_base_handler
    knowledge_base_handler = KnowledgeBaseHandler()
    knowledge_base_handler.open()


def close_knowledge_base():
    if knowledge_base_handler and not knowledge_base_handler.is_closed():
        knowledge_base_handler.close()
