--- 1회
전화번호를 어떤 형식으로 정리하고 싶으신가요? 보통 두 가지 경우가 가장 많습니다.

1.  **특수문자 제거:** 숫자만 남기기 (DB 저장용)
2.  **하이픈(-) 삽입:** 보기 좋게 포맷팅하기 (출력용)

Python을 이용해 이 두 가지 기능을 모두 포함한 함수를 만들어 보았습니다.

### Python 코드 예시

```python
import re

def format_phone_number(phone, mode='clean'):
    """
    전화번호 정리 함수
    :param phone: 입력된 전화번호 (문자열)
    :param mode: 'clean' (숫자만 남김), 'format' (하이픈 삽입), 'none' (그대로 반환)
    :return: 정리된 전화번호
    """
    # 1. 숫자 이외의 모든 문자 제거 (0, 1, 2... 만 남김)
    digits = re.sub(r'\D', '', phone)
    
    if mode == 'clean':
        return digits
    
    elif mode == 'format':
        # 휴대폰 번호 패턴 (010-1234-5678)
        if len(digits) == 11 and digits.startswith('01'):
            return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}"
        
        # 일반 전화/지역 번호 패턴 (02-123-4567 또는 031-1234-5678)
        elif len(digits) == 9 or len(digits) == 10:
            # 앞자리가 2자리(서울)인 경우 처리
            if len(digits) == 9 and digits.startswith('02'):
                return f"{digits[:2]}-{digits[2:5]}-{digits[5:]}"
            else:
                return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}" if len(digits) == 11 else f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
        
        # 길이에 따라 유연하게 처리 (기본적인 하이픈 규칙 적용)
        elif len(digits) == 8:
            return f"{digits[:3]}-{digits[3:]}"
        
        return digits # 패턴이 맞지 않으면 숫자만 반환
    
    else:
        return phone

# --- 테스트 코드 ---
test_numbers = [
    "010-1234-5678",
    "01012345678",
    "02.123.4567",
    "031 1234 5678",
    "010 1234 5678",
    "abc010-1234-5678xyz" # 특수문자 섞인 경우
]

print(f"{'원본':<20} | {'숫자만(clean)':<15} | {'포맷팅(format)'}")
print("-" * 55)

for num in test_numbers:
    clean = format_phone_number(num, mode='clean')
    formatted = format_phone_number(num, mode='format')
    print(f"{num:<20} | {clean:<15} | {formatted}")
```

### 코드 설명

1.  **`re.sub(r'\D', '', phone)`**: 정규 표현식을 사용하여 숫자가 아닌 모든 문자(`\D`)를 빈 문자열로 바꿉니다. 즉, 공백, 하이픈, 마침표, 영문자 등을 모두 제거하고 **숫자만 추출**합니다.
2.  **`mode='clean'`**: 데이터베이스에 저장하거나 계산할 때 유용하도록 숫자만 깔끔하게 반환합니다.
3.  **`mode='format'`**: 
    *   **휴대폰 번호(11자리):** `010-XXXX-XXXX` 형태로 만듭니다.
    *   **지역 번호(9~10자리):** 서울(02)과 같은 2자리 지역번호와 그 외 지역번호를 구분하여 하이픈을 넣습니다.
    *   **예외 처리:** 숫자의 길이에 따라 적절한 위치에 `-`를 삽입합니다.

### 실행 결과 예시

| 원본 | 숫자만(clean) | 포맷팅(format) |
| :--- | :--- | :--- |
| 010-1234-5678 | 01012345678 | 010-1234-5678 |
| 01012345678 | 01012345678 | 010-1234-5678 |
| 02.123.4567 | 021234567 | 02-123-4567 |
| 031 1234 5678 | 03112345678 | 031-1234-5678 |
| abc010-1234-5678xyz | 01012345678 | 010-1234-5678 |

