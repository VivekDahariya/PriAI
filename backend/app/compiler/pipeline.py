from .parser import Parser
from .hierarchy_builder import HierarchyBuilder
from .metadata_inheritor import MetadataInheritor
from .dictionary_encoder import DictionaryEncoder
from .knowledge_builder import KnowledgeBuilder
from .relation_builder import RelationBuilder
from .embedding_builder import EmbeddingBuilder
from .storage_builder import StorageBuilder


class KnowledgeCompiler:

    def __init__(self):

        self.parser = Parser()

        self.hierarchy = HierarchyBuilder()

        self.inheritor = MetadataInheritor()

        self.dictionary = DictionaryEncoder()

        self.builder = KnowledgeBuilder()

        self.relations = RelationBuilder()

        self.embedding = EmbeddingBuilder()

        self.storage = StorageBuilder()