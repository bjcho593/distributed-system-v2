# Profile Service

This microservice is responsible for managing user profile information such as name, bio, and email. It is part of the **Authentication Domain** in the distributed system project.

## 🚀 Tech Stack

- **Language:** Python 3.11
- **Framework:** FastAPI
- **Database:** MongoDB 6
- **Containerized with:** Docker & Docker Compose
- **Testing:** Pytest
- **CI/CD:** GitHub Actions

## 📦 Features

- Create a new user profile
- Retrieve a profile by `user_id`
- MongoDB-backed storage
- RESTful API with Swagger UI

## 🔧 API Endpoints

| Method | Endpoint              | Description             |
|--------|-----------------------|-------------------------|
| POST   | `/profile/`           | Create a new profile    |
| GET    | `/profile/{user_id}`  | Retrieve a profile      |

### Example Request (POST `/profile/`)

```json
{
  "user_id": "u123",
  "name": "John Doe",
  "bio": "Backend developer",
  "email": "john@example.com"
}
