from datetime import UTC, datetime


def get_health_status(now: datetime | None = None) -> dict[str, str]:
    now = now or datetime.now(UTC)
    return {"status": "ok", "time": now.isoformat()}
