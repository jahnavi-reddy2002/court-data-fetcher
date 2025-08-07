import requests

def fetch_case_details(case_type, case_number, filing_year):
    url = f"http://localhost:8000/api/case/{case_type}/{case_number}/{filing_year}"
    response = requests.get(url)

    if response.status_code == 404:
        raise Exception("No case found for the given details.")
    elif response.status_code != 200:
        raise Exception("Mock API not reachable.")

    return response.json()








