from datetime import UTC, datetime

from app.services.health import get_health


def test_health_returns_200_and_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert set(body) == {"status", "time"}


def test_health_time_is_iso8601(client):
    body = client.get("/health").json()
    assert datetime.fromisoformat(body["time"]).tzinfo is not None


def test_health_requires_no_auth(client):
    response = client.get("/health", headers={})
    assert response.status_code == 200


def test_get_health_service_uses_given_time():
    now = datetime(2026, 1, 2, 3, 4, 5, tzinfo=UTC)
    assert get_health(now) == {"status": "ok", "time": "2026-01-02T03:04:05+00:00"}
