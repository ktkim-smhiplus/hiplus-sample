from datetime import UTC, datetime


def get_health(now: datetime | None = None) -> dict[str, str]:
    """서버 상태와 ISO8601 현재 시각을 반환한다."""
    current = now or datetime.now(UTC)
    return {"status": "ok", "time": current.isoformat()}
