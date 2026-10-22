
import os
import tempfile
import pytest
from contextlib import closing
from app import app


@pytest.fixture()
def client():
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)

    import app as app_module
    old_database = app_module.DATABASE
    app_module.DATABASE = path
    app.config.update(TESTING=True, SECRET_KEY="test-secret")

    try:
        with app.test_client() as test_client:
            with test_client.session_transaction() as session:
                session.clear()
            yield test_client
    finally:
        app_module.DATABASE = old_database
        if os.path.exists(path):
            os.unlink(path)


def register(client, username="student1", password="securepass123"):
    return client.post(
        "/register",
        data={"username": username, "password": password},
        follow_redirects=True,
    )


def login(client, username="student1", password="securepass123"):
    return client.post(
        "/login",
        data={"username": username, "password": password},
        follow_redirects=True,
    )


def test_register_login_and_logout(client):
    response = register(client)
    assert b"Account created" in response.data

    response = login(client)
    assert b"Signed in as" in response.data

    response = client.post("/logout", follow_redirects=True)
    assert b"You have signed out" in response.data


def test_authenticated_user_can_post_and_feed_shows_post(client):
    register(client)
    login(client)

    response = client.post(
        "/post",
        data={"content": "Hello from my MVP!"},
        follow_redirects=True,
    )
    assert b"Hello from my MVP!" in response.data
    assert b"@student1" in response.data


def test_anonymous_user_cannot_post(client):
    response = client.post(
        "/post",
        data={"content": "not allowed"},
        follow_redirects=True,
    )
    assert b"Please sign in" in response.data
    assert b"not allowed" not in response.data


def test_password_is_hashed(client):
    register(client)

    import app as app_module
    with closing(app_module.connect_db()) as db, db:
        row = db.execute(
            "SELECT password_hash FROM users WHERE username = ?",
            ("student1",),
        ).fetchone()

    assert row["password_hash"] != "securepass123"
    assert row["password_hash"].startswith("scrypt:")
