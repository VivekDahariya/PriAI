# Tech Stack

**Status:** Approved (Version 1)

**Version:** 1.0

---

# Purpose

This document defines the technologies selected for PriAI Version 1.

The goal is to build a modern, maintainable, cross-platform desktop application capable of creating private, offline, domain-specific AI assistants.

Technology choices prioritize developer experience, performance, maintainability, and future scalability.

---

# Technology Overview

| Layer | Technology |
|--------|------------|
| Desktop Application | Electron |
| Frontend | React |
| Language | TypeScript |
| Build Tool | Vite |
| Styling | Tailwind CSS |
| Backend Runtime | Node.js |
| AI Processing | Python |
| Local API | FastAPI |
| Document Processing | Python Libraries |
| Local Database | SQLite |
| AI Models | Ollama (Local LLMs) |
| Embedding Models | Local Embedding Models |
| Version Control | Git |
| Repository Hosting | GitHub |

---

# Desktop Application

## Electron

Electron provides the desktop application shell.

Reasons:

- Cross-platform
- Mature ecosystem
- Strong community support
- Native desktop capabilities
- Easy integration with React

---

# Frontend

## React

React is responsible for the complete user interface.

Reasons:

- Component-based architecture
- Fast development
- Large ecosystem
- Excellent TypeScript support

---

## TypeScript

TypeScript provides static typing across the frontend.

Benefits:

- Better maintainability
- Improved IDE support
- Reduced runtime errors
- Easier refactoring

---

## Vite

Vite is used as the frontend build tool.

Reasons:

- Fast startup
- Fast hot reload
- Modern tooling
- Excellent React integration

---

## Tailwind CSS

Tailwind CSS is responsible for styling.

Reasons:

- Rapid UI development
- Consistent design system
- Utility-first approach
- Easy maintenance

---

# Backend

## Node.js

Node.js coordinates the application.

Responsibilities include:

- AI management
- File handling
- Communication between frontend and AI services
- Application logic

---

## FastAPI

Python services are exposed through FastAPI.

Responsibilities include:

- Document processing
- Embedding generation
- Knowledge retrieval
- AI inference

Separating Python from the application backend keeps AI logic modular.

---

# AI Layer

PriAI uses locally running language models.

Version 1 targets compatibility with Ollama-supported models.

Benefits include:

- Offline operation
- Privacy
- Model flexibility
- Easy replacement of models

---

# Document Processing

Python is responsible for document processing.

Tasks include:

- Reading PDFs
- Reading text files
- Text extraction
- Text cleaning
- Chunk generation

Future versions may support additional document types.

---

# Local Storage

## SQLite

SQLite stores structured application data.

Examples include:

- AI metadata
- Configuration
- Chat history
- User preferences

SQLite requires no installation and is well suited for local desktop applications.

---

# Knowledge Storage

Knowledge generated during AI creation is stored locally.

Stored data includes:

- Processed text
- Embeddings
- Knowledge indexes
- Metadata

Each AI maintains its own isolated knowledge base.

---

# Development Tools

Development will primarily use:

- Visual Studio Code
- Git
- GitHub
- npm
- Python virtual environments

---

# Why This Stack?

The selected technologies provide:

- Cross-platform compatibility
- Offline capability
- Modern development workflow
- Modular architecture
- Strong community support
- Easy future expansion

The stack also allows independent evolution of the frontend, backend, and AI components.

---

# Future Technology Considerations

Future versions may evaluate:

- Tauri
- Rust services
- PostgreSQL
- Cloud synchronization
- Mobile applications
- Distributed knowledge storage

These technologies are outside the scope of Version 1.

---

# Engineering Outcome

After reading this document, developers should understand:

- The complete technology stack.
- The responsibility of each technology.
- Why each technology was selected.
- How the technologies interact.
- The intended direction for future evolution.