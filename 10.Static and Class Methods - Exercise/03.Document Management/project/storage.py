from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category:Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for cat in self.categories:
            if cat.id == category_id:
                cat.edit(new_name)
                break

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for topic in self.topics:
            if topic.id == topic_id:
                topic.edit(new_topic, new_storage_folder)
                break

    def edit_document(self, document_id: int, new_file_name: str):
        for doc in self.documents:
            if doc.id == document_id:
                doc.edit(new_file_name)
                break

    def delete_category(self, category_id):
        for cat in self.categories:
            if cat.id == category_id:
                self.categories.remove(cat)
                break

    def delete_topic(self, topic_id):
        for top in self.topics:
            if top.id == topic_id:
                self.topics.remove(top)
                break

    def delete_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                self.documents.remove(doc)
                break

    def get_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                return doc

    def __repr__(self):
        result = ""
        for doc in self.documents:
            result += f"{str(doc)}\n"
        return result[:-1]
