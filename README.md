# Ship Python Example

<!-- BADGES:START -->
[![api-first-architecture](https://img.shields.io/badge/-api--first--architecture-blue?style=flat-square)](https://github.com/topics/api-first-architecture) [![docker](https://img.shields.io/badge/-docker-2496ed?style=flat-square)](https://github.com/topics/docker) [![electron](https://img.shields.io/badge/-electron-47848f?style=flat-square)](https://github.com/topics/electron) [![fastapi](https://img.shields.io/badge/-fastapi-009688?style=flat-square)](https://github.com/topics/fastapi) [![javascript](https://img.shields.io/badge/-javascript-f7df1e?style=flat-square)](https://github.com/topics/javascript) [![multi-platform-development](https://img.shields.io/badge/-multi--platform--development-blue?style=flat-square)](https://github.com/topics/multi-platform-development) [![pwa](https://img.shields.io/badge/-pwa-blue?style=flat-square)](https://github.com/topics/pwa) [![python](https://img.shields.io/badge/-python-3776ab?style=flat-square)](https://github.com/topics/python) [![react](https://img.shields.io/badge/-react-61dafb?style=flat-square)](https://github.com/topics/react) [![typescript](https://img.shields.io/badge/-typescript-3178c6?style=flat-square)](https://github.com/topics/typescript)
<!-- BADGES:END -->

A complete working example of a multi-platform Python application demonstrating the architecture from **[Ship Python, Orchestrate AI: Professional Python in the AI Era](https://michael-borck.github.io/ship-python-orchestrate-ai)** by Michael Borck.

This example shows a simple task manager application with:
- FastAPI backend with RESTful API
- React frontend with TypeScript
- Electron desktop wrapper
- Docker deployment configuration

## Running the Example

### Backend

```bash
cd backend
uv sync
uv run uvicorn my_app.main:app --reload
```

Visit http://localhost:8000/docs to see the API documentation.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Visit http://localhost:5173 to see the app.

### Docker (Full Stack)

```bash
docker-compose -f docker/docker-compose.yml up
```

### Desktop (Electron)

```bash
cd frontend && npm run build
cd ../electron
npm install
npm start
```

## What This Example Demonstrates

1. **API-First Architecture**: Backend and frontend communicate through a well-defined REST API
2. **Type Safety**: Pydantic models (backend) and TypeScript (frontend) ensure type safety
3. **Modern Tooling**: uv, Vite, React Query for efficient development
4. **Multi-Platform Distribution**: Same codebase runs as web app, PWA, and desktop app
5. **AI-Ready Structure**: CLAUDE.md provides context for AI assistants

## Project Structure

```
ship-python-example/
├── backend/           # FastAPI backend
│   ├── src/my_app/    # Application code
│   └── tests/         # API tests
├── frontend/          # React frontend
│   └── src/           # Components and services
├── electron/          # Desktop wrapper
├── docker/            # Container configs
├── .github/workflows/ # CI/CD
└── CLAUDE.md          # AI context
```

## Using This as a Starting Point

If you want to use this architecture for your own project:

1. **Cookiecutter template**: `cookiecutter gh:michael-borck/ship-python-cookiecutter` - Full customization
2. **GitHub template**: [ship-python-template](https://github.com/michael-borck/ship-python-template) - Quick start

## Related Resources

- [Ship Python, Orchestrate AI](https://github.com/michael-borck/ship-python-orchestrate-ai) - The companion book
- [ship-python-cookiecutter](https://github.com/michael-borck/ship-python-cookiecutter) - Cookiecutter template
- [ship-python-template](https://github.com/michael-borck/ship-python-template) - GitHub template

## License

MIT License - see [LICENSE](LICENSE) for details.
