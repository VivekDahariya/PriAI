import re

from .models import KnowledgeRelation


RELATION_WEIGHTS = {

    "next": 0.7,

    "trained_by": 0.95,
    "trained_using": 0.95,

    "optimized_by": 0.9,
    "optimizes": 0.9,

    "depends_on": 0.9,

    "requires": 0.85,

    "uses": 0.85,

    "contains": 0.8,
    "part_of": 0.8,

    "is_a": 0.9,
    "example_of": 0.85,

    "called": 0.75,
    "alias": 0.75

}


class RelationBuilder:

    def build(self, units):

        relations = []

        seen = set()


        # --------------------------------
        # Structural document order edges
        # --------------------------------

        for i in range(len(units) - 1):

            relation = KnowledgeRelation(

                source=units[i].hkr_node_id,

                relation="next",

                target=units[i + 1].hkr_node_id,

                weight=RELATION_WEIGHTS["next"],

                confidence=1.0,

                source_type="chunk",

                target_type="chunk"

            )


            key = (
                relation.source,
                relation.relation,
                relation.target
            )


            if key not in seen:

                relations.append(relation)

                seen.add(key)



        # --------------------------------
        # Semantic relationship patterns
        # --------------------------------

        patterns = [

            (r"\bare trained using\b", "trained_by"),
            (r"\bare trained by\b", "trained_by"),
            (r"\btrained using\b", "trained_by"),
            (r"\btrained by\b", "trained_by"),


            (r"\boptimizes\b", "optimizes"),
            (r"\boptimized by\b", "optimized_by"),


            (r"\buses\b", "uses"),

            (r"\bcontains\b", "contains"),
            (r"\bconsists of\b", "contains"),

            (r"\bpart of\b", "part_of"),

            (r"\bdepends on\b", "depends_on"),

            (r"\brequires\b", "requires"),


            (r"\bcalled\b", "called"),
            (r"\bknown as\b", "alias"),


            (r"\bis a type of\b", "is_a"),

            (r"\bis an example of\b", "example_of"),

        ]



        for unit in units:

            text = unit.text.strip()


            for pattern, relation_name in patterns:


                match = re.search(
                    pattern,
                    text,
                    flags=re.IGNORECASE
                )


                if not match:

                    continue



                left = text[:match.start()].strip(
                    " .,:;()"
                )


                right = text[match.end():].strip(
                    " .,:;()"
                )



                # Remove helper verbs from left side

                for suffix in [

                    " are",
                    " is",
                    " was",
                    " were",
                    " has",
                    " have",

                ]:

                    if left.lower().endswith(suffix):

                        left = left[:-len(suffix)].strip()



                if not left or not right:

                    continue



                relation = KnowledgeRelation(

                    source=unit.hkr_node_id,

                    relation=relation_name,

                    target=right,

                    weight=RELATION_WEIGHTS.get(
                        relation_name,
                        0.5
                    ),

                    confidence=0.8,

                    source_type="chunk",

                    target_type="concept"

                )



                key = (

                    relation.source,

                    relation.relation,

                    relation.target

                )



                if key not in seen:

                    relations.append(relation)

                    seen.add(key)



        return relations