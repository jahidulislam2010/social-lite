# Social Lite — Software Engineering Workshop MVP

A lightweight X/Twitter-style web app built with Flask and SQLite.

## Features
- Register, sign in and sign out
- Passwords stored as Werkzeug password hashes, never plain text
- Authenticated users can publish posts (maximum 280 characters)
- Public feed shows author, content and creation time, newest first
- SQLite data persisted in a Docker named volume
- Automated tests and GitHub Actions CI

## Requirements
Install Docker Desktop and ensure Docker Compose is available. Alternatively, use Python 3.12+ for local development.

## Run with Docker
From this folder:
```bash
docker compose up --build
```
Open http://localhost:5000. Stop with `Ctrl+C`; optionally run `docker compose down`. The named volume `social_data` preserves the database across container restarts. To delete all stored data, run `docker compose down -v`.

## Run tests locally
Run these commands from the project root folder (the folder containing `app.py`). The `pytest.ini` file configures test discovery.
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

Tests use a temporary database. The default app database is `/data/social.db`; set `DATABASE_PATH` to a writable path for local development.

## Example user journey
1. Select **Create account** and register a username (3–30 characters) and password (at least 8 characters).
2. Sign in with those credentials.
3. Publish a short post from the home feed.
4. Confirm it appears at the top with author and timestamp.
5. Sign out and verify posting redirects to sign-in.
6. Restart the Docker container and confirm the post remains.

## Project structure
- `app.py` — routes, authentication and SQLite persistence
- `templates/` — HTML views
- `tests/` — automated tests
- `docs/` — requirements, methodology, backlog and architecture decision record
- `.github/workflows/ci.yml` — test and Docker build on push/pull request

## Submission verification checklist
Before submission, run `pytest -q`, start the app with `docker compose up --build`, and manually demonstrate registration, login, posting, feed order, logout, and persistence after restarting the container. Save screenshots of the successful test output, running application, GitHub Actions result, and project board. Do not claim a test or CI run passed until you have observed the result.

## Security and scope
This is an educational local MVP, not production-ready. Set a strong `SECRET_KEY` outside source control before any non-demo deployment. HTTPS, email verification, password reset, rate limiting, moderation and production database operations are out of scope.

## Engineering decisions
See `docs/requirements.md`, `docs/methodology-and-backlog.md`, and `docs/architecture-and-adr.md`.