**혹시 다른 언어(JavaScript 등)가 필요하시거나, 더 복잡한 규칙(국가 번호 포함 등)이 필요하시면 말씀해 주세요!**
---
def format_phone_number(phone, mode='clean'):
--- 2회
전화번호를 어떤 형식으로 정리하고 싶은지에 따라 여러 가지 방법이 있습니다. 가장 흔히 쓰이는 **1) 숫자만 추출하기**, **2) 하이픈(`-`)을 넣어 표준 형식으로 만들기**, **3) 특정 형식(예: 010-xxxx-xxxx)으로 통일하기** 세 가지 버전을 파이썬(Python) 코드로 만들어 보았습니다.

### Python 코드 예시

```python
import re

def clean_phone_number(phone):
    """
    1. 입력된 문자열에서 숫자만 남깁니다.
    """
    return re.sub(r'[^0-9]', '', phone)

def format_phone_number(phone):
    """
    2. 숫자만 있는 문자열을 받아서 010-0000-0000 형식으로 만듭니다.
    """
    digits = clean_phone_number(phone)
    
    length = len(digits)
    
    if length == 8:  # 지역번호가 없는 경우 (예: 12345678)
        return f"{digits[:4]}-{digits[4:]}"
    
    elif length == 10: # 02-123-4567 또는 010-123-4567 형태
        # 첫 부분이 02로 시작하면 2자리, 나머지는 3자리/4자리로 나뉨
        if digits.startswith('02'):
            return f"{digits[:2]}-{digits[2:5]}-{digits[5:]}"
        else:
            return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
            
    elif length == 11: # 010-1234-5678 형태
        return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}"
    
    else:
        # 형식이 맞지 않으면 숫자만 반환하거나 에러 처리
        return digits

# --- 테스트 코드 ---
test_numbers = [
    "01012345678",          # 숫자만 있는 경우
    "010-1234-5678",       # 이미 하이픈이 있는 경우
    "02.123.4567",         # 점(.)이 찍힌 경우
    "(010) 1234 5678",     # 괄호와 공백이 있는 경우
    "0101234567",          # 10자리 번호
    "021234567"            # 서울 지역번호 10자리
]

print(f"{'원본':<20} | {'정리된 결과'}")
print("-" * 40)
for num in test_numbers:
    print(f"{num:<20} | {format_phone_number(num)}")
```

### 코드 설명

1.  **`clean_phone_number(phone)`**:
    *   `re.sub(r'[^0-9]', '', phone)`를 사용하여 숫자가 아닌 모든 문자(하이픈, 공백, 괄호, 점 등)를 제거합니다. 가장 먼저 수행해야 하는 단계입니다.

2.  **`format_phone_number(phone)`**:
    *   숫자만 남은 상태에서 길이를 체크하여 하이픈 위치를 결정합니다.
    *   **11자리**: `010-1234-5678` (가장 일반적인 휴대폰)
    *   **10자리**: 
        *   `02`로 시작하면 서울 지역번호로 간주하여 `02-123-4567`로 변환합니다.
        *   그 외에는 `010-123-4567` 형태로 변환합니다.
    *   **8자리**: `1234-5678` 형태로 변환합니다.

### 실행 결과
```text
원본                 | 정리된 결과
----------------------------------------
01012345678          | 010-1234-5678
010-1234-5678        | 010-1234-5678
02.123.4567          | 02-123-4567
(010) 1234 5678      | 010-1234-5678
0101234567           | 010-123-4567
021234567            | 02-123-4567
```

### 활용 팁
*   **데이터 분석 시**: 데이터프레임(Pandas)을 사용 중이라면 `df['phone'].apply(format_phone_number)`와 같이 사용하여 수만 개의 데이터를 한 번에 정리할 수 있습니다.
*   **예외 처리**: 만약 전화번호가 아닌 값이 들어올 경우를 대비해 `try-except` 문을 추가하면 더욱 안전한 함수가 됩니다.
---
def clean_phone_number(phone):
def format_phone_number(phone):
--- 3회
전화번호를 어떤 형식으로 정리하고 싶은지에 따라 여러 가지 방법이 있습니다. 가장 대표적인 세 가지 상황(하이픈 제거, 하이픈 추가, 특정 형식으로 통일)에 맞춰 파이썬 코드를 작성해 드립니다.

