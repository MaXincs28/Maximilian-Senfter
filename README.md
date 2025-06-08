# ShopOwner Demo

This repository contains a basic FastAPI backend with PostgreSQL and JWT authentication, along with a minimal Next.js frontend for registration and login.

## Prerequisites

- Python
- Node.js and npm
- PostgreSQL

You can open the integrated terminal in VS Code via **View → Terminal** or with **Ctrl+`**.

## Backend

1. Open a terminal and navigate to the `backend` directory.
2. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. Install the backend requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the API with hot‑reload:
   ```bash
   uvicorn app.main:app --reload
   ```

Ensure that the environment variable `DATABASE_URL` points to your PostgreSQL instance.

## Frontend

1. Open a **second terminal** (use the plus icon in the terminal panel).
2. Navigate to the `frontend` directory.
3. Install dependencies:
   ```bash
   npm install
   ```
4. Start the development server:
   ```bash
   npm run dev
   ```

The signup page is available at `/signup` and the login page at `/login`.
