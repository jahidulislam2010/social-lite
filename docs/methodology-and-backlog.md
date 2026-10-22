# Methodology and Backlog

## Methodology: lightweight Scrum
A lightweight Scrum approach is appropriate because the requirements are initially incomplete and the delivery window is short. Work is divided into a small set of prioritized tasks. The working MVP is reviewed against acceptance criteria after each increment. For an individual project, the student performs developer, tester and product-owner responsibilities.

## Working approach
- Sprint goal: deliver a locally runnable social posting MVP with documented engineering decisions.
- Daily check: identify completed work, next task and blockers.
- Definition of Done: code runs, relevant tests pass, README is updated, and changes are committed.
- Board workflow: Backlog → To Do → In Progress → Review / Testing → Done.
- Prioritization: mandatory account, feed and publishing features first; documentation, Docker and CI next; extras deferred.

## Prioritized backlog
| ID | User story / task | Acceptance criteria | Priority | Suggested status |
|---|---|---|---|---|
| US-01 | As a visitor, I want to register so that I can create an account. | Valid details create account; duplicates rejected. | P1 | Done when verified |
| US-02 | As a user, I want to sign in and out so that I can manage my session. | Correct login works; logout clears session. | P1 | Done when verified |
| US-03 | As a visitor, I want to view the feed so that I can read public posts. | Author, text and time shown newest first. | P1 | Done when verified |
| US-04 | As a signed-in user, I want to publish a post so that I can share an update. | Non-empty text up to 280 characters is saved and displayed. | P1 | Done when verified |
| US-05 | As an owner, I want persistent storage so that posts survive restarts. | Docker named volume stores SQLite database. | P1 | To verify |
| US-06 | As a lecturer, I want a repeatable local setup so that I can run the MVP. | README and Compose start app. | P1 | To verify |
| US-07 | As a developer, I want automated tests so that regressions are detected. | `pytest -q` passes. | P1 | To verify |
| US-08 | As a developer, I want CI on pushes so that tests/build are checked automatically. | GitHub Actions runs tests and Docker build. | P1 | To verify |
| US-09 | As an assessor, I want requirements and architecture decisions documented. | Requirements, diagram and ADR are committed. | P1 | Done when reviewed |
| US-10 | As a future user, I may want likes and profiles. | Deferred until mandatory criteria are complete. | P3 | Backlog |

## Board evidence
Create a GitHub Project (or Trello board) with the five columns above. Add US-01 to US-10. Move each card only when its work is genuinely complete and attach the repository or evidence link. Capture a screenshot for the submission.
