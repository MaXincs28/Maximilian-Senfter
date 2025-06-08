# Project Skeleton

This repository demonstrates a simple multi-platform project layout. It contains a Python FastAPI backend and placeholders for separate mobile and web frontends. Folders for infrastructure scripts and documentation are included as well.

## Directory Structure

- `backend/` – FastAPI application code
- `frontend/mobile/` – placeholder for mobile client
- `frontend/web/` – web client implementation
- `infra/` – infrastructure configuration
- `docs/` – project documentation

This structure provides a starting point for expanding the backend and frontend implementations or adding deployment scripts under `infra`.

### Backend quickstart
1. Install dependencies from `backend/requirements.txt`.
2. Copy `.env.example` to `.env` in the `backend` folder and adjust values if needed.
3. Run the API locally with `python backend/main.py`.

Authentication uses JWTs signed with the secret key. Register and log in via `/auth/register` and `/auth/login`,
then include the token in the `Authorization` header to access `/shops` and `/products` routes.
