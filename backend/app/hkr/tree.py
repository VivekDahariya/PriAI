from app.hkr.models import HKRNode


class HKRTree:

    def __init__(self):

        self.nodes = {}


    def add_node(self, node: HKRNode):

        self.nodes[node.id] = node


    def get_node(self, node_id):

        return self.nodes.get(node_id)


    def get_parent(self, node_id):

        node = self.get_node(node_id)

        if node and node.parent_id:
            return self.get_node(node.parent_id)

        return None