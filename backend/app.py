from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    print("Received data:", data)  # Log received data for debugging

    # Extract data from the request
    age = data['age']
    retirement_age = data['retirementAge']
    salary = data['salary']
    savings_rate = data['savings']
    investment_rate = data['investments']

    # Updated growth rates
    weak_growth_rate = 0.03
    moderate_growth_rate = 0.06
    strong_growth_rate = 0.09

    # Initialize growth lists
    weak_growth = []
    moderate_growth = []
    strong_growth = []

    # Initialize current savings and investments for each scenario
    non_invested_savings = 0
    current_investment_weak = 0
    current_investment_moderate = 0
    current_investment_strong = 0

    # Calculate investment growth for each year until retirement
    for year in range(retirement_age - age + 1):
        # Add new savings to non-invested savings
        annual_savings = salary * savings_rate
        non_invested_savings += annual_savings * (1 - investment_rate)

        # Calculate the portion of savings that is invested
        annual_investment = annual_savings * investment_rate

        # Apply investment growth rates and update investments
        current_investment_weak = (current_investment_weak + annual_investment) * (1 + weak_growth_rate)
        current_investment_moderate = (current_investment_moderate + annual_investment) * (1 + moderate_growth_rate)
        current_investment_strong = (current_investment_strong + annual_investment) * (1 + strong_growth_rate)

        # Calculate total value by adding non-invested savings
        total_weak = current_investment_weak + non_invested_savings
        total_moderate = current_investment_moderate + non_invested_savings
        total_strong = current_investment_strong + non_invested_savings

        # Append the current investments to the growth lists
        weak_growth.append(total_weak)
        moderate_growth.append(total_moderate)
        strong_growth.append(total_strong)

    result = {
        'weak': weak_growth,
        'moderate': moderate_growth,
        'strong': strong_growth
    }
    print("Calculated result:", result)  # Log result for debugging
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
