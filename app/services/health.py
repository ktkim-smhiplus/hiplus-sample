from datetime import UTC, datetime


def get_health_status(now: datetime | None = None) -> dict[str, str]:
    current = now or datetime.now(UTC)
    return {"status": "ok", "time": current.isoformat()}