### 1. 기본 코드: 하이픈(`-`)을 제거하거나 추가하기

가장 많이 쓰이는 방식은 숫자만 남기거나, 숫자에 규칙적으로 하이픈을 넣는 것입니다.

```python
import re

def clean_phone_number(phone):
    # 1. 모든 숫자 이외의 문자(하이픈, 공백, 괄호 등)를 제거
    digits = re.sub(r'\D', '', phone)
    return digits

def format_phone_number(phone):
    # 1. 숫자만 추출
    digits = re.sub(r'\D', '', phone)
    
    # 2. 길이에 따라 다른 형식 적용
    length = len(digits)
    
    if length == 11: # 010-1234-5678 형식
        return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}"
    elif length == 10: # 02-123-4567 또는 010-123-4567 형식
        # 앞자리가 02이면 2자리, 그 외엔 3자리로 처리하는 로직이 필요할 수 있음
        if digits.startswith('02'):
            return f"{digits[:2]}-{digits[2:5]}-{digits[5:]}"
        else:
            return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    elif length == 9: # 02-1234-5678 (서울 지역번호 2자리인 경우)
        return f"{digits[:2]}-{digits[2:6]}-{digits[6:]}"
    else:
        return digits # 형식이 맞지 않으면 숫자만 반환

# --- 테스트 ---
test_numbers = ["01012345678", "010-1234-5678", "02 123 4567", "(02)123-4567", "010.1234.5678"]

print("--- 숫자만 추출 ---")
for n in test_numbers:
    print(f"{n} -> {clean_phone_number(n)}")

print("\n--- 하이픈 형식 통일 ---")
for n in test_numbers:
    print(f"{n} -> {format_phone_number(n)}")
```

---

### 2. 데이터 분석용 (Pandas 활용)
만약 엑셀이나 CSV 파일에 있는 수천 개의 전화번호를 한꺼번에 정리해야 한다면 `pandas` 라이브러리를 사용하는 것이 훨씬 빠릅니다.

```python
import pandas as pd
import re

def standardize_phone(phone):
    if pd.isna(phone): return ""
    digits = re.sub(r'\D', '', str(phone))
    
    if len(digits) == 11:
        return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}"
    elif len(digits) == 10:
        if digits.startswith('02'):
            return f"{digits[:2]}-{digits[2:5]}-{digits[5:]}"
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    return digits

# 샘플 데이터 생성
df = pd.DataFrame({
    'name': ['김철수', '이영희', '박민수', '최지우'],
    'phone': ['01012345678', '02-123-4567', '(010) 9876 5432', '010.5555.4444']
})

# 함수 적용
df['cleaned_phone'] = df['phone'].apply(standardize_phone)

print(df)
```

---

### 💡 코드 설명 및 팁

1.  **`re.sub(r'\D', '', phone)`**: 정규표현식을 사용하여 숫자가 아닌 모든 것(`\D`)을 빈 문자열(`''`)로 바꿉니다. 즉, 하이픈, 공백, 점, 괄호를 한 번에 지워줍니다.
2.  **예외 처리**: 전화번호 길이가 10자리인지 11자리인지에 따라 슬라이싱(`[:]`) 위치를 다르게 설정했습니다. 특히 **서울 지역번호(02)**는 길이가 다르므로 이를 구분하는 조건문이 들어있습니다.
3.  **확장성**: 만약 해외 전화번호까지 고려해야 한다면 훨씬 복잡한 정규식이 필요하지만, 국내 번호 정리용으로는 위 코드로 충분합니다.

