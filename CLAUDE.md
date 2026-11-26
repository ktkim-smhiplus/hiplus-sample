# CLAUDE.md

이 저장소는 Google 시트의 기능 정의가 n8n을 거쳐 `claude-dev` 라벨 이슈로 올라오면,
GitHub Actions의 Claude가 구현하고 PR을 만드는 자동 개발 대상입니다.

## 기술 스택
- Python 3.12, FastAPI, Pydantic v2
- 테스트: pytest + `fastapi.testclient.TestClient` (`tests/conftest.py`의 `client` 픽스처 사용)
- 린트/포맷: ruff (`pyproject.toml` 설정 따름, 줄 길이 100)
- 새 런타임 의존성은 꼭 필요할 때만 추가하고, 추가했다면 PR 본문에 이유를 적는다.

## 명령
```bash
pip install -e ".[dev]"     # 의존성 설치
pytest -q                   # 테스트
ruff check . && ruff format --check .   # 린트/포맷 검사
ruff format .               # 포맷 적용
```
PR을 만들기 전에 위 테스트와 린트가 모두 통과해야 한다.

## 구조
```
app/
  main.py          # FastAPI 앱 생성, 라우터 등록만
  routers/         # 기능별 APIRouter (예: health.py)
  schemas/         # Pydantic 요청/응답 모델
  services/        # 비즈니스 로직 (라우터에서 분리, 순수 함수 우선)
tests/
  test_<기능>.py   # 기능별 테스트
```
- 라우터는 얇게 두고 로직은 `services/`에 둔다. 서비스 함수는 HTTP 없이 단위 테스트한다.
- 엔드포인트는 응답 모델(`response_model`)을 명시한다.
- 디렉터리가 아직 없으면 위 구조대로 만든다.

## 이슈 처리 규칙
- 이슈 본문의 **기능 정의**와 **수용 기준**이 요구사항의 전부다. 범위 밖 리팩터링이나 기능 추가는 하지 않는다.
- 수용 기준마다 최소 하나의 테스트를 작성하고, 경계값이 언급되면 경계값 테스트를 포함한다.
- 요구사항이 모호하면 가장 단순한 해석으로 구현하고, 그 가정을 PR 본문 "가정" 항목에 적는다.
- 브랜치: `claude/issue-<번호>-<짧은-설명>`
- 커밋 메시지와 PR 제목: `feat: <기능명> (#<이슈번호>)` 형식, 한국어 설명 허용
- PR 본문에는 반드시 `Closes #<이슈번호>`를 포함한다. n8n이 이 문구로 시트 상태를 갱신한다.
- PR 본문 구성: 요약 / 변경 파일 / 수용 기준별 확인 결과 / 가정

## 금지
- `.env`, 키, 토큰 등 비밀값을 커밋하지 않는다.
- `.github/workflows/` 파일은 수정하지 않는다.
- 테스트를 통과시키려고 기존 테스트를 삭제하거나 약화시키지 않는다.
