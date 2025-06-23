# Auth Service

Microservice responsible for user authentication using Node.js, Express, and Redis.

## 🚀 Technologies

- Node.js (Express)
- Redis
- JWT (jsonwebtoken)
- Docker + Docker Compose

## 📦 Main Endpoints

- `POST /auth/register` – User registration
- `POST /auth/login` – Log in and return a JWT
- `GET /auth/status` – Check if the service is up

## ⚙️ Environment Variables

- `REDIS_HOST=redis`
- `REDIS_PORT=6379`
- `JWT_SECRET=superkey123`

## ▶️ How to run

```bash
docker-compose -f docker-compose.yml -f auth-service/docker-compose.override.yml up --build -d
```
