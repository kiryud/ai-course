# project 실습 규칙 문서

## 공통 규칙

- 개발 언어는 `python`이다.
    - `python`의 버전은 3.10 이상이어야 한다
    - `Flet` 1.0 패키지만 사용 가능하다
    - `random` `json`등의 모듈은 사용 가능하다
- `Flet`은 `main.py`와 동일한 뼈대를 기반으로 작성해야한다
    - 뼈대에 없는 클래스, 인자, 속성은 사용하지 않는다
    - 메모리에 저장된 Flet 문법은 버전이 맞지 않으므로 절대 사용하지 않아야만 한다
    - 특히 flet 1.0에서 절대 사용하면 안되는 존재하지 않는 함수는 다음과 같다
        - ft.app(...)
        - ft.colors
        - ft.alignment.center
        - ft.ElevatedButton
        - Button(text=...)
        - page.window_width
        - ft.UserControl
        - TextField(error_text=...)