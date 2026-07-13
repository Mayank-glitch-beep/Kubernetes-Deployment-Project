from flask import request
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    name=request.form['name']
    return render_template(...)
 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
