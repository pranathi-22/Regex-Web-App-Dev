from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = re.findall(regex_pattern, test_string)
    return render_template('results.html', matches=matches)

@app.route('/validate-email', methods=['POST'])
def validate_email():
    email = request.form['email']
    is_valid = bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))
    return render_template('email_validation.html', email=email, is_valid=is_valid)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)