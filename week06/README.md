# 6주차 확인 과제

> 정리가 명시된 항목 없음

---

### 1절 : 직접해보기 1

소스코드 : [vague.py](./vague.py)

실행 결과

```shell
--- 1회
def format_phone_number(phone_str):
def extract_digits(phone_str):
def remove_hyphens(phone_str):
--- 2회
def clean_phone_number(phone):
def only_digits(phone):
def clean_phone_list(phone_list):
--- 3회
def format_phone_number(phone_str, mode='hyphen'):
--- 4회
def clean_phone_number(phone):
def format_phone_number(phone):
--- 5회
def format_phone_number(phone):
def clean_phone_number(phone):
def format_phone_series(series):
```

[vague_log](./vague_log.md)

### 2절 : 직접해보기 2

소스코드 :
- [evalprompt.py](./evalprompt.py)
- [p1.txt](./p1.txt)

실행 결과

- [out_1.py](./out_1.py)
- [out_2.py](./out_2.py)
- [out_3.py](./out_3.py)
- [out_4.py](./out_4.py)
- [out_5.py](./out_5.py)

```shell
1회: 0/10  normalize_phone 없음. 있는 함수: ['format_phone_number']
2회: 0/10  normalize_phone 없음. 있는 함수: ['clean_phone_number']
3회: 0/10  normalize_phone 없음. 있는 함수: ['format_phone_number']
4회: 0/10  normalize_phone 없음. 있는 함수: ['format_phone_number']
5회: 0/10  normalize_phone 없음. 있는 함수: ['format_phone_number']
평균 0.0/10
```

### 2절 : 직접해보기 3

소스코드 :
- [evalprompt.py](./evalprompt.py)
- [p1.txt](./p1.txt)
- [p2.txt](./p2.txt)
- [p3.txt](./p3.txt)
- [p4.txt](./p4.txt)

실행 결과

- [evalprompt_log](./evalprompt_log.md)

|파일|추가한 것|평균 통과 수|실패한 입력|
|:---:|:---:|:---:|:---:|
|p1.txt|(한 줄 요청)|0|normalize_phone 없음.|
|p2.txt|함수 이름, 결과 형식, 출력 형식|4.4|'+82 10-1234-5678' -> '+82 10-1234-5678'|
||||'011-123-4567' -> '011-1234-567'|
||||'02-123-4567' -> '02-123-4567'|
||||'010-1234-567' -> '010-1234-567'|
||||'010-abcd-5678' -> '010-abcd-5678'|
||||'' -> ''|
|p3.txt|규칙 목록|9|'010-1234-567' -> '010-123-4567'|
|p4.txt|실패에서 찾은 규칙 수정|10||

### 2절 : 직접해보기 4

소스코드 : [eval2.py](./eval2.py)

실행 결과

- [eval2_log](./eval2_log.md)

이상하게 중복 코드 창조하다 터진다

### 3절 : 직접해보기 5

소스코드 : [SPEC.md](./todo/SPEC.md)

실행 결과



### 4절 : 직접해보기 6

소스코드 : 
실행 결과

```shell

```

### 4절 : 직접해보기 7

소스코드 : 

실행 결과

```shell

```

### 5절 : 직접해보기 8

소스코드 :

실행 결과

```shell

```

### 5절 : 직접해보기 9

소스코드 :

실행 결과

```shell

```

### 5절 : 직접해보기 10

소스코드 :

실행 결과

```shell

```

### 6절 : 직접해보기 11

소스코드 :

실행 결과

```shell

```

### 6절 : 직접해보기 12

소스코드 :

실행 결과

```shell

```

### 7절 : 직접해보기 13

소스코드 :

실행 결과

```shell

```

### 9절 : 직접해보기 14

소스코드 :

실행 결과

```shell

```

### 9절 : 직접해보기 15

소스코드 :

실행 결과

```shell

```
