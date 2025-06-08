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
2. Copy `.env.example` to `.env` in the `backend` folder and adjust values.
3. Apply the database migrations using `alembic upgrade head` from the
   `backend` directory (requires PostgreSQL with the PostGIS extension).
4. Run the API with `python backend/main.py`.
5. Start the Celery worker with `celery -A backend.celery_app.celery_app worker --loglevel=info`.

Authentication uses JWTs signed with the secret key. Set `FIREBASE_CREDENTIALS` in your `.env`
to initialize Firebase Admin. Register and log in via `/auth/register` and `/auth/login`,
then include the token in the `Authorization` header to access `/shops` and `/products` routes.
Provide a Stripe test secret in `STRIPE_API_KEY` for order payments.
