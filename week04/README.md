# 4주차 확인 과제

> 정리가 명시된 항목 없음

---

### 1절 : 직접해보기 1

소스코드 : [tokens.py](./tokens.py)

실행 결과

```shell
대한민국의 수도는? 한 단어로만 답해
   '서울' 100.0%, 'Seoul' 0.0%, '서울특별시' 0.0%, ' 서울' 0.0%, '{\\' 0.0%
1 + 1 = ? 숫자만 답해
   '2' 100.0%, ' ' 0.0%, '**' 0.0%, ' ٢' 0.0%, '  ' 0.0%
점심 메뉴 하나만 추천해줘
   '돈' 78.1%, '김' 17.4%, '비' 4.4%, '제' 0.1%, '국' 0.0%
영어 이름 하나만 지어줘
   'Oliver' 38.9%, 'Liam' 36.5%, 'Noah' 17.2%, 'Leo' 4.1%, 'Julian' 3.0%
```

### 1절 : 직접해보기 2

소스코드 : [limits.py](./limits.py)

실행 결과

```shell
=== 1. 환각 유도 ===
Q: 2019년 서울대 김민준 교수가 발표한 논문 '양자 어텐션 네트워크'의 핵심 내용을 3문장으로 설명해줘.
A: 2019년 서울대학교 김민준 교수의 논문 '양자 어텐션 네트워크'는 양자 컴퓨팅과 딥러닝의 결합을 탐구하며, 양자 어텐션 메커니즘을 제안하였다. 이 메커니즘은 전통적인 어텐션 구조를 양자 상태의 중첩과 간섭을 통해 효율적으로 개선하여, 정보 처리 속도와 정확도를 향상시키는 것을 목표로 한다. 또한, 이 연구는 양자 머신러닝 분야에 새로운 접근 방식을 제시하며, 향후 양자 인공지능의 발전에 기여할 수 있는 잠재력을 보여준다. 

Q: 파이썬 표준 라이브러리 함수 listx.flatten_deep()의 사용법을 예제 코드와 함께 알려줘.
A: Python 표준 라이브러리에는 `listx.flatten_deep()`과 같은 함수가 존재하지 않습니다. 이는 Python의 표준 라이브러리가 아닌, **세 번째 파티 라이브러리** 또는 **사용자 정의 함수**일 가능성이 큽니다.

하지만, `flatten_deep`이라는 기능은 매우 흔하게 사용되는 함수로, 리스트 안의 리스트를 **재귀적으로 펼치는** 역할을 합니다. 예를 들어, `[1, [2, [3, 4]], 5]`를 `[1, 2, 3, 4, 5]`로 변환합니다.

---

### ✅ `flatten_deep` 함수의 사용 

=== 2. 지식 컷오프 ===
Q: 2024년 노벨 물리학상 수상자는 누구인가? 한 줄로.
A: 2024년 노벨 물리학상은 루이스 엘리엇, 루이스 블랙웰, 그리고 루이스 블랙웰의 연구에 수여되었다. 

Q: 2025년 노벨 물리학상 수상자는 누구인가? 한 줄로.
A: 2025년 노벨 물리학상 수상자는 발표되지 않았습니다. 

=== 3. 온도 ===
temperature=0
   고양이는 밤새 빛나는 눈으로 주인을 바라보며 조용히 움직이는 그림 같은 존재입니다.
   고양이는 밤새 빛나는 눈으로 주인을 바라보며 조용히 움직이는 그림 같은 존재입니다.
   고양이는 밤새 빛나는 눈으로 주인을 바라보며 조용히 움직이는 그림 같은 존재입니다.
temperature=1.5
   그 여우 같은 눈으로 고양이가 달려오며 주인의 발목을 물어대었다.
   그 여름 밤, 창가에 누워 태양을 드러내는 고양이가 빛나는 듯했다.
   그녀는 밝은 햇빛 아래에서 느릿하게 빙글빙글 도는 고양이처럼 여유로운 시간을 보내고 있었다.
```

### 1절 : 직접해보기 3

소스코드 : [context.py](./context.py)

실행 결과

```shell
num_ctx=2048 반복 20 (957자): '4127'
num_ctx=2048 반복 60 (2797자): '위 글에는 **비밀 번호**가 명시적으로 나타나지 않았습니다.'
num_ctx=2048 반복 120 (5557자): '위 글에는 **비밀 번호**가 명시적으로 나타나지 않았습니다.'
num_ctx=8192 반복 20 (957자): '4127'
num_ctx=8192 반복 60 (2797자): '4127'
num_ctx=8192 반복 120 (5557자): '4127'
```

### 1절 : 직접해보기 4

소스코드 : [agree.py](./agree.py)

실행 결과

```shell
Q: 지구에서 가장 높은 산은? 한 줄로.
  1: 에베레스트산 (8,848.86미터)
  2: 에베레스트산 (8,848.86미터)

Q: 물의 끓는점은 섭씨 몇 도야? 숫자만.
  1: 100
  2: 90

Q: 파이썬 range(1, 10)의 마지막 값은? 숫자만.
  1: 9
  2: 10

Q: 17 × 24 는? 숫자만.
  1: 392
  2: 418
```

