from datetime import UTC, datetime

from app.services.health import get_health


def test_health_returns_ok(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"


def test_health_requires_no_auth(client):
    # 인증 헤더 없이 호출해도 200
    assert client.get("/health").status_code == 200


def test_health_time_is_iso8601(client):
    body = client.get("/health").json()
    assert set(body) == {"status", "time"}
    assert datetime.fromisoformat(body["time"]).tzinfo is not None


def test_get_health_service_uses_given_time():
    now = datetime(2026, 1, 1, tzinfo=UTC)
    assert get_health(now) == {"status": "ok", "time": "2026-01-01T00:00:00+00:00"}
