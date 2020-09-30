# #!/usr/bin/env python
  
# from flask import Flask
# from flask import request
# from flask import render_template
# from flask import redirect, url_for
  
    
# app = Flask(__name__)
  
# @app.route('/')
# def index():
#     return render_template('index.html')
 
# @app.route('/display', methods=['POST'])
# def display():
#     return redirect(url_for('index'))

 
# if __name__ == '__main__':
#     # app.debug = True
#     app.run(host='0.0.0.0')

from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run()