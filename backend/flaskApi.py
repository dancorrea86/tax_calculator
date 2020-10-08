from script_simples_calculation import SimplesTaxCalculator
from flask import render_template

from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/api/', methods=["POST"])
def main_interface():
    response = request.form['line']
    response2 = request.form['line2']
    
    # valor = script_simples_calculation.SimplesTaxCalculator.get_effective_rate(float(response))

    valor = SimplesTaxCalculator(float(response), response2)
    valor2 = valor.get_effective_rate()
    print (valor2)
    
    return render_template('index.html', data=str(valor2))
    
    # str(valor2))

if __name__ == '__main__':
    app.run(debug=True)