from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze')
def analyze():
    return render_template('analyze.html')

@app.route('/result', methods=['POST'])
def result():
    region = request.form['region']
    roads = int(request.form['roads'])
    internet = int(request.form['internet'])
    education = int(request.form['education'])
    business = int(request.form['business']

    )

    score = roads + internet + education + business

    if score >= 100:
        growth = "High Growth"
    elif score >= 60:
        growth = "Medium Growth"
    else:
        growth = "Low Growth"

    return render_template(
        'result.html',
        region=region,
        score=score,
        growth=growth
    )

if __name__ == '__main__':
    app.run(debug=True)
