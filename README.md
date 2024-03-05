# Interview_LT
A simple interview question-keyword generating exe

## Purpose and Usage
Simple interview program that fetches data(questions towards the interviewee) from google forms via google sheets API, and sends this data to openAI. OpenAI extracts keywords from these questions and places them randomly on screen.
This was used in real interviews. (Check author's github webpage)

### Code abstract
- auth.py: Authrization for google sheets. Requires Google Sheets API --> json file.
- response_generator.py: Generates response from openAI, requires openai_key.
- main.py: Creates window and buttons with data passed from auth and response_generator
