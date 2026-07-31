# Hierarchical Knowledge Representation (HKR)

## Vision

HKR is PriAI's knowledge organization architecture.

Its purpose is to reduce metadata duplication, improve storage efficiency,
and create a structured representation of knowledge where information can
inherit properties from parent nodes.

---

# Core Idea

Traditional RAG:

Chunk
 ├── Text
 ├── Author
 ├── Language
 ├── Topic
 ├── Publisher


HKR:

Book
 |
 ├── Metadata
 |
 ├── Chapter
 |      |
 |      ├── Metadata
 |      |
 |      └── Chunk
 |              |
 |              ├── Text
 |              ├── Embedding
 |              └── Local Metadata


Metadata is stored only where it originates.

Children inherit information from parents.

---

# Design Principles

## 1. Hierarchical Storage

Knowledge exists as a tree.

Every node has:

- id
- parent_id
- type
- metadata


## 2. Metadata Inheritance

Child nodes do not duplicate parent metadata.

Example:

Book:
Language = English Author = ABC
Chapter:
Topic = Machine Learning
Chunk:
Text only
A chunk can resolve:
Author Language Topic
by walking upward.

---

# Node Types

## Knowledge Base

Contains multiple sources.

---

## Source

Represents an uploaded document.

Example:
book.pdf lecture_notes.pdf website
Stores:

- filename
- author
- language
- publisher


---

## Section

Represents logical divisions.

Examples:

- Chapter
- Heading
- Topic


Stores:

- title
- position


---

## Chunk

The smallest retrieval unit.

Stores:
id parent_id text embedding
Only local information.

---

# Dictionary Engine

Repeated metadata values should be stored once.

Example:

Before:
Language = English Language = English Language = English
After:
LanguageID = 1
Dictionary:
1 -> English
---

# Future Components

## Compression Layer

Optimizes raw knowledge storage.

## Adaptive Retrieval Engine

Optimizes retrieval decisions.

## Relationship Engine

Stores explicit knowledge relationships.

---

# HKR API

Future interface:
create_node()
get_node()
get_parent()
get_children()
resolve_metadata()
store_dictionary_value()
get_dictionary_value()