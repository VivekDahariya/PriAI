# UI / UX Specification

**Status:** Approved (Version 1)

**Version:** 1.0

---

# Purpose

This document defines every user-facing screen of PriAI Version 1.

It specifies the purpose, components, user interactions, navigation, and expected behavior of each screen.

The objective is to create a consistent, intuitive, and modern desktop experience.

---

# Design Principles

PriAI should feel:

- Clean
- Modern
- Fast
- Minimal
- Professional
- Beginner Friendly

Every screen should focus on the user's task and avoid unnecessary complexity.

---

# Navigation Structure

```
Home
│
├── Build New AI
│      │
│      ├── AI Details
│      ├── Upload Knowledge
│      ├── Build Progress
│      └── Build Complete
│
├── Open Existing AI
│      │
│      ├── Chat
│      ├── Documents
│      ├── Rebuild
│      └── Settings
│
└── Global Settings
```

---

# Screen 1 — Home

## Purpose

Provide access to all created AI assistants.

### Components

- PriAI Logo
- Tagline
- Build New AI button
- AI Cards
- Search AI (future)
- Settings button

### Actions

User can:

- Create AI
- Open AI
- Delete AI
- Rename AI

### Layout

```
-------------------------------------------------
 PriAI

 Transform Your Knowledge Into AI

 [+ Build New AI]

 -----------------------------------------------

 📘 Computer Science AI

 📗 JEE Advanced AI

 📙 Company Documentation

 -----------------------------------------------

                 Settings
-------------------------------------------------
```

---

# Screen 2 — Create AI

## Purpose

Collect basic information before importing knowledge.

### Components

- AI Name
- Description (Optional)
- Continue Button

### Validation

- AI Name required
- Name must be unique

---

# Screen 3 — Upload Knowledge

## Purpose

Allow users to import documents.

### Components

- Drag & Drop Area
- Browse Files
- Uploaded File List
- Remove File
- Build AI Button

Supported Formats:

Version 1

- PDF
- TXT

Future

- DOCX
- PPTX
- Images
- Audio
- Video

---

# Screen 4 — Building AI

## Purpose

Display progress while processing knowledge.

### Progress Steps

- Reading Documents
- Extracting Text
- Cleaning Data
- Creating Chunks
- Building Knowledge Index
- Finalizing AI

### Components

- Progress Bar
- Current Step
- Percentage
- Estimated Time (Optional)

The user cannot ask questions until the build is complete.

---

# Screen 5 — Chat

## Purpose

Primary interaction screen.

### Components

- Chat History
- Message Input
- Send Button
- Sources Panel
- AI Information Button

### Answer Layout

Question

↓

Answer

↓

Sources

- Document Name
- Page Number (if available)

---

# Screen 6 — Documents

## Purpose

Manage uploaded knowledge.

### Components

Document List

Each document displays:

- Name
- Size
- Date Added

### Actions

- Add Documents
- Remove Documents
- Rebuild AI

---

# Screen 7 — AI Settings

## Purpose

Manage a specific AI.

### Components

- AI Name
- Description
- Number of Documents
- Last Build
- Delete AI
- Rebuild AI

---

# Screen 8 — Application Settings

## Purpose

Configure PriAI.

### Components

- Theme
- Storage Location
- Installed Models
- About
- Version Information

Future versions may include additional preferences.

---

# Error States

Examples include:

No Documents Uploaded

↓

"Upload at least one supported document."

Unsupported File

↓

"This file type is not supported."

Question Outside Knowledge

↓

"This AI cannot answer the question using its current knowledge."

Build Failure

↓

"The AI could not be built. Please review the uploaded documents and try again."

---

# Design Guidelines

The interface should emphasize:

- Large readable typography
- Minimal clicks
- Clear progress feedback
- Consistent spacing
- Responsive layouts
- Accessible controls

Every primary action should be obvious without requiring instructions.

---

# Engineering Outcome

After reading this document, developers should understand:

- Every screen required in Version 1.
- Navigation between screens.
- Components present on each screen.
- User interactions.
- Expected application behavior.