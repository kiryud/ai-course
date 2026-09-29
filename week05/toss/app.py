import os
import json
import base64
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# 4. 키 - 시크릿 키 설정
TOSS_SECRET_KEY = os.environ.get("TOSS_SECRET_KEY", "test_gsk_docs_OaPz8L5KdmQXkzRz3y47BMw6")

def get_auth_header():
    """시크릿 키를 Base64로 인코딩하여 Authorization 헤더 생성"""
    auth_string = f"{TOSS_SECRET_KEY}:"
    encoded_auth = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")
    return {"Authorization": f"Basic {encoded_auth}"}

@app.route("/")
def index():
    """GET / : index.html 렌더링"""
    return render_template("index.html")

@app.route("/success")
def success():
    """GET /success : 결제 승인 처리"""
    payment_key = request.args.get("paymentKey")
    order_id = request.args.get("orderId")
    amount = request.args.get("amount")

    # 19. 승인 API를 부르기 전에 쿼리의 amount가 1000과 같은지 확인한다.
    try:
        if int(amount) != 1000:
            return render_template("success.html", error={
                "status": 400,
                "message": f"금액 불일치: 예상 1000, 실제 {amount}",
                "raw_json": json.dumps({"error": "Invalid amount"}, indent=2)
            }), 400
    except (ValueError, TypeError):
        return render_template("success.html", error={
            "status": 400,
            "message": "잘못된 금액 형식입니다.",
            "raw_json": json.dumps({"error": "Invalid amount format"}, indent=2)
        }), 400

    # 토스페이먼츠 결제 승인 API 호출
    url = "https://api.tosspayments.com/v1/payments/confirm"
    headers = get_auth_header()
    payload = {
        "paymentKey": payment_key,
        "orderId": order_id,
        "amount": amount
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response_data = response.json()

        if response.status_code == 200:
            # 승인 성공
            return render_template(
                "success.html",
                data={
                    "status": response_data.get("status"),
                    "orderName": response_data.get("orderName"),
                    "totalAmount": response_data.get("totalAmount"),
                    "method": response_data.get("method"),
                    "approvedAt": response_data.get("approvedAt")
                },
                raw_json=json.dumps(response_data, indent=2, ensure_ascii=False)
            )
        else:
            # 승인 실패 (4XX, 5XX)
            return render_template(
                "success.html",
                error={
                    "status": response.status_code,
                    "message": response_data.get("message", "Unknown error"),
                    "raw_json": json.dumps(response_data, indent=2, ensure_ascii=False)
                }
            ), response.status_code

    except Exception as e:
        return render_template(
            "success.html",
            error={
                "status": 500,
                "message": str(e),
                "raw_json": json.dumps({"error": "Internal Server Error"}, indent=2)
            }
        ), 500

@app.route("/fail")
def fail():
    """GET /fail : 실패 메시지 표시"""
    code = request.args.get("code")
    message = request.args.get("message")
    return render_template("fail.html", code=code, message=message)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
