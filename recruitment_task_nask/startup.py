from recruitment_task_nask.knowledge_base_sorted_handler import KnowledgeBaseSortedHandler
from recruitment_task_nask.knowledge_base_sorter import KnowledgeBaseHandlerSorter

knowledge_base_sorted_handler = None


def open_knowledge_base():
    global knowledge_base_sorted_handler

    knowledge_base_handler_sorter = KnowledgeBaseHandlerSorter()
    knowledge_base_handler_sorter.execute()

    knowledge_base_sorted_handler = KnowledgeBaseSortedHandler()
    knowledge_base_sorted_handler.open()


def close_knowledge_base():
    if knowledge_base_sorted_handler and not knowledge_base_sorted_handler.is_closed():
        knowledge_base_sorted_handler.close()
