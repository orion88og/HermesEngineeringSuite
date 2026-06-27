# Database Design
Core entities:
Project(id,name,status,owner,start_date,end_date)
Milestone
Task
Requirement
Risk
Decision
Document
Relationships:
Project owns all subordinate entities.
Soft delete for archival.
