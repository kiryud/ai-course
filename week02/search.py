import ollama
import numpy as np

def emb(text):
    return np.array(ollama.embed(model="bge-m3", input=text).embeddings[0])

docs = [
    "2026 넥토리얼은 게임 프로그래머만 모집한다",
    "ai면접은 9월 12일 토요일이다",
    "팀 면접은 11월 중 진행 예정이며 지원자에 따라 다회차로 진행될 수 있다",
    "9월 7일 4시까지 서류 지원을 완료해야만 한다",
    "직군면접은 10월 중 진행될 예정이다",
    "인턴십 기간 중 모든 복지는 사원과 같다",
    "ai면접을 제외한 이후 프로세스는 대상자만 진행 가능하고 상세 일정은 대상자 개별 연락한다",
    "전형 절차는 다음과 같다. 서류접수, ai면접, ai활용 역량평가, 직군면접, 팀면접, 입사"
    "ai활용 역량평가는 10월 3일 토요일 오후 중 일괄진행된다",
    "입사는 12월 7일 월요일이다",
    "인턴십 기간은 6개월이다",
]
D = np.stack([emb(d) for d in docs])          # 문서 10개를 미리 벡터로 (10 x 1024)

def search(question, k=3):
    q = emb(question)
    sims = D @ q / (np.linalg.norm(D, axis=1) * np.linalg.norm(q))   # 문서 10개와의 코사인을 한 번에
    for i in np.argsort(-sims)[:k]:
        print(f"   {sims[i]:.3f}  {docs[i]}")

for question in ["지원 시기는 어떻게 되는거지?", "과정은 어떻게 알 수 있지?", "개발자도 할 수 있나?", "합격하면 뭘 할 수 있을까?"]:
    print("Q:", question)
    search(question)
