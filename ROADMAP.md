# ROADMAP – Backend de prácticas (FastAPI + SQLAlchemy)

## Objetivo

Construir un web service API RESTful con:

- FastAPI
- SQLAlchemy (Session / AsyncSession)
- Pydantic
- pytest (unitarios, integración, e2e, markers, seeds de DB)
- ruff (linter + formateador)
- pyright (type checking)
- uv como gestor de dependencias

Infra:

- Docker + docker-compose
- Base de datos (Postgres)
- Redis (cache, si da tiempo)
- Deploy en Render.com

Frontend (más adelante):

- TypeScript
- React
- NextJS

## Fases

1. Esqueleto backend
   - uv + FastAPI
   - ruff + pyright + pytest configurados
   - endpoint `/health` con su test

2. Base de datos + SQLAlchemy
   - Modelo sencillo (User/Task)
   - AsyncSession, conexión vía docker-compose (Postgres)
   - CRUD básico + tests de integración

3. Auth + HTTP / REST
   - Login/registro con JWT sencillo
   - Códigos HTTP bien usados
   - Manejo de errores e invariantes

4. Hardening
   - ruff + pyright estrictos
   - markers de pytest
   - N+1, caching con Redis, etc.

5. Docker + Render
   - Dockerfile
   - docker-compose (app + DB + Redis)
   - Deploy a Render.com

6. Frontend demo
   - NextJS consumiendo la API
   - Auth básica, listados, formularios
