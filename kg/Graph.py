'''实例化知识图谱对象'''
from config.config import Config
from py2neo import Graph, NodeMatcher, RelationshipMatcher, ConnectionUnavailable

class GraphDao(object):
    pass  # TODO: implement

    def __init__(self):
        pass  # TODO: implement



    def ensure_connection(function):
        pass  # TODO: implement
        def wrapper(*args, **kwargs):
            pass  # TODO: implement


    def __connect_graph(self):
        pass  # TODO: implement
    def query_relationship_by_name(self, entity_name: str):
        pass  # TODO: implement
    def query_node(self, *label, **properties):
        pass  # TODO: implement
