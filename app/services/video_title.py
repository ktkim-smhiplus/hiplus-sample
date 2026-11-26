MAX_TITLE_LENGTH = 40
ELLIPSIS = "..."


def normalize_title(title: str) -> str:
    """제목이 40자를 넘으면 앞 37자 + '...' 으로 잘라 정확히 40자로 만든다."""
    if len(title) <= MAX_TITLE_LENGTH:
        return title
    return title[: MAX_TITLE_LENGTH - len(ELLIPSIS)] + ELLIPSIS
