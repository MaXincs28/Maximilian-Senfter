# ShopOwner Demo

This repository contains a basic FastAPI backend with PostgreSQL and JWT authentication, along with a minimal Next.js frontend for registration and login.

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

## License

This project is licensed under the [MIT License](LICENSE).
