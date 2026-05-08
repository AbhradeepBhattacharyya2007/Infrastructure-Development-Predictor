from flask import Flask, render_template, request

app = Flask(__name__)

# -------------------------------
# 🔹 COMPONENT FUNCTIONS
# -------------------------------

def get_input_data(request):
    region = request.form['region']
    roads = int(request.form['roads'])
    internet = int(request.form['internet'])
    education = int(request.form['education'])
    business = int(request.form['business'])
    return region, roads, internet, education, business


def calculate_score(roads, internet, education, business):
    return (roads + internet + education + business) // 4


def get_growth_level(score):
    if score >= 70:
        return "High"
    elif score >= 40:
        return "Medium"
    else:
        return "Low"


def detect_problems(roads, internet, education, business):
    problems = []

    if internet <= 10:
        problems.append("Weak internet connectivity")

    if education <= 10:
        problems.append("Low education accessibility")

    if roads <= 10:
        problems.append("Poor transport infrastructure")

    if business <= 10:
        problems.append("Low business activity")

    return problems


def generate_solutions(problems):
    solutions = []

    if "Weak internet connectivity" in problems:
        solutions.append("Improve digital infrastructure")

    if "Low education accessibility" in problems:
        solutions.append("Build vocational training centers")

    if "Low business activity" in problems:
        solutions.append("Encourage local entrepreneurship")

    if "Poor transport infrastructure" in problems:
        solutions.append("Develop transport systems")

    return solutions


def format_output(region, score, growth, problems, solutions):
    return {
        "region": region,
        "score": score,
        "growth": growth,
        "problems": problems,
        "solutions": solutions
    }


# -------------------------------
# 🔹 ROUTES
# -------------------------------

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze')
def analyze():
    return render_template('analyze.html')


@app.route('/result', methods=['POST'])
def result():
    region, roads, internet, education, business = get_input_data(request)

    score = calculate_score(roads, internet, education, business)
    growth = get_growth_level(score)
    problems = detect_problems(roads, internet, education, business)
    solutions = generate_solutions(problems)

    # ✅ ADD HERE
    reasons = []

    if internet < 20:
        reasons.append("Low internet reduces business connectivity")
    if education < 20:
        reasons.append("Low education reduces skilled workforce")
    if roads < 20:
        reasons.append("Poor roads slow transportation")
    if business < 20:
        reasons.append("Weak business ecosystem limits jobs")

    future_score = min(score + (100 - score) * 0.3, 100)
    future_score = int(future_score)

    return render_template(
        'result.html',
        region=region,
        score=score,
        growth=growth,
        problems=problems,
        solutions=solutions,
        roads=roads,
        internet=internet,
        education=education,
        business=business,
        reasons=reasons,
        future_score=future_score
    )


# -------------------------------
# 🔹 RUN APP
# -------------------------------

if __name__ == '__main__':
    app.run(debug=True)
