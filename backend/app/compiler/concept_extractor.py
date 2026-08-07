import re


class ConceptExtractor:

    """
    Simple rule-based concept extractor.

    Later this will be replaced by
    NLP / LLM extraction.
    """

    STOPWORDS = {

        "the",
        "a",
        "an",
        "is",
        "are",
        "was",
        "were",
        "this",
        "that",
        "these",
        "those",
        "of",
        "to",
        "for",
        "and",
        "or",
        "in",
        "on",
        "by",
        "with",
        "using",
        "used"

    }

    def extract(
        self,
        text: str
    ) -> list[str]:

        candidates = re.findall(

            r"[A-Za-z][A-Za-z0-9#+.-]*(?:\s+[A-Za-z][A-Za-z0-9#+.-]*)*",

            text

        )

        concepts = []

        for phrase in candidates:

            phrase = phrase.strip()

            if len(phrase) < 3:
                continue

            if phrase.lower() in self.STOPWORDS:
                continue

            concepts.append(
                phrase
            )

        return list(
            dict.fromkeys(concepts)
        )