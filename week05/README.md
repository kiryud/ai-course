# 5주차 확인 과제

> 정리가 명시된 항목 없음

---

### 1절 : 직접해보기 1

소스코드 : NULL

실행 결과

```shell
PS C:\Users\user> curl http://localhost:11434/api/version

보안 경고: 스크립트 실행 위험
Invoke-WebRequest는 웹 페이지의 내용을 구문 분석합니다. 페이지를 구문 분석할 때 웹 페이지 내 스크립트 코드가 실행될 수
있습니다.
      권장 조치:
      -UseBasicParsing 스위치를 사용하여 스크립트 코드 실행을 방지합니다.

      계속하시겠어요?

[Y] 예(Y)  [A] 모두 예(A)  [N] 아니요(N)  [L] 모두 아니요(L)  [S] 일시 중단(S)  [?] 도움말 (기본값은 "N"): a


StatusCode        : 200
StatusDescription : OK
Content           : {"version":"0.34.3"}
RawContent        : HTTP/1.1 200 OK
                    Content-Length: 20
                    Content-Type: application/json; charset=utf-8
                    Date: Tue, 29 Sep 2026 04:53:23 GMT

                    {"version":"0.34.3"}
Forms             : {}
Headers           : {[Content-Length, 20], [Content-Type, application/json; charset=utf-8], [Date, Tue, 29 Sep 2026 04:
                    53:23 GMT]}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 20



PS C:\Users\user> curl http://localhost:11434/api/tags


StatusCode        : 200
StatusDescription : OK
Content           : {"models":[{"name":"qwen3:8b","model":"qwen3:8b","modified_at":"2026-09-15T14:34:53.2035018+09:00",
                    "size":5225388164,"digest":"500a1f067a9f782620b40bee6f7b0c89e17ae61f686b92c24933e4ca4b2b8b41","deta
                    il...
RawContent        : HTTP/1.1 200 OK
                    Content-Length: 1685
                    Content-Type: application/json; charset=utf-8
                    Date: Tue, 29 Sep 2026 04:53:34 GMT

                    {"models":[{"name":"qwen3:8b","model":"qwen3:8b","modified_at":"2026-09-15T...
Forms             : {}
Headers           : {[Content-Length, 1685], [Content-Type, application/json; charset=utf-8], [Date, Tue, 29 Sep 2026 0
                    4:53:34 GMT]}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 1685
```

### 1절 : 직접해보기 2

소스코드 : [raw.py](./raw.py)

실행 결과

````shell
{
  "model": "qwen3:8b",
  "created_at": "2026-09-29T04:54:30.9845785Z",
  "message": {
    "role": "assistant",
    "content": "파이썬에서 리스트를 한 줄로 뒤집는 방법은 다음과 같습니다:\n\n```python\nmy_list = [1, 2, 3, 4, 5]\nreversed_list = my_list[::-1]\n```\n\n이 코드는 `my_list`를 뒤집어서 `reversed_list`에 저장합니다. `[::-1]`은 슬라이싱을 사용한 리스트 뒤집기 방법입니다."
  },
  "done": true,
  "done_reason": "stop",
  "total_duration": 6115364000,
  "load_duration": 3949479600,
  "prompt_eval_count": 34,
  "prompt_eval_cached_count": 0,
  "prompt_eval_duration": 149091000,
  "eval_count": 97,
  "eval_duration": 2012684000
}

답만: 파이썬에서 리스트를 한 줄로 뒤집는 방법은 다음과 같습니다:

```python
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
```

이 코드는 `my_list`를 뒤집어서 `reversed_list`에 저장합니다. `[::-1]`은 슬라이싱을 사용한 리스트 뒤집기 방법입니다.
생성 속도: 48.2 tok/s
````

### 2절 : 직접해보기 3

소스코드 : [twoservers.py](./twoservers.py)

실행 결과

