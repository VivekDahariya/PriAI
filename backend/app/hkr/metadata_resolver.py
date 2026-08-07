class MetadataResolver:


    def __init__(self, manager):

        self.manager = manager



    def resolve(self, node_id):

        metadata = {}

        lineage = []


        current = node_id


        while current:

            node = self.manager.get_node(current)


            if not node:
                break


            lineage.append(node)


            current = node.parent_id



        # Parent first, child last
        # Child overrides parent

        for node in reversed(lineage):

            for key,value in node.metadata.items():

                metadata[key] = value



        return metadata