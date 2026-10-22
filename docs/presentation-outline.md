# 10-minute presentation outline

1. **Problem and scope (1 min):** A startup needs a lightweight social platform. The MVP supports registration, login/logout, public feed and post creation.
2. **Requirements and assumptions (1 min):** Explain FR/NFR IDs, 280-character posts, unique usernames and public read access.
3. **Methodology and board (1 min):** Explain lightweight Scrum and show actual GitHub Project/Trello board.
4. **Architecture and ADR (1.5 min):** Flask monolith, SQLite, password hashing, Docker volume; mention trade-offs.
5. **Live demonstration (3 min):** Register a demo user, sign in, publish a post, show author/time in feed, sign out, and try posting while signed out.
6. **Quality and delivery (1 min):** Run `pytest -q`, show Docker Compose, and show successful GitHub Actions run if available.
7. **Reflection (1.5 min):** Explain that likes/follows and production hardening were intentionally excluded to protect the core MVP scope.

Only claim tests, Docker or CI succeeded after you have run them and observed the result.
