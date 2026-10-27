from fastapi.testclient import TestClient
from urllib.parse import unquote

from main import app

client = TestClient(app)



import json

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_set_preferences():
    payload = {
        "theme": "dark",
        "language": "pt",
        "notifications": False,
    }

    response = client.post("/preferences/", json=payload)

    assert response.status_code == 200
    assert response.json() == {"Preferences": "Saved"}

    cookie = response.cookies.get("user_preferences")   
    assert cookie is not None

    
    saved_preferences = json.loads(unquote(cookie))
    assert saved_preferences == payload
    


def test_get_preferences_with_cookie():
    preferences = {
        "theme": "dark",
        "language": "pt",
        "notifications": False,
    }

    response = client.get(
        "/preferences/",
        cookies={
            "user_preferences": json.dumps(preferences)
        },
    )

    assert response.status_code == 200
    assert response.json()["Preferences"] == preferences

def test_get_preferences_without_cookie():
    with TestClient(app) as client:
        response = client.get("/preferences/")

    assert response.status_code == 200
    assert response.json()["Preferences"] == {
        "theme": "light",
        "language": "en",
        "notifications": True,
    }

def test_invalid_theme():
    payload = {
        "theme": "blue",
        "language": "en",
        "notifications": True,
    }

    response = client.post("/preferences/", json=payload)

    assert response.status_code == 422


def test_invalid_language():
    payload = {
        "theme": "light",
        "language": "fr",
        "notifications": True,
    }

    response = client.post("/preferences/", json=payload)

    assert response.status_code == 422


def test_invalid_cookie_json():
    response = client.get(
        "/preferences/",
        cookies={"user_preferences": "{invalid json"},
    )

   
    assert response.status_code == 400
