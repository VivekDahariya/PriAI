import json
from pathlib import Path


class GraphRetriever:

    def __init__(self):

        self.relations_dir = Path(
            "database/relations"
        )


    def expand(
        self,
        ai_id: str,
        node_ids: list[str],
        hops: int = 1,
        max_nodes: int = 10
    ):

        relation_file = (
            self.relations_dir /
            f"{ai_id}.json"
        )


        if not relation_file.exists():

            return []


        with relation_file.open("r") as f:

            relations = json.load(f)



        visited = set(node_ids)

        results = []


        frontier = set(node_ids)



        for depth in range(1, hops + 1):

            next_frontier = set()


            for relation in relations:


                source = relation["source"]

                target = relation["target"]


                if source in frontier:

                    if target not in visited:

                        visited.add(target)

                        next_frontier.add(target)


                        results.append(

                            {
                                "node_id": target,
                                "distance": depth,
                                "relation": relation["relation"]
                            }

                        )


                if target in frontier:

                    if source not in visited:

                        visited.add(source)

                        next_frontier.add(source)


                        results.append(

                            {
                                "node_id": source,
                                "distance": depth,
                                "relation": relation["relation"]
                            }

                        )


            frontier = next_frontier


        return results[:max_nodes]