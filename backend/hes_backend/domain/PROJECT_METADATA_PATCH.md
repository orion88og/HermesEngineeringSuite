Update project.py by introducing optional metadata fields:

- project_number: str | None
- customer: str | None
- lead_engineer: str | None
- location: str | None
- priority: int = 0

Add setter methods:

- set_project_number()
- set_customer()
- set_lead_engineer()
- set_location()
- set_priority()

Each setter should:
- validate simple input (non-empty where appropriate)
- update the field
- call touch()

Do not add business rules beyond basic validation in this package.
