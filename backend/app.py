from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    age = data['age']
    retirementAge = data['retirementAge']
    salary = data['salary']
    savingsRate = data['savingsRate']
    investmentRate = data['investmentRate']

    weak_return = 0.03
    moderate_return = 0.06
    strong_return = 0.09

    years = list(range(1, retirementAge - age + 1))
    weak = []
    moderate = []
    strong = []

    annual_savings = salary * savingsRate
    annual_investment = annual_savings * investmentRate
    annual_cash_savings = annual_savings - annual_investment

    weak_value = 0
    moderate_value = 0
    strong_value = 0

    for year in years:
        weak_value = (weak_value + annual_investment) * (1 + weak_return) + annual_cash_savings
        moderate_value = (moderate_value + annual_investment) * (1 + moderate_return) + annual_cash_savings
        strong_value = (strong_value + annual_investment) * (1 + strong_return) + annual_cash_savings

        weak.append(weak_value)
        moderate.append(moderate_value)
        strong.append(strong_value)

    result = {
        'years': [f'Year {year}' for year in years],
        'weak': weak,
        'moderate': moderate,
        'strong': strong,
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
