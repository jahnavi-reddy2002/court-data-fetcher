from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/case/<case_type>/<int:case_number>/<int:filing_year>', methods=['GET'])
def get_case(case_type, case_number, filing_year):
    if case_type == 'SCA' and case_number == 1040 and filing_year == 2020:
        return jsonify({
            "caseType": "SCA",
            "caseNumber": 1040,
            "caseYear": 2020,
            "caseStatus": "Pending",
            "petitioner": "ABC Pvt Ltd",
            "respondent": "State of Gujarat",
            "filingDate": "2020-01-10",
            "nextHearingDate": "2025-08-15",
            "courtName": "Gujarat High Court",
            "judge": "Justice D. R. Mehta",
            "latestOrderPDF": "https://example.com/order.pdf"
        })
    else:
        return jsonify({"error": "Case not found"}), 404

if __name__ == '__main__':
    app.run(port=8000)
