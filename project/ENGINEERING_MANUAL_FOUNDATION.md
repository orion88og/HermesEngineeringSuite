# ENGINEERING_MANUAL_FOUNDATION.md

# HES Engineering Manual Foundation
Version: 1.0
Status: FROZEN
Authority: Project Constitution

## Purpose
This document is the governing constitution for the Hermes Engineering Suite (HES).
It defines the permanent engineering framework for the project.

No architectural, organizational, or workflow changes are made outside the ADR process.

---

# Frozen Decisions

## Repository Structure (FROZEN)

HermesEngineeringSuite/
    backend/
    frontend/
    tools/
    tests/

    project/
        PROJECT_MANIFEST.md
        MASTER_INDEX.md
        engineering-manual/
            foundation/
            volumes/
            modules/
            requirements/
            adr/
            templates/
            generated/
            diagrams/
            schemas/
            assets/

## Module Structure (FROZEN)

00 Charter
01 Functional Specification
02 UX Specification
03 Data Model
04 API Contract
05 Service Architecture
06 AI Integration
07 Security
08 Search
09 Notifications & Events
10 Reporting
11 Import / Export
12 Testing
13 Operations
14 Implementation Roadmap
15 ADRs
16 Requirements
17 Story Mapping
18 Glossary
19 Examples
20 Changelog

Every module follows this structure.

## Development Workflow (FROZEN)

Vision
→ Capability
→ Requirement
→ Module Specification
→ Story
→ Implementation
→ Testing
→ Documentation
→ Release

## Blueprint Rule (FROZEN)

The blueprint is the source of truth.
Implementation conforms to the blueprint.
The blueprint evolves only through approved ADRs.

## One Active Task Rule (FROZEN)

At any time there is exactly ONE active implementation task.
Complete it.
Commit it.
Advance the queue.

## Repository Governance Files

ENGINEERING_MANUAL_FOUNDATION.md
PROJECT_STATUS.md
IMPLEMENTATION_QUEUE.md
FUTURE_ENHANCEMENTS.md
PROJECT_MANIFEST.md
MASTER_INDEX.md

## Change Control

Architectural changes require:
1. ADR
2. Review
3. Approval
4. Blueprint update

Ideas that are not required for the current milestone are recorded in FUTURE_ENHANCEMENTS.md.

## Capability Order (FROZEN)

M0 Foundation
M1 Projects
M2 Knowledge
M3 AI Workspace
M4 Engineering
M5 Manufacturing
M6 Networking
M7 Business
M8 Automation
M9 Administration

Capabilities are completed in order unless an approved ADR changes the sequence.

## Definition of Done

Every completed story includes:
- Documentation updated
- Code implemented
- Tests passing
- Blueprint references updated
- Commit created

## Working Agreement

We optimize for completion rather than continual redesign.

The framework defined in this document is considered locked for HES 1.x.
