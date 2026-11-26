from datetime import UTC, datetime


def get_health(now: datetime | None = None) -> dict[str, str]:
    """서버 상태와 ISO8601 시각을 반환한다."""
    now = now or datetime.now(UTC)
    return {"status": "ok", "time": now.isoformat()}
