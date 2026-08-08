from copy import deepcopy


class MetadataResolver:


    def __init__(self, tree):

        self.tree = tree



    def resolve(
        self,
        node_id,
        key
    ):

        current = self.tree.get_node(
            node_id
        )


        while current:

            if key in current.metadata:

                return current.metadata[key]


            current = self.tree.get_parent(
                current.id
            )


        return None



    def resolve_all(
        self,
        node_id
    ):

        current = self.tree.get_node(
            node_id
        )


        chain = []


        while current:

            chain.append(
                current
            )

            current = self.tree.get_parent(
                current.id
            )


        resolved = {}


        # Parent first, child last
        for node in reversed(chain):

            resolved.update(
                deepcopy(
                    node.metadata
                )
            )


        return resolved