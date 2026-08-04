from enum import Enum


class RelationType(str, Enum):

    NEXT = "next"

    CONTAINS = "contains"

    DEPENDS_ON = "depends_on"

    EXPLAINS = "explains"

    RELATED = "related"