from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    total_amount = None
    people_count = None

    if request.method == 'POST':
        try:
            total_amount = int(request.form.get('total_amount', 0))
            people_count = int(request.form.get('people_count', 0))

            if people_count > 0:
                result = total_amount / people_count
            else:
                result = "인원수는 1명 이상이어야 합니다."
        except ValueError:
            result = "숫자만 입력해주세요."

    return render_template('index.html', result=result, total_amount=total_amount, people_count=people_count)

if __name__ == '__main__':
    app.run(debug=True)
