# Team Service

Microservice responsible for managing user teams. Implemented in Java with Spring Boot and PostgreSQL.

## 🚀 Technologies

- Java 17
-SpringBoot
- PostgreSQL
- Docker + Docker Compose

## 📦 Endpoints

- `GET /teams` – List teams
- `POST /teams` – Create new team
- `GET /teams/{id}` – Get details

## ⚙️ Environment variables

- `SPRING_DATASOURCE_URL=jdbc:postgresql://postgres:5432/usersdb`
- `SPRING_DATASOURCE_USERNAME=postgres`
- `SPRING_DATASOURCE_PASSWORD=SS29lose`

## ▶️ How to run

```bash
docker-compose -f docker-compose.yml -f team-service/docker-compose.override.yml up --build -d
```
