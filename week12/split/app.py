import base64, json, re
from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(base_url="https://krchoi.com/gemma4/v1", api_key="none")

def ask(prompt, image_bytes=None, mime="image/jpeg"):
    content = [{"type": "text", "text": prompt}]
    if image_bytes:
        url = f"data:{mime};base64," + base64.b64encode(image_bytes).decode()
        content.append({"type": "image_url", "image_url": {"url": url}})
    r = client.chat.completions.create(model="gemma4", messages=[{"role": "user", "content": content}])
    return r.choices[0].message.content

def parse_json(text):
    m = re.search(r"```(?:json)?\s*(.*?)```", text, re.S)
    try:
        return json.loads(m.group(1) if m else text)
    except (json.JSONDecodeError, TypeError):
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    total_amount = None
    people_count = None
    items = None

    if request.method == 'POST':
        # Case 1: Manual Input
        if 'total_amount' in request.form:
            try:
                total_amount = int(request.form.get('total_amount', 0))
                people_count = int(request.form.get('people_count', 0))

                if people_count > 0:
                    result = total_amount / people_count
                else:
                    result = "인원수는 1명 이상이어야 합니다."
            except ValueError:
                result = "숫자만 입력해주세요."

        # Case 2: Image Upload (OCR)
        elif 'receipt_image' in request.files:
            file = request.files['receipt_image']
            people_count = int(request.form.get('people_count', 1))
            
            if file and file.filename != '':
                image_bytes = file.read()
                prompt = "영수증에 있는 항목(item)과 금액(price)을 찾아 JSON 형식으로 리스트로 반환해줘. 형식: [{\"item\": \"항목명\", \"price\": 금액}, ...]"
                
                try:
                    response_text = ask(prompt, image_bytes=image_bytes)
                    items_data = parse_json(response_text)
                    
                    if items_data and isinstance(items_data, list):
                        items = items_data
                        total_amount = sum(item.get('price', 0) for item in items_data)
                        if people_count > 0:
                            result = total_amount / people_count
                        else:
                            result = "인원수는 1명 이상이어야 합니다."
                    else:
                        result = "읽지 못했습니다"
                except Exception as e:
                    print(f"Error: {e}")
                    result = "읽지 못했습니다"
            else:
                result = "이미지를 업로드해주세요."

    return render_template('index.html', result=result, total_amount=total_amount, people_count=people_count, items=items)

if __name__ == '__main__':
    app.run(debug=True)
