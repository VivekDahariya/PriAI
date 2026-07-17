# User Journey

**Status:** Approved (Version 1)

**Version:** 1.0

---

# Purpose

This document describes the complete user journey through PriAI Version 1.

Its objective is to ensure that every interaction feels simple, intuitive, and predictable.

After reading this document, a designer or developer should understand exactly how users interact with PriAI from launching the application to chatting with their own AI assistant.

---

# User Journey Overview

The complete PriAI workflow consists of six stages:

1. Launch PriAI
2. Create a New AI
3. Upload Knowledge
4. Build the AI
5. Chat with the AI
6. Manage Existing AIs

---

# Journey 1 — Launch PriAI

## Goal

Allow users to immediately access their existing AI assistants or create a new one.

## User Experience

When PriAI opens, the user sees:

- Application Logo
- Tagline
- "Build New AI" button
- List of existing AI assistants

If no AI exists:

Display an empty state encouraging users to create their first AI.

---

# Journey 2 — Create a New AI

## Goal

Create a new domain-specific AI.

## User Actions

User clicks:

Build New AI

The application asks for:

- AI Name
- Short Description (Optional)

Example:

AI Name

Computer Science AI

Description

Semester Notes and Books

User clicks Continue.

---

# Journey 3 — Upload Knowledge

## Goal

Allow users to import the knowledge that their AI should learn.

Supported in Version 1:

- PDF
- TXT

Future versions will support:

- DOCX
- PPTX
- Images
- Audio
- Video
- Websites

Users may:

- Drag and Drop files
- Browse Files

The application displays:

- File Name
- File Size
- Number of Files
- Remove File option

User clicks:

Build AI

---

# Journey 4 — Build AI

## Goal

Transform uploaded documents into a searchable AI.

During this process PriAI:

- Reads documents
- Extracts text
- Cleans the data
- Creates embeddings
- Builds the knowledge index
- Saves the completed AI

The user sees:

- Progress Bar
- Current Step
- Estimated Progress

When complete:

Display:

✅ AI Built Successfully

Open AI

---

# Journey 5 — Chat with AI

## Goal

Allow users to ask questions naturally.

Users type questions into the chat box.

Example:

Explain JVM in Java.

PriAI:

- Searches uploaded knowledge
- Retrieves relevant information
- Generates an answer
- Shows supporting sources

Example:

Source

Java Complete Reference

Page 143

If information is unavailable:

PriAI replies:

"This question cannot be answered using the current knowledge available in this AI."

PriAI should never invent unsupported information.

---

# Journey 6 — Manage AI

Users can:

- Open AI
- Rename AI
- View imported documents
- Delete documents
- Add more documents
- Rebuild AI
- Delete AI

---

# Error Handling

Examples include:

No files selected.

Unsupported file type.

Corrupted PDF.

Build failed.

Storage full.

Question outside knowledge scope.

Every error should explain:

- What happened
- Why it happened
- How the user can fix it

---

# Design Principles

Every interaction should be:

- Simple
- Predictable
- Fast
- Transparent
- Beginner Friendly

Users should never need technical AI knowledge to use PriAI.

---

# Engineering Outcome

After reading this document, developers should understand:

- The complete user workflow.
- Every major screen required.
- User actions on each screen.
- Expected system responses.
- Error handling requirements.