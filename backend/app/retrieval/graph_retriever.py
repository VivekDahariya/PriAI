import json
from pathlib import Path


class GraphRetriever:

    def __init__(self):

        self.relations_dir = Path("database/relations")

    def expand(
        self,
        ai_id: str,
        node_ids: list[str],
        hops: int = 1
    ):

        relation_file = self.relations_dir / f"{ai_id}.json"

        if not relation_file.exists():
            return []

        with relation_file.open("r") as f:
            relations = json.load(f)

        visited = set(node_ids)
        frontier = set(node_ids)

        for _ in range(hops):

            next_frontier = set()

            for relation in relations:

                if relation["source"] in frontier:

                    target = relation["target"]

                    if target not in visited:

                        visited.add(target)
                        next_frontier.add(target)

                if relation["target"] in frontier:

                    source = relation["source"]

                    if source not in visited:

                        visited.add(source)
                        next_frontier.add(source)

            frontier = next_frontier

        return list(visited)