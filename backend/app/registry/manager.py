import json
import os


class RegistryManager:

    def __init__(self):

        self.path = "registry.json"

        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump([], f, indent=4)

    def _load(self):

        with open(self.path, "r") as f:
            return json.load(f)

    def _save(self, data):

        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def register(
        self,
        ai_id,
        name,
        documents,
        chunks,
        knowledge_density,
        suggested_top_k,
        suggested_threshold
    ):

        registry = self._load()

        registry = [
            ai for ai in registry
            if ai["id"] != ai_id
        ]

        from datetime import datetime

        registry.append(
            {
                "id": ai_id,
                "name": name,
                "documents": documents,
                "chunks": chunks,
                "created_at": datetime.now().isoformat(),
                "knowledge_density": knowledge_density,
                "suggested_top_k": suggested_top_k,
                "suggested_threshold": suggested_threshold
            }
        )

        self._save(registry)

    def get_ai(self, ai_id):

        registry = self._load()

        for ai in registry:

            if ai["id"] == ai_id:
                return ai

        return None

    def list_all(self):

        return self._load()

    def delete(self, ai_id):

        registry = self._load()

        registry = [
            ai for ai in registry
            if ai["id"] != ai_id
        ]

        self._save(registry)