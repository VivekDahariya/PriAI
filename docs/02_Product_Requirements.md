# Product Requirements

**Status:** Approved (v1 MVP)

**Version:** 1.0

---

# Purpose

This document defines the functional and non-functional requirements for PriAI Version 1 (MVP).

Its purpose is to establish a clear scope before implementation begins so that development remains focused on solving the core problem instead of continuously adding features.

After reading this document, any developer should understand exactly what PriAI v1 is expected to do and what is intentionally left for future versions.

---

# Product Overview

PriAI is a desktop application that enables users to build their own domain-specific AI assistants from their personal knowledge.

Users upload study material such as PDFs, text files, books, notes, and other supported documents.

PriAI processes the uploaded knowledge, builds a local searchable knowledge base, and creates an AI assistant capable of answering questions using only the imported information.

The resulting AI works privately on the user's device and does not require an internet connection after the knowledge has been built.

PriAI is not intended to compete with general-purpose AI assistants.

Instead, it allows users to transform their own knowledge into an AI.

---

# Goals

PriAI Version 1 aims to:

- Allow users to create multiple domain-specific AI assistants.
- Enable private and offline question answering.
- Provide source-grounded responses whenever possible.
- Minimize hallucinations by restricting answers to uploaded knowledge.
- Build a simple and intuitive user experience.
- Create a strong technical foundation for future versions.

---

# Non-Goals

The following features are intentionally excluded from Version 1:

- Cloud synchronization
- User accounts
- Multi-user collaboration
- Mobile applications
- Live internet search
- Daily news and real-time information
- Voice conversations
- AI-generated internet research
- Online model training

These may be introduced in future versions.

---

# Target Users

PriAI is designed for users who work with stable knowledge domains.

Examples include:

- Engineering students
- JEE / NEET / UPSC aspirants
- Researchers
- Teachers
- Software developers
- Companies with internal documentation
- Lawyers
- Medical professionals
- Technical writers
- Anyone maintaining a personal knowledge base

---

# Functional Requirements

## AI Management

The system shall allow users to:

- Create a new AI
- Name an AI
- View all created AIs
- Delete an AI
- Rebuild an AI after adding or removing knowledge

---

## Knowledge Import

The system shall allow users to import:

Version 1

- PDF (Text-based)
- TXT

Future Versions

- DOCX
- PPTX
- Images
- Audio
- Video
- Websites

---

## AI Building

The system shall:

- Read uploaded files
- Extract text
- Process knowledge
- Build a searchable knowledge index
- Save the completed AI locally
- Display build progress

---

## Question Answering

The system shall:

- Accept natural language questions
- Search only uploaded knowledge
- Generate answers using retrieved information
- Display supporting source references
- Inform users when the answer cannot be derived from available knowledge

---

## Knowledge Management

Users shall be able to:

- View imported documents
- Remove documents
- Rebuild the AI after changes

---

# Non-Functional Requirements

## Privacy

All user knowledge should remain on the local device whenever possible.

---

## Offline Capability

After the AI has been built, no internet connection should be required for normal usage.

---

## Performance

Normal question answering should feel responsive.

Knowledge processing may take longer but should occur only during AI creation or rebuilding.

---

## Reliability

The system should prioritize correctness over creativity.

When uncertain, PriAI should clearly indicate that sufficient information is unavailable.

---

## Usability

A first-time user should be able to build their first AI without reading documentation.

---

# MVP Scope

Version 1 includes:

✅ Create AI

✅ Import PDF and TXT

✅ Build AI

✅ Chat with AI

✅ Source citations

✅ Offline usage

✅ AI management

Everything else is postponed until later releases.

---

# Future Scope

Potential future features include:

- OCR support
- Image understanding
- Audio processing
- Video processing
- Website import
- Cloud backup
- Mobile application
- AI sharing
- Team workspaces
- Knowledge synchronization
- Plugin ecosystem
- Multi-model support

---

# Success Metrics

Version 1 will be considered successful if users can:

- Build an AI from their own documents.
- Ask natural language questions.
- Receive accurate answers grounded in uploaded knowledge.
- Trust that answers originate from their own data.
- Continue using the AI without an internet connection.

---

# Engineering Outcome

After reading this document, a developer should understand:

- What PriAI Version 1 includes.
- What is intentionally excluded.
- The core functionality of the application.
- The primary users of the system.
- The quality expectations for the MVP.