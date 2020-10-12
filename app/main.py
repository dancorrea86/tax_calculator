# Import of Flask
from flask import Flask, render_template, request

# Import modulos próprios
from scripts.script_simples_calculation import SimplesTaxCalculator

# Call the Flask in the application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simple_calc', methods=['GET','POST'])
def simple_calc():
    error=""
    if request.method == 'POST':
        attchament_choose = request.form['attachment']
        revenues_twelve_months = request.form['revenues-twelve-months']
        payroll_twelve_months = request.form['payroll-twelve-months']
        revenue_month = request.form['revenue-month']
        revenue_month_retention = request.form['revenue-month-retention']

    # validate form data
        try:
            revenues_twelve_months = float(revenues_twelve_months)
            payroll_twelve_months = float(payroll_twelve_months)
            revenue_month = float(revenue_month)
            tax_rate = link_calculator(revenues_twelve_months, attchament_choose, payroll_twelve_months, revenue_month)
            tax = str(revenue_month * (float(tax_rate)/100))
            print (tax_rate, revenue_month, tax)
        except ValueError:
            error = "Please supply both first and last name"

        else:
            return render_template('thank-you.html', data=tax_rate, tax=tax)


    return render_template('simple_calc.html', message=error)

def link_calculator(revenues_twelve_months, attchament_choose,  payroll_twelve_months, revenue_month):
    tax_rate_calculation = SimplesTaxCalculator(revenues_twelve_months, attchament_choose, payroll_twelve_months, revenue_month)
    tax_rate = str(tax_rate_calculation.get_effective_rate())
    return tax_rate


# Run the application
if __name__ == '__main__':
    app.run(debug=True)