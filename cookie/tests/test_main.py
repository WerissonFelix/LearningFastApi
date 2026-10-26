from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_cookies():
    response = client.get(
        "/cookies/",
        cookies={
            "session_id": "abc123",
            "fatebook_tracker": "tracker456",
            "googall_tracker": "tracker789",
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "Cookie": {
            "session_id": "abc123",
            "fatebook_tracker": "tracker456",
            "googall_tracker": "tracker789",
        }
    }


def test_read_cookies_with_optional_fields_missing():
    response = client.get(
        "/cookies/",
        cookies={"session_id": "abc123"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "Cookie": {
            "session_id": "abc123",
            "fatebook_tracker": None,
            "googall_tracker": None,
        }
    }


def test_read_cookies_without_cookies():
    response = client.get("/cookies/", cookies={})

    assert response.status_code == 200
    assert response.json() == {"Cookie": None}


def test_read_cookies_missing_required_field():
    response = client.get(
        "/cookies/",
        cookies={"fatebook_tracker": "tracker456"},
    )

    assert response.status_code == 422


def test_read_preferences():
    response = client.get(
        "/preferences/",
        cookies={
            "theme": "dark",
            "locale": "en-US",
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "Preference: ": {
            "theme": "dark",
            "locale": "en-US",
        }
    }


def test_read_preferences_without_cookies():
    response = client.get("/preferences/")

    assert response.status_code == 200
    assert response.json() == {"Preference: ": None}


def test_read_preferences_missing_required_field():
    response = client.get(
        "/preferences/",
        cookies={"theme": "dark"},
    )

    assert response.status_code == 422