# Password Recovery Service

This microservice handles password reset requests via email token generation and validation.

## 🚀 Tech Stack

- **Language:** Python 3.11
- **Framework:** FastAPI
- **Database:** MongoDB 6
- **Containerized with:** Docker & Docker Compose
- **Testing:** Pytest
- **CI/CD:** GitHub Actions

## 📦 Features

- Request password recovery token
- Validate token and reset password
- Store tokens in MongoDB
- Stateless token generation
- RESTful API with Swagger UI

## 🔧 API Endpoints

| Method | Endpoint               | Description              |
|--------|------------------------|--------------------------|
| POST   | `/recovery/request`    | Request recovery token   |
| POST   | `/recovery/reset`      | Reset password           |

## ⚙️ Environment Variables

```env
MONGO_URL=mongodb://recovery-db:27017/
```

## 🐳 Docker

```bash
docker-compose up -d password-recovery-service recovery-db
```

Swagger UI: [http://localhost:8087/docs](http://localhost:8087/docs)

## ✅ Tests

```bash
pytest
```
