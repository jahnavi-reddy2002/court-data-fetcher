from flask import Flask, render_template, request
from scraper import fetch_case_details

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    case_data = None
    error = None

    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        filing_year = request.form['filing_year']

        try:
            case_data = fetch_case_details(case_type, case_number, filing_year)
        except Exception as e:
            error = str(e)

    return render_template('index.html', case_data=case_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
