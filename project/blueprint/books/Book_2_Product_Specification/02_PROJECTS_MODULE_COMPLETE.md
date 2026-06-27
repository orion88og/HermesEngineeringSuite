# Projects Module Specification
**Document ID:** HES-BP-221
**Status:** Draft (Living)

# Purpose
The Projects module is the primary organizing domain of HES. Every engineering
artifact belongs to a project.

# Goals
- Organize engineering work from idea to archive.
- Provide a single source of truth for project status.
- Integrate documents, AI conversations, CAD, manufacturing, networking,
business records, and automation.

# Core Entities
- Project
- Milestone
- Task
- Requirement
- Decision
- Risk
- Document
- Asset
- Contact
- Change Log

# Lifecycle
Idea → Planning → Active Development → Validation → Production → Maintenance → Archived

# Functional Requirements
## Project Management
- Create, edit, archive, clone projects.
- Templates for common project types.
- Custom metadata and tags.

## Planning
- Milestones
- Kanban and list views
- Dependencies
- Priorities
- Time estimates

## Documentation
- Link notes, PDFs, images, CAD files, BOMs and specifications.
- Version history.

## AI Integration
- Project-aware chat.
- Automatic context assembly.
- Summaries.
- Action item generation.

## Search
- Global search scoped to project.
- Full-text search.
- Tag and metadata filters.

# User Roles
Administrator
Engineer
Contributor
Viewer

# Dashboard
Displays:
- Active milestones
- Recent activity
- Open risks
- AI insights
- Pending tasks
- Recent documents

# API (Initial)
GET /projects
POST /projects
GET /projects/{id}
PATCH /projects/{id}
DELETE /projects/{id}
GET /projects/{id}/tasks
GET /projects/{id}/documents

# Data Relationships
Project owns:
Tasks
Milestones
Requirements
Documents
AI Sessions
Manufacturing Jobs
Network Assets
Business Records

# Acceptance Criteria
- CRUD operations work.
- Project dashboard loads.
- Search returns project assets.
- AI uses project context.
- Audit history recorded.

# Roadmap
MVP:
Projects, tasks, milestones, documents.
Later:
Gantt charts, resource planning, budgeting, portfolio management.

# Blueprint References
Book 2 Product Specification
Book 3 Architecture
Engineering Standards
