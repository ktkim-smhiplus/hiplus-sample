from datetime import UTC, datetime

from app.services.health import get_health_status


def test_health_returns_200_and_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_health_time_is_iso8601(client):
    body = client.get("/health").json()
    assert datetime.fromisoformat(body["time"]).tzinfo is not None


def test_health_needs_no_auth(client):
    response = client.get("/health")  # 인증 헤더 없이 호출
    assert response.status_code == 200


def test_service_uses_given_time():
    now = datetime(2026, 1, 1, tzinfo=UTC)
    assert get_health_status(now) == {"status": "ok", "time": now.isoformat()}
