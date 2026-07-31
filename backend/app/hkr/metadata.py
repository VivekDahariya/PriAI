class MetadataResolver:


    def __init__(self, tree):

        self.tree = tree



    def resolve(self, node_id, key):

        current = self.tree.get_node(node_id)


        while current:

            if key in current.metadata:
                return current.metadata[key]


            current = self.tree.get_parent(current.id)


        return None