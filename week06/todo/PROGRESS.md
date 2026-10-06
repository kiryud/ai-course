# Progress Report

## ✅ 완료된 단계
- 데이터베이스 설계 및 CRUD 로직 구현 (`db.py`, `database.db`)
- Flask 기본 라우팅 및 앱 구조 설정 (`app.py`)
- 기본 기능 테스트 작성 (`test_app.py`)

## ⚠️ 스펙 대비 차이점
- 테스트 코드에서 `app.DATABASE`를 변경해도 `db.py` 내부의 `DATABASE` 변수에 반영되지 않아 테스트 격리가 완벽하지 않을 수 있음.

## 🚀 남은 일
- 프론트엔드 구현 (`templates/index.html`, `static/css/style.css`)
- 상세 기능 테스트 완성 (Toggle, Delete, Error cases)
- 빈 제목 입력 등 예외 처리 보완
