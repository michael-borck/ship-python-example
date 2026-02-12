# Project: My Application

## Overview

A multi-platform Python application with FastAPI backend and React frontend.

## Architecture

### Stack
- **Backend**: FastAPI (Python 3.11+)
- **Frontend**: React 18 + TypeScript + Vite
- **Desktop**: Electron
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Deployment**: Docker, GitHub Actions

### Directory Structure
```
my-application/
├── backend/          # FastAPI application
│   ├── src/my_app/
│   └── tests/
├── frontend/         # React application
│   └── src/
├── electron/         # Desktop wrapper
├── docker/           # Container configs
└── .github/          # CI/CD workflows
```

## Conventions

### Backend
- All API routes under `/api/` prefix
- Pydantic models for all request/response schemas
- SQLAlchemy for database operations
- Async handlers where beneficial

### Frontend
- Functional components with hooks
- React Query for server state
- Axios for API calls
- TypeScript strict mode

### General
- Semantic versioning (v1.2.3)
- Conventional commits
- All code formatted and linted before commit

## Development Commands

### Backend
```bash
cd backend
uv run uvicorn my_app.main:app --reload
uv run pytest
uv run ruff check .
```

### Frontend
```bash
cd frontend
npm run dev
npm test
npm run lint
```

### Docker
```bash
docker-compose -f docker/docker-compose.yml up
```

## API Endpoints
- `GET /health` - Health check
- `GET /api/items` - List items
- `POST /api/items` - Create item
- `GET /api/items/{id}` - Get item
- `PUT /api/items/{id}` - Update item
- `DELETE /api/items/{id}` - Delete item

## Environment Variables
- `DEBUG` - Enable debug mode (default: false)
- `DATABASE_URL` - Database connection string
- `SECRET_KEY` - Application secret key
- `CORS_ORIGINS` - Allowed CORS origins
