---
title: GDD Agents
type: docs
weight: 99
aliases:
  - /gdd_agents.html
  - /GDD_Agents.html
---

# AI Agent Guidelines

This section provides **rules, workflows, skills, and knowledge references** for AI coding agents (Gemini, Copilot, Cursor, etc.) working on this project. These documents ensure that AI-generated code and documentation are consistent with our standards.

> **Key Principle:** AI agents must produce code and documentation that is indistinguishable from human-written work. All output must follow the project's coding standards, naming conventions, and architecture patterns.

***

## Document Groups

### Rules

Mandatory constraints and standards that agents must follow in every interaction.

* [**Code Generation Rules**](Rules/CodeGeneration.md) — C++ code generation constraints, UE5 patterns, UPROPERTY/UFUNCTION usage
* [**Documentation Standards**](Rules/DocumentationStandards.md) — Markdown formatting, GDD structure, language, and image placeholders

***

### Workflows

Step-by-step procedures for common development tasks.

* [**Feature Implementation**](Workflows/FeatureImplementation.md) — End-to-end workflow for adding a new gameplay feature
* [**Bug Fix Workflow**](Workflows/BugFix.md) — Systematic approach to diagnosing and fixing bugs

***

### Skills

Specialized competencies and UE5-specific knowledge for agents.

* [**Unreal Engine Skills**](Skills/UnrealEngine.md) — UE5-specific patterns, GAS, Enhanced Input, replication, UMG

***

### Knowledge Sources

Reference documentation and key links for research.

* [**Source References**](Knowledge/SourceReferences.md) — Official docs, style guides, GDC talks, and community resources

***

## Related Standards

Agents **must** read and follow these documents before generating any code or documentation:

| Document                     | Path                                                               | Priority  |
| ---------------------------- | ------------------------------------------------------------------ | --------- |
| **Coding & Asset Standards** | [CodingStandards.md](../GDD_Technical/CodingStandards.md)          | CRITICAL  |
| **GDD Documentation Guide**  | [GDD\_Documentation\_Guide.md](/broken/pages/TB2kA98NBUMqvdPpAsVj) | HIGH      |
| **GDD Technical Index**      | [GDD\_Technical/\_index.md](../GDD_Technical/_index.md)            | HIGH      |
| **GDD Design Index**         | [GDD\_Design/\_index.md](../GDD_Design/_index.md)                  | REFERENCE |
