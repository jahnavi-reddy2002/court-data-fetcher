Court Data Fetcher & Mini Dashboard (Mock API)

A simple and educational Flask web project that simulates looking up court case details using a locally hosted fake API.

1. What does this project do?

It allows users to enter:
1. Case Type
2. Case Number
3. Filing Year

and then fetches related court case information like:
Petitioner and Respondent
Judge
Filing and Hearing Dates
Case Status
Latest Order (PDF link)

All this is fetched from a local mock API, so it's completely offline and safe.

2. Why a mock API?

The original task required fetching data from an Indian court site — which is hard to automate due to CAPTCHAs, redirects, and legal concerns.

So instead, we built a mock API using Flask to simulate court responses. This makes the project:
 Easier to run
 More reliable in demos
 Still a good technical showcase

3. What’s used in the project?

Flask – For both the web app and the mock API
Requests – To make API calls
HTML – For the form UI
Python – To tie it all together


4. What’s inside the project folder?

court-data-fetcher/
├── app.py # Main Flask web app
├── scraper.py # Talks to the mock API
├── mock_api.py # Fake API for case details
├── templates/
│ └── index.html # The web form and results page
├── requirements.txt # Package list
└── README.md # This file


5. How do I run it?

You’ll need to run two Python scripts – one for the mock API, one for the main app.

Step 1 – Start the mock API
In Terminal 1:
python mock_api.py

This runs at http://localhost:8000

Step 2 – Start the main Flask app
In Terminal 2:
python app.py

This runs at http://localhost:5000

Now open your browser and visit:
http://localhost:5000

6. What input should I use to test it?
Use the following case (which exists in the fake API):

Field                	Value
Case Type	             SCA
Case Number	           1040
Filing Year	           2020

7. What will I see?
   
A list of case details like court name, judge, next hearing date, etc.
A downloadable link to the order PDF (fake link)
Clean error message if case not found when you enter unavailable case details

7. What's in requirements.txt?

Flask
requests

You can install them with:

pip install -r requirements.txt

8. Is this legal / real court data?
No — it's just mock data for demo purposes.
You're not connecting to any real court database. It's all local and private.

