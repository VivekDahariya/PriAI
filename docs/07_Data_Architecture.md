# Data Architecture

**Status:** Approved (Version 1)

**Version:** 1.0

---

# Purpose

This document defines how PriAI stores, organizes, and manages data.

The objective is to ensure that every AI created by a user remains isolated, maintainable, and efficient while preserving privacy and enabling offline operation.

This document focuses on logical data organization rather than implementation details.

---

# Data Architecture Overview

PriAI stores all information locally on the user's device.

Each AI is treated as an independent project with its own documents, processed knowledge, configuration, and conversation history.

No data is shared between different AIs unless explicitly supported in future versions.

---

# Storage Structure

A simplified logical structure is shown below.

```
PriAI/
│
├── Config/
│   ├── settings
│   └── preferences
│
├── Models/
│
├── AI_Projects/
│   │
│   ├── Computer Science AI/
│   │   ├── Documents/
│   │   ├── Processed/
│   │   ├── Index/
│   │   ├── Chats/
│   │   └── Metadata
│   │
│   ├── JEE Physics AI/
│   │   ├── Documents/
│   │   ├── Processed/
│   │   ├── Index/
│   │   ├── Chats/
│   │   └── Metadata
│   │
│   └── ...
│
└── Logs/
```

Each AI remains completely independent.

---

# Data Categories

PriAI manages five major categories of data.

---

## 1. AI Metadata

Metadata describes an AI project.

Examples include:

- AI Name
- Description
- Creation Date
- Last Build Time
- Number of Documents
- Version
- Status

Metadata allows PriAI to display and manage AI projects efficiently.

---

## 2. Original Documents

Uploaded files are preserved.

Examples:

- PDF
- TXT

Future versions:

- DOCX
- PPTX
- Images
- Audio
- Video

Keeping originals allows rebuilding without requiring users to upload files again.

---

## 3. Processed Knowledge

After processing, extracted knowledge is stored separately from the original documents.

Examples include:

- Cleaned text
- Chunks
- Processing metadata

Separating processed data avoids repeating expensive preprocessing.

---

## 4. Knowledge Index

The searchable knowledge representation is stored independently.

Responsibilities include:

- Fast retrieval
- Semantic search
- Source mapping

Each AI owns its own knowledge index.

---

## 5. Chat History

Each AI maintains its own conversations.

Each conversation contains:

- User Question
- AI Response
- Sources
- Timestamp

Future versions may support conversation search.

---

# Data Isolation

Every AI is isolated.

For example:

Computer Science AI

cannot access

JEE Physics AI

Likewise,

Company Documentation AI

cannot access

Personal Notes AI.

This isolation improves:

- Privacy
- Organization
- Retrieval quality
- Scalability

---

# Data Lifecycle

Every piece of knowledge follows the same lifecycle.

Upload

↓

Store Original

↓

Process

↓

Create Chunks

↓

Build Knowledge Index

↓

Answer Questions

↓

Optional Rebuild

↓

Delete

Deleting an AI removes all associated data.

---

# Privacy

Version 1 follows a local-first approach.

User knowledge remains on the local device.

No uploaded knowledge is transmitted to external servers during normal operation.

---

# Backup Strategy

Version 1 does not include automatic cloud backup.

Users remain responsible for backing up their AI projects.

Future versions may introduce:

- Export AI
- Import AI
- Cloud Backup
- Synchronization

---

# Future Data Expansion

The architecture should support future storage of:

- OCR results
- Image embeddings
- Audio transcripts
- Video transcripts
- Website snapshots
- Multiple language indexes

These additions should integrate without restructuring existing projects.

---

# Engineering Outcome

After reading this document, developers should understand:

- How PriAI organizes data.
- The relationship between AI projects and their knowledge.
- The separation of original and processed data.
- How conversations are stored.
- How future storage requirements can be accommodated.