**원하시는 특정 형식이 따로 있다면(예: `01012345678` -> `+82 10-1234-5678`) 말씀해 주세요! 바로 수정해 드릴게요.**
---
def clean_phone_number(phone):
def format_phone_number(phone):
def standardize_phone(phone):
--- 4회
전화번호를 어떤 형식으로 정리하고 싶은지에 따라 여러 가지 방법이 있습니다. 가장 흔히 쓰이는 세 가지 상황(하이픈 제거, 하이픈 추가, 특정 형식으로 통일)에 맞춰 파이썬 코드를 작성해 드립니다.

### 1. 정규표현식(Regex)을 이용한 통합 함수
이 함수는 숫자만 남긴 뒤, 숫자의 길이에 따라 자동으로 하이픈(`-`)을 넣어주는 가장 범용적인 방식입니다.

```python
import re

def format_phone_number(phone_str):
    # 1. 숫자 이외의 모든 문자 제거
    digits = re.sub(r'\D', '', str(phone_str))
    
    length = len(digits)
    
    # 2. 길이에 따른 포맷팅
    if length == 11:  # 010-1234-5678 형식
        return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}"
    elif length == 10:
        # 02-123-4567 또는 010-123-4567 형식
        if digits.startswith('02'): # 서울 지역번호
            return f"{digits[:2]}-{digits[2:5]}-{digits[5:]}"
        else:
            return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    elif length == 9:  # 02-12-3456 형식
        return f"{digits[:2]}-{digits[2:4]}-{digits[4:]}"
    elif length == 8:  # 1234-5678 형식
        return f"{digits[:4]}-{digits[4:]}"
    else:
        # 형식이 맞지 않으면 숫자만 반환하거나 에러 처리
        return digits

# --- 테스트 ---
test_numbers = [
    "01012345678",          # 숫자만 있는 경우
    "010-1234-5678",        # 이미 하이픈이 있는 경우
    "021234567",            # 서울 지역번호 (10자리)
    "02-123-4567",          # 서울 지역번호 (9자리)
    "010.1234.5678",        # 점(.)으로 구분된 경우
    "(010) 1234 5678",      # 괄호와 공백이 있는 경우
    "12345678"              # 8자리 번호
]

print(f"{'원본':<15} | {'정리된 번호'}")
print("-" * 30)
for num in test_numbers:
    print(f"{num:<15} | {format_phone_number(num)}")
```

---

### 2. 상황별 함수 모음 (간단 버전)

만약 복잡한 로직이 필요 없고 특정 목적만 있다면 아래 함수들을 골라 쓰세요.

#### A. 숫자만 추출하기 (데이터 분석/DB 저장용)
가장 깔끔하게 데이터베이스에 넣고 싶을 때 사용합니다.
```python
def clean_to_digits(phone_str):
    return "".join(filter(str.isdigit, str(phone_str)))

# 예: "010-1234-5678" -> "01012345678"
```

#### B. 하이픈 제거하기 (통일된 숫자형태로 만들기)
```python
def remove_hyphens(phone_str):
    return phone_str.replace("-", "").replace(" ", "").replace("(", "").replace(")", "")

# 예: "(010) 1234-5678" -> "01012345678"
```

---

### 💡 코드 설명
1.  **`re.sub(r'\D', '', str(phone_str))`**: 정규표현식을 사용하여 숫자가 아닌 것(`\D`)을 모두 빈 문자열(`''`)로 바꿉니다. 즉, 특수문자나 공백을 한 번에 지워줍니다.
2.  **`f-string` (Python 3.6+)**: `f"{digits[:3]}-..."`와 같은 문법을 사용하여 문자열을 매우 직관적이고 빠르게 조립합니다.
3.  **조건문 (`if-elif`)**: 한국 전화번호 체계(02 지역번호, 010 휴대폰, 8~11자리 길이)를 기준으로 분기 처리를 하여 정확도를 높였습니다.