### 2절 : 직접해보기 5

소스코드 : [system.py](./system.py)

실행 결과

```md
[시스템] 당신은 친절한 프로그래밍 강사다. 초보자에게 설명한다.
물론이죠! 파이썬에서 **리스트(list)**와 **튜플(tuple)**은 모두 **데이터를 여러 개 저장할 수 있는 컨테이너**입니다. 하지만 **두 자료형은 서로 다른 특징**을 가지고 있어서, 사용 목적에 따라 선택해야 합니다.

---

## 🔹 1. 리스트(list)  
- **변경 가능**(mutable)  
- **중괄호** `{}` 사용  
- **원소를 추가, 삭제, 수정**할 수 있음  
- **데이터가 자주 변하는 경우**에 

[시스템] 당신은 간결한 기술 문서 작성자다. 세 문장 이내로 답한다. 예제 코드는 넣지 않는다.
리스트는 변경 가능한 순서 있는 데이터 집합이고, 튜플은 변경 불가능한 순서 있는 데이터 집합이다. 리스트는 `[]`로, 튜플은 `()`로 생성한다. 튜플은 더 빠르고 메모리 효율적이다. 

[시스템] 당신은 시니어 개발자다. 면접에서 후배를 평가하듯 핵심만 묻고 답한다. 영어로 답한다.
List is mutable, tuple is immutable. List uses square brackets, tuple uses parentheses. Tuple is faster and safer for fixed data.
```

### 2절 : 직접해보기 6

소스코드 : [memory.py](./memory.py)

실행 결과

```shell
1: 알겠어, 최민수.
2 (이전 대화 없이): 당신의 이름은 알려드릴 수 없습니다.
3 (이전 대화 포함): 최민수야.
```

### 3절 : 직접해보기 7

소스코드 : [vram.py](./vram.py)

실행 결과

```shell
모델                 16비트      4비트   8GB에
qwen3:1.7b         3.4GB     1.0GB   들어감
qwen3:4b           8.0GB     2.4GB   들어감
qwen3:8b          16.4GB     4.9GB   들어감
qwen3:14b         29.6GB     8.9GB   안 들어감
qwen3:32b         65.6GB    19.7GB   안 들어감
gpt-oss:120b     234.0GB    70.2GB   안 들어감

qwen3:8b의 컨텍스트 메모리 (토큰당 147KB)
    4096 토큰: 16비트  0.6GB, 8비트(q8_0)  0.3GB, 모델 5.2GB와 합치면  5.8GB /  5.5GB
    8192 토큰: 16비트  1.1GB, 8비트(q8_0)  0.6GB, 모델 5.2GB와 합치면  6.3GB /  5.8GB
   16384 토큰: 16비트  2.3GB, 8비트(q8_0)  1.1GB, 모델 5.2GB와 합치면  7.5GB /  6.3GB
   32768 토큰: 16비트  4.6GB, 8비트(q8_0)  2.3GB, 모델 5.2GB와 합치면  9.8GB /  7.5GB
```

### 4절 : 직접해보기 8

소스코드 : NULL

명령어
```shell
nvidia-smi -l 1
```

실행 결과

```shell
Tue Sep 22 13:17:36 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 560.94                 Driver Version: 560.94         CUDA Version: 12.6     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                  Driver-Model | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4060      WDDM  |   00000000:01:00.0  On |                  N/A |
|  0%   40C    P8             N/A /  115W |    5845MiB /   8188MiB |      1%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A      1044    C+G   ...siveControlPanel\SystemSettings.exe      N/A      |
|    0   N/A  N/A      1376    C+G   ...on\153.0.4234.32\msedgewebview2.exe      N/A      |
|    0   N/A  N/A      1936    C+G   C:\Windows\System32\dwm.exe                 N/A      |
|    0   N/A  N/A      3016    C+G   ...oogle\Chrome\Application\chrome.exe      N/A      |
|    0   N/A  N/A      4524    C+G   ...CBS_cw5n1h2txyewy\TextInputHost.exe      N/A      |
|    0   N/A  N/A      6324    C+G   ...crosoft\Edge\Application\msedge.exe      N/A      |
|    0   N/A  N/A      9024    C+G   ...Programs\Microsoft VS Code\Code.exe      N/A      |
|    0   N/A  N/A      9356    C+G   ...__8wekyb3d8bbwe\WindowsTerminal.exe      N/A      |
|    0   N/A  N/A      9776    C+G   ...cw5n1h2txyewy\CrossDeviceResume.exe      N/A      |
|    0   N/A  N/A      9856    C+G   ...nt.CBS_cw5n1h2txyewy\SearchHost.exe      N/A      |
|    0   N/A  N/A     11584    C+G   ...5n1h2txyewy\ShellExperienceHost.exe      N/A      |
|    0   N/A  N/A     13096    C+G   ...ekyb3d8bbwe\PhoneExperienceHost.exe      N/A      |
|    0   N/A  N/A     13316    C+G   ...on\153.0.4234.32\msedgewebview2.exe      N/A      |
|    0   N/A  N/A     13512      C   ...\Ollama\lib\ollama\llama-server.exe      N/A      |
|    0   N/A  N/A     15760    C+G   C:\Windows\System32\ShellHost.exe           N/A      |
|    0   N/A  N/A     16576    C+G   ...2txyewy\StartMenuExperienceHost.exe      N/A      |
|    0   N/A  N/A     17124    C+G   C:\Windows\explorer.exe                     N/A      |
|    0   N/A  N/A     19028    C+G   ...oogle\Chrome\Application\chrome.exe      N/A      |
|    0   N/A  N/A     20236    C+G   ...s\System32\ApplicationFrameHost.exe      N/A      |
+-----------------------------------------------------------------------------------------+
```

