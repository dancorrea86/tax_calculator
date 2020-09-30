from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
 
@app.route('/')
def index(name=None):
    return render_template('index.html')

@app.route('/d')
def index1(name=None):
    return render_template('index1.html')

@app.route('/display', methods=['POST'])
def display():
    print(request.form['line'])
    return redirect(url_for('index1'))
 
if __name__ == '__main__':
    app.run()