# 할 일 관리 웹앱 (Todo App) 스펙 문서

## 1. 개요
사용자가 할 일을 기록하고, 완료 여부를 관리하며, 필요 없는 항목을 삭제할 수 있는 심플한 웹 애플리케이션입니다. 최소한의 기능으로 높은 사용성을 목표로 합니다.

## 2. 기술 스택
- **Language**: Python 3.x
- **Framework**: Flask
- **Database**: SQLite3
- **Frontend**: HTML5, Vanilla CSS (외부 프레임워크 미사용)

## 3. 파일 구성
```text
todo_app/
├── app.py              # Flask 애플리케이션 로직 및 라우팅
├── database.db         # SQLite 데이터베이스 파일
├── static/
│   └── css/
│       └── style.css   # 사용자 정의 CSS 스타일
├── templates/
│   └── index.html      # 메인 페이지 HTML 템플릿
└── tests/
    └── test_app.py     # Flask test_client를 이용한 테스트 코드
```

## 4. 동작 규칙 (API/Route)

| 메서드 | 주소 (Endpoint) | 입력 (Input) | 결과 (Output) |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | 없음 | 전체 할 일 목록 (생성 시각 기준 오름차순) |
| `POST` | `/add` | `title` (string) | 새로운 할 일 추가 및 목록 리다이렉트 |
| `POST` | `/toggle/<id>` | `id` (integer) | 해당 ID의 `is_completed` 상태 반전 및 리다이렉트 |
| `POST` | `/delete/<id>` | `id` (integer) | 해당 ID의 데이터 삭제 및 리다이렉트 |
| `POST` | `/add` (Error Case) | `title` (empty string) | 에러 메시지 출력 또는 입력 무시 |
| `POST` | `/toggle/<invalid_id>` | `id` (non-existent) | 404 에러 또는 오류 메시지 처리 |
| `POST` | `/delete/<invalid_id>`| `id` (non-existent) | 404 에러 또는 오류 메시지 처리 |

## 5. 화면 구성
- **레이아웃**: 화면 중앙에 정렬된 단일 컨테이너 구조.
- **상단 영역**: 할 일 제목을 입력할 수 있는 `input` 창과 '추가' 버튼.
- **중간 영역**: 할 일 목록 리스트.
    - 각 항목은 제목, 완료 여부 상태를 표시.
    - 항목 클릭(또는 체크박스) 시 완료/미완료 토글.
    - 항목 우측에 '삭제' 버튼 배치.
- **스타일**: 별도의 프레임워크 없이 깔끔하고 가독성 있는 폰트와 여백을 가진 Vanilla CSS 적용.

## 6. 테스트 계획 (Flask `test_client` 활용)

| 요청 (Request) | 기대하는 결과 (Expected Result) |
| :--- | :--- |
| `GET /` | 초기 페이지 접속 시 200 OK 및 빈 목록 표시 |
| `POST /add` (제목: "공부하기") | 데이터베이스에 "공부하기" 저장 및 200 OK |
| `GET /` (데이터 추가 후) | 목록에 "공부하기"가 포함되어 나타남 |
| `POST /toggle/1` | ID 1번 항목의 `is_completed` 값이 0에서 1로 변경됨 |
| `POST /delete/1` | ID 1번 항목이 데이터베이스에서 완전히 삭제됨 |
| `GET /` (데이터 삭제 후) | 목록에 삭제된 항목이 보이지 않음 |
| `POST /add` (빈 제목 입력) | 400 Bad Request 또는 빈 값이 추가되지 않음 |
| `POST /add` (공백만 입력) | 데이터가 유효하지 않음을 처리하거나 추가되지 않음 |
| `POST /add` (매우 긴 제목) | 데이터베이스 저장 제한 확인 및 처리 |
| `POST /toggle/999` (없는 ID) | 404 Not Found 에러 발생 |
| `POST /delete/999` (없는 ID) | 404 Not Found 에러 발생 |
| `POST /toggle/abc` (숫자 아님) | 400 Bad Request 에러 발생 |

## 7. 완료 전 점검
- [ ] 모든 할 일이 생성 시간 순(오래된 순)으로 정렬되는가?
- [ ] 완료 상태 토글이 정상적으로 작동하는가?
- [ ] 삭제 버튼 클릭 시 데이터가 실제로 제거되는가?
- [ ] 디자인이 깨지지 않고 중앙 정렬되어 보이는가?
- [ ] 데이터베이스 파일(`database.db`)이 정상적으로 생성되는가?

## 8. 하지 않는 것
- **사용자 기능**: 로그인, 회원가입 기능 구현 안 함.
- **수정 기능**: 이미 작성된 할 일의 내용을 수정하는 기능 구현 안 함.
- **외부 프레임워크**: Bootstrap, Tailwind CSS 등 외부 CSS 프레임워크 사용 안 함.
- **JS 프레임워크**: React, Vue.js 등 자바스크립트 프레임워크 사용 안 함 (순수 HTML form 제출 방식 사용).