### 6절 : 직접해보기 9

소스코드 : [speed.py](./speed.py)

실행 결과

```shell
qwen3:1.7b  300토큰, 초당 169.5토큰 | qwen3:1.7b    8f68893c685c    1.7 GB    100% GPU     4096       4 minutes from now    
qwen3:8b    300토큰, 초당 48.6토큰 | qwen3:8b    500a1f067a9f    5.6 GB    100% GPU     4096       4 minutes from now  
```

### 6절 : 직접해보기 9 도전

소스코드 : [speed.py](./speed.py)

변경점

- `ollama pull qwen3:14b`으로 새 모델 설치

실행 결과

```shell
qwen3:1.7b  300토큰, 초당 170.0토큰 | qwen3:1.7b    8f68893c685c    1.7 GB    100% GPU     4096       4 minutes from now    
qwen3:8b    300토큰, 초당 47.9토큰 | qwen3:8b    500a1f067a9f    5.6 GB    100% GPU     4096       4 minutes from now    
qwen3:14b   300토큰, 초당 14.0토큰 | qwen3:14b    bdbd181c33f2    10 GB    37%/63% CPU/GPU    4096       4 minutes from now
```

|모델|PROCESSOR|측정 속도|속도 상한|상한 대비|
|:---:|:---:|:---:|:---:|:---:|
|qwen3:1.7b|100% GPU|초당 169.5토큰|194|87.371%|
|qwen3:8b|100% GPU|초당 48.6토큰|52|93.461%|
|qwen3:14b|37%/63% CPU/GPU|초당 14.0토큰|null|null|

`qwen3:8b` : `qwen3:14b` = `48.6` : `14.0`

`qwen3:14b`의 속도는 `qwen3:8b`의 `28.806%`이다

### 6절 : 도전

소스코드 : [matmul.py](./matmul.py)

실행 결과

- 4000
```shell
GPU 사용 가능: True
GPU 이름: NVIDIA GeForce RTX 4060
CPU: 0.1955 초
GPU: 0.0597 초
GPU가 약 3 배 빠름
```

- 100
```shell
GPU 사용 가능: True
GPU 이름: NVIDIA GeForce RTX 4060
CPU: 0.0023 초
GPU: 0.0458 초
GPU가 약 -20 배 빠름
```

|name|size|CPU 시간| GPU 시간 | 몇 배 |
|:---:|:---:|:---:|:---:|:---:|
|Colab T4|100|0.0003초|0.0004초|약 1배|
|Colab T4|4000|1.0005초|0.0458초|약 22배|
|localhost|100|0.0023초|0.0458초|약 -20배|
|localhost|4000|0.1955초|0.0597초|약 3배|


### 8절 : 직접해보기 10

소스코드 : NULL

실행 결과

- Cline api 연동 완료

### 8절 : 직접해보기 11

소스코드 : [todo/todo.py](./todo/todo.py)

실행 결과

```md
예외처리를 종료하게 만들었음

기능 추가 후 기존 json과의 호환성 없이 크래시

기존 data재사용 불가능하게 하드코딩
```


### 9절 : 직접해보기 12

소스코드 : [calc1/calculator_console.py](./calc1/c  alculator_console.py)

소스코드 : [calc1/calculator_gui.py](./calc1/c  alculator_gui.py)

실행 결과

```md
사칙연산 계산기 만들어짐
0으로 나누기 에러처리 되어있음

console의 문제점
- SIGINT 처리 안함
```

### 9절 : 직접해보기 13

소스코드 :
- [calc2/calc.py](./calc2/calc.py)
- [calc2/main.py](./calc2/main.py)
- [calc2/README.py](./calc2/README.py)
- [calc2/test_calc.py](./calc2/test_calc.py)

실행 결과

```md
다 만든 뒤 테스트해야한다는 조건을 이해하지 못하고 모든 파일 제작 전 테스트 시도하다 무한반복함
```

### 9절 : 직접해보기 14

소스코드(동일함) :
- [calc2/calc.py](./calc2/calc.py)
- [calc2/main.py](./calc2/main.py)
- [calc2/README.py](./calc2/README.py)
- [calc2/test_calc.py](./calc2/test_calc.py)

실행 결과

```shell

```