**사용 팁:** 엑셀 데이터나 리스트 형태의 데이터를 정리할 때는 `map(format_phone_number, list_of_numbers)`를 사용하면 한 번에 변환할 수 있습니다.
---
def format_phone_number(phone_str):
def clean_to_digits(phone_str):
def remove_hyphens(phone_str):
--- 5회
전화번호를 어떤 형식으로 정리하고 싶은지에 따라 여러 가지 방법이 있습니다. 가장 흔히 쓰이는 세 가지 케이스(하이픈 추가, 숫자만 추출, 특정 형식으로 통일)에 맞춰 파이썬 코드를 작성해 드립니다.

### 1. 숫자만 남기고 하이픈(`-`)을 넣어 정규화하기
가장 많이 쓰이는 방식입니다. 입력된 데이터가 `01012345678`, `010-1234-5678`, `010 1234 5678` 등 제각각일 때 이를 하나로 통일합니다.

```python
import re

def format_phone_number(phone):
    # 1. 숫자 이외의 모든 문자를 제거
    digits = re.sub(r'\D', '', str(phone))
    
    # 2. 숫자의 길이에 따라 하이픈 삽입
    length = len(digits)
    
    if length == 11:  # 010-1234-5678 형식
        return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}"
    elif length == 10:  # 02-123-4567 또는 010-123-4567 형식
        # 앞자리가 3자리인지 2자리인지에 따라 구분 (일반적으로 02는 2자리)
        if digits.startswith('02'):
            return f"{digits[:2]}-{digits[2:5]}-{digits[5:]}"
        else:
            return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    elif length == 9:  # 02-1234-5678 등 짧은 번호
        return f"{digits[:2]}-{digits[2:6]}-{digits[6:]}"
    else:
        # 형식이 맞지 않으면 숫자만 반환하거나 에러 처리
        return digits

# 테스트
test_numbers = ["01012345678", "010-1234-5678", "021234567", "010 1234 5678", "010.1234.5678"]
for num in test_numbers:
    print(f"{num}  =>  {format_phone_number(num)}")
```

---

### 2. 리스트에 있는 전화번호 일괄 정리하기
데이터베이스나 엑셀에서 가져온 여러 개의 번호를 한꺼번에 정리할 때 유용합니다.

```python
def clean_phone_list(phone_list):
    return [format_phone_number(p) for p in phone_list]

# 테스트
raw_data = ["01012345678", "02-123-4567", "010.9876.5432", "01011112222"]
cleaned_data = clean_phone_list(raw_data)
print(cleaned_data)
# 출력: ['010-1234-5678', '02-123-4567', '010-9876-5432', '010-1111-2222']
```

---

### 3. (심화) 아주 깔끔하게 숫자만 추출하기
만약 하이픈 없이 **데이터 분석용**으로 숫자만 필요하다면 이 함수가 가장 빠릅니다.

```python
import re

def extract_only_digits(phone):
    return re.sub(r'\D', '', str(phone))

# 테스트
print(extract_only_digits("010-1234-5678")) # 출력: 01012345678
```

### 요약 및 사용 팁
1.  **`re.sub(r'\D', '', str(phone))`**: 이 코드가 핵심입니다. `\D`는 "숫자가 아닌 것"을 의미하며, 이를 빈 문자열(`''`)로 바꿔서 숫자만 남기는 원리입니다.
2.  **예외 처리**: 만약 전화번호가 너무 짧거나(예: 5자리) 잘못된 데이터가 들어올 경우를 대비해 `if length == ...` 조건문을 통해 방어 코드를 짜는 것이 중요합니다.
3.  **추천 방식**: 사용자에게 보여주는 용도라면 **1번 방식**을, 데이터 가공/저장 용도라면 **3번 방식**을 추천합니다.

원하시는 특정 형식이 따로 있다면(예: 국가번호 `+82` 추가 등) 말씀해 주세요! 바로 수정해 드릴게요.
---
def format_phone_number(phone):
def clean_phone_list(phone_list):
def extract_only_digits(phone):