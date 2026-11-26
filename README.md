# hiplus-sample

Google 시트에 적은 기능 정의를 n8n이 GitHub 이슈로 올리면, GitHub Actions의 Claude가 구현해 PR을 만드는 자동 개발 샘플 저장소입니다.

## 로컬 실행

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload   # http://localhost:8000/docs
pytest
```
