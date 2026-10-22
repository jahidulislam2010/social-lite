# Requirements Specification

## Purpose and assumptions
Social Lite is a local, lightweight social platform for demonstrating core user journeys to stakeholders. The first release is a web application. Users choose a unique username and password. Anyone may view the feed; only signed-in users may publish. Posts are plain text, limited to 280 characters. No email address is required for this MVP.

## Functional requirements
| ID | Requirement | Acceptance criteria | Priority |
|---|---|---|---|
| FR-01 | Register an account | A valid username (3–30 characters) and password (8+ characters) create one account; duplicate usernames are rejected. | Must |
| FR-02 | Authenticate user | Correct credentials start a session; incorrect credentials show a generic error. | Must |
| FR-03 | Sign out | A signed-in user can sign out and their session is cleared. | Must |
| FR-04 | View feed | The home page shows all posts with author, text and creation time, newest first. | Must |
| FR-05 | Publish post | Signed-in users can publish non-empty text of at most 280 characters; it appears at the top of the feed. | Must |
| FR-06 | Restrict publishing | Anonymous requests to publish are redirected to sign-in and do not create a post. | Must |
| FR-07 | Persist data | User and post records remain after an ordinary application/container restart when the volume is retained. | Must |

## Non-functional requirements
| ID | Requirement | Acceptance criteria | Priority |
|---|---|---|---|
| NFR-01 | Security | Passwords are hashed; parameterized SQL is used; publishing requires authentication. | Must |
| NFR-02 | Usability | Core pages use clear labels, simple navigation and feedback messages. | Should |
| NFR-03 | Reproducibility | A reviewer can start the app using `docker compose up --build` and open localhost:5000. | Must |
| NFR-04 | Maintainability | Routes, templates, tests and docs are organized separately. | Should |
| NFR-05 | Basic performance | Feed is ordered by newest inserted post and remains responsive for a small demonstration dataset. | Should |
| NFR-06 | Testability | Automated tests cover registration/login/logout, post publishing, access control and password hashing. | Must |

## Out of scope
Likes, comments, follows, direct messages, media uploads, email verification, password reset, moderation, mobile apps, deployment to the public internet and production-scale traffic.
