
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
 
@app.route('/')
def index(name=None):
    return render_template('index.html')

data = {
    "name": "daniel"
}
@app.route('/result', methods=[ 'POST', 'GET'])
def result():
    return render_template('index1.html', data=data)

@app.route('/display', methods=['POST'])
def display():
    print(request.form['line'])
    return redirect(url_for('result'))
 
if __name__ == '__main__':
    app.run()