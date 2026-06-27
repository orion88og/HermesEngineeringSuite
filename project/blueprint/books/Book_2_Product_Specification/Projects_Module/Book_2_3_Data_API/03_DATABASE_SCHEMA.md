# Initial Database Schema

Table: projects
- id (UUID)
- name
- description
- status
- owner_id
- created_at
- updated_at
- archived_at

Table: tasks
- id
- project_id (FK)
- title
- status
- priority
- assignee_id
- due_date

Indexes:
- projects(status)
- tasks(project_id,status)
