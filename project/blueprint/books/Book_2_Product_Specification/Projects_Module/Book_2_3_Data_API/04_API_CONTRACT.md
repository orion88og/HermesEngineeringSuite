# API Contract

GET    /api/v1/projects
POST   /api/v1/projects
GET    /api/v1/projects/{id}
PATCH  /api/v1/projects/{id}
DELETE /api/v1/projects/{id}

GET    /api/v1/projects/{id}/tasks
POST   /api/v1/projects/{id}/tasks

Response format:
{
  "data": ...,
  "meta": ...,
  "errors": []
}
