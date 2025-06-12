# Project Skeleton

This repository contains a minimal FastAPI backend and a simple Next.js web frontend. It is intended for local testing with SQLite and does not require any additional services.

## Directory Structure

- `backend/` – FastAPI application code
- `frontend/web/` – Next.js web client

This structure can easily be expanded as you add more features.

### Backend quickstart
1. Install dependencies from `backend/requirements.txt` (Pydantic is pinned to v1 for compatibility and includes `python-multipart` for file uploads).
2. Copy `.env.example` to `.env` in the `backend` folder and adjust values if needed.
3. Run the API locally with `python backend/main.py`. It uses SQLite by default and will create `local.db` automatically. You can also launch it with Uvicorn:
   ```bash
   uvicorn backend.main:app --reload
   ```
4. (Optional) To use PostgreSQL, set `DATABASE_URL` in `.env` and run `alembic upgrade head` from the `backend` directory before starting the API.

Alternatively, you can run it as a module with `python -m backend.main`.

Ensure that an empty `backend/__init__.py` file exists so the package can be executed as a module.

Authentication uses JWTs signed with the secret key. Register and log in via `/auth/register` and `/auth/login`,
then include the token in the `Authorization` header to access `/shops` and `/products` routes.

### Running on Windows
1. Open PowerShell in the project root.
2. Create a virtual environment:
   ```powershell
   py -3 -m venv .venv
   .\.venv\Scripts\activate
   ```
3. Install dependencies:
   ```powershell
   pip install -r backend\requirements.txt
   ```
4. Copy the example environment file:
   ```powershell
   copy backend\.env.example backend\.env
   ```
5. Start the API:
   ```powershell
   python backend\main.py
   ```
The server listens on http://localhost:8000 and uses a local SQLite database located at `backend/local.db`.

### Frontend quickstart
1. Open a new terminal and navigate to `frontend/web`.
2. Install dependencies with:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```
   The frontend will be available at <http://localhost:3000> and expects the backend to run on port 8000.
