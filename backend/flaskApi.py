import script_simples_calculation

from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/api/', methods=["POST"])
def main_interface():
    response = request.form['line']
    valor = script_simples_calculation.get_effective_rate(float(response))
    valor = str(valor)
    # print(response, line)
    return (valor)
if __name__ == '__main__':
    app.run(debug=True)