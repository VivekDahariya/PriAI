import re

from app.compiler.concept_models import (
    ConceptNode,
    ConceptRelation
)

from app.compiler.models import KnowledgeUnit


class ConceptRelationBuilder:


    def __init__(self):

        self.rules = [

            (
                re.compile(
                    r"(.+?) requires (.+)",
                    re.IGNORECASE
                ),
                "requires",
                0.95,
                0.90
            ),

            (
                re.compile(
                    r"(.+?) uses (.+)",
                    re.IGNORECASE
                ),
                "uses",
                0.90,
                0.85
            ),

            (
                re.compile(
                    r"(.+?) is part of (.+)",
                    re.IGNORECASE
                ),
                "part_of",
                0.95,
                0.90
            ),

            (
                re.compile(
                    r"(.+?) belongs to (.+)",
                    re.IGNORECASE
                ),
                "belongs_to",
                0.95,
                0.90
            ),

            (
                re.compile(
                    r"(.+?) depends on (.+)",
                    re.IGNORECASE
                ),
                "depends_on",
                0.90,
                0.85
            ),

            (
                re.compile(
                    r"(.+?) trained by (.+)",
                    re.IGNORECASE
                ),
                "trained_by",
                0.90,
                0.85
            ),

            (
                re.compile(
                    r"(.+?) optimized by (.+)",
                    re.IGNORECASE
                ),
                "optimized_by",
                0.90,
                0.85
            )

        ]



    def normalize(
        self,
        text: str
    ):

        return (
            text
            .lower()
            .strip()
        )



    def build_lookup(
        self,
        concepts: list[ConceptNode]
    ):

        lookup = {}


        for concept in concepts:


            names = [

                concept.name

            ] + concept.aliases


            for name in names:

                lookup[
                    self.normalize(name)
                ] = concept.id


        return lookup



    def find_concepts_in_text(
        self,
        text: str,
        concepts: list[ConceptNode]
    ):

        found = []


        normalized = self.normalize(
            text
        )


        for concept in concepts:


            names = [

                concept.name

            ] + concept.aliases


            for name in names:


                if self.normalize(name) in normalized:

                    found.append(
                        concept
                    )

                    break


        return found



    def build(
        self,
        concepts: list[ConceptNode],
        chunks: list[KnowledgeUnit]
    ):


        concept_lookup = self.build_lookup(
            concepts
        )


        relations = []

        relation_keys = set()



        # ---------------------------------
        # Strong Explicit Relations
        # ---------------------------------

        for chunk in chunks:


            text = chunk.text


            for pattern, relation_name, weight, confidence in self.rules:


                match = pattern.search(
                    text
                )


                if not match:

                    continue



                left = self.normalize(
                    match.group(1)
                )

                right = self.normalize(
                    match.group(2)
                )


                source = concept_lookup.get(
                    left
                )


                target = concept_lookup.get(
                    right
                )


                if not source or not target:

                    continue


                key = (

                    source,

                    target,

                    relation_name

                )


                if key in relation_keys:

                    continue


                relation_keys.add(
                    key
                )


                relations.append(

                    ConceptRelation(

                        source=source,

                        target=target,

                        relation=relation_name,

                        weight=weight,

                        confidence=confidence

                    )

                )



        # ---------------------------------
        # Weak Co-occurrence Relations
        # ---------------------------------

        for chunk in chunks:


            mentioned = self.find_concepts_in_text(

                chunk.text,

                concepts

            )


            if len(mentioned) < 2:

                continue



            for i in range(
                len(mentioned)
            ):

                for j in range(
                    i + 1,
                    len(mentioned)
                ):


                    source = mentioned[i]

                    target = mentioned[j]


                    key = (

                        source.id,

                        target.id,

                        "related_to"

                    )


                    reverse_key = (

                        target.id,

                        source.id,

                        "related_to"

                    )


                    if (
                        key in relation_keys
                        or
                        reverse_key in relation_keys
                    ):

                        continue



                    relation_keys.add(
                        key
                    )


                    relations.append(

                        ConceptRelation(

                            source=source.id,

                            target=target.id,

                            relation="related_to",

                            weight=0.50,

                            confidence=0.60

                        )

                    )


        return relations