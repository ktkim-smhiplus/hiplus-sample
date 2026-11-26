from fastapi.testclient import TestClient

from app.services.video_title import normalize_title


def test_short_title_unchanged():
    assert normalize_title("안녕") == "안녕"


def test_40_chars_unchanged():
    title = "a" * 40
    assert normalize_title(title) == title


def test_41_chars_truncated_to_40():
    result = normalize_title("a" * 41)
    assert len(result) == 40
    assert result == "a" * 37 + "..."


def test_long_title_truncated_to_40():
    result = normalize_title("가" * 100)
    assert len(result) == 40
    assert result.endswith("...")


def test_api_boundary(client: TestClient):
    r40 = client.post("/videos", json={"title": "b" * 40})
    assert r40.status_code == 200
    assert r40.json()["title"] == "b" * 40
    r41 = client.post("/videos", json={"title": "b" * 41})
    assert r41.json()["title"] == "b" * 37 + "..."
