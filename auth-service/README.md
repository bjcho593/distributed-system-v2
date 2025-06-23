# Auth Service

Microservicio encargado de la autenticación de usuarios mediante Node.js, Express y Redis.

## 🚀 Tecnologías

- Node.js (Express)
- Redis
- JWT (jsonwebtoken)
- Docker + Docker Compose

## 📦 Endpoints principales

- `POST /auth/register` – Registro de usuarios
- `POST /auth/login` – Inicia sesión y devuelve un JWT
- `GET /auth/status` – Verifica si el servicio está activo

## ⚙️ Variables de entorno

- `REDIS_HOST=redis`
- `REDIS_PORT=6379`
- `JWT_SECRET=superclave123`

## ▶️ Cómo ejecutar

```bash
docker-compose -f docker-compose.yml -f auth-service/docker-compose.override.yml up --build -d
```
