# ShopOwner Demo

This repository contains a basic FastAPI backend with PostgreSQL and JWT authentication, along with a minimal Next.js frontend for registration and login. Once logged in you can also create shops and add products.

## Backend

Navigate to `backend` and install requirements:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app.main:app --reload
```

Environment variable `DATABASE_URL` should point to your PostgreSQL instance.

### Quick start in VS Code (Windows example)

1. Open the repository folder in Visual Studio Code.
2. Open the terminal and run the backend:
   ```cmd
   cd backend
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   set DATABASE_URL=postgresql://user:password@localhost/shop
   uvicorn app.main:app --reload
   ```
3. Open another terminal for the frontend:
   ```cmd
   cd frontend
   npm install
   npm run dev
   ```
4. Visit `http://localhost:3000/signup` in your browser to create an account and then `/login` to sign in.

## Frontend

Navigate to `frontend` and install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The signup page is at `/signup` and login page at `/login`.
After logging in, you can create a shop at `/create-shop` and add products at `/add-product`.