```shell
[내 PC (Ollama)] 파이썬에서 리스트와 튜플의 주요 차이는 리스트는 변경 가능한(mutable) 자료구조이고 튜플은 변경 불가능한(immutable) 자료구조라는
   입력 28 토큰, 출력 200 토큰
[실습 서버 (vLLM)] 리스트는 요소를 변경할 수 있는 **가변(Mutable)** 객체인 반면, 튜플은 생성 후 요소를 변경할 수 없는 **불변(Immutable)** 객체입니다.
   입력 31 토큰, 출력 44 토큰
```

### 3절 : 직접해보기 4

소스코드 : [sse.py](./sse.py)

실행 결과

```shell
봄의 따스함을 담은 짧은 시입니다.

**[봄의 인사]**

겨울잠 깨어난 햇살 한 줌에
얼었던 땅이 기지개를 켜고
수줍게 고개 내민 꽃봉오리 위로
살랑이는 봄바람이 머물다 가네.

조각 34개, 입력 27 토큰, 출력 73 토큰
```

### 4절 : 직접해보기 5

소스코드 : [chat.py](./chat.py)

실행 결과

```shell

나: /history
  [system] 당신은 프로그래밍 조교다. 한국어로 짧게 답한다.
  [user] 내 이름은 정진석이야
  [assistant] 안녕하세요, 정진석 씨! 도와드릴 일이 있으신가요?

나: 내 이름이 뭐더라
AI: 당신의 이름은 정진석이에요.

나: /reset
(대화 이력을 지웠습니다)

나: 내 이름이 뭐였지
AI: 당신의 이름은 알려드릴 수 없어요. 😊

나: /history
  [system] 당신은 프로그래밍 조교다. 한국어로 짧게 답한다.
  [user] 내 이름이 뭐였지
  [assistant] 당신의 이름은 알려드릴 수 없어요. 😊
```

### 5절 : 직접해보기 6

소스코드 : [jsonmode.py](./jsonmode.py)

실행 결과

```shell
원문: {"name": "김민수", "dept": "소프트웨어학부", "year": "2학년"}
파싱: 김민수 / 소프트웨어학부 / 2학년
```

### 6절 : 직접해보기 7

소스코드 : [tools.py](./tools.py)

실행 결과

```shell
  도구 호출: get_time({}) -> 2026-09-29 14:10
  도구 호출: calc({'expression': '17 * 24'}) -> 408
답: 지금은 2026년 9월 29일 14시 10분입니다. 그리고 17 곱하기 24는 408입니다.
```

### 7절 : 직접해보기 8

소스코드 : NULL

실행 결과

```shell
gemma4
25.9M
 Downloads
Updated 
6 days ago

Gemma 4 models are designed to deliver frontier-level performance at each size. They are well-suited for reasoning, agentic workflows, coding, and multimodal understanding.
vision
tools
thinking
audio
cloud
e2b
e4b
12b
26b
31b
```

### 8절 : 도전

소스코드 : [rag.py](./rag.py)

실행 결과

```shell
Q: 책 빌리는 곳 몇 시에 닫아?
   검색: 도서관은 평일 오전 9시부터 오후 10시까지 연다
   답: 자료에 없습니다.
Q: 졸업하려면 뭐가 필요해?
   검색: 졸업 요건은 130학점 이상 이수와 졸업 작품 제출이다
   답: 졸업하려면 130학점 이상 이수와 졸업 작품 제출이 필요해.
Q: 학식은 얼마야?
   검색: 졸업 요건은 130학점 이상 이수와 졸업 작품 제출이다
   답: 자료에 없습니다
```

### 9절 : 직접해보기 9

소스코드 : NULL

### 9절 : 직접해보기 10

소스코드 :

[index.html](./toss/index.html)
[success.html](./toss/success.html)
[fail.html](./toss/fail.html)


### 9절 : 직접해보기 11

소스코드 :
[SPEC.md](./toss/SPEC.md)
[app.py](./toss/app.py)
[index.html](./toss/templates/index.html)
[success.html](./toss/templates/success.html)
[fail.html](./toss/templates/fail.html)


### 9절 : 직접해보기 12

소스코드 : [index.html](./figma/index.html)
