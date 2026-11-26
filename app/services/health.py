from datetime import UTC, datetime


def get_health(now: datetime | None = None) -> dict[str, str]:
    current = now or datetime.now(UTC)
    return {"status": "ok", "time": current.isoformat()}
