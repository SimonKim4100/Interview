# Interview_LT
A simple interview question-keyword generating exe <br>
Built with python

## Purpose and Usage
Simple interview program that fetches data(questions towards the interviewee) from google forms via google sheets API, and sends this data to openAI. OpenAI extracts keywords from these questions and places them randomly on screen.
This was used in real interviews. (Check author's github webpage)

### Code abstract
- auth.py: Authrization for google sheets. Requires Google Sheets API --> json file.
- response_generator.py: Generates response from openAI, requires openai_key.
- main.py: Creates window and buttons with data passed from auth and response_generator
- assistant(optional): This is an optional file. Replace response_generator with this if you want to use an assistant instead. For more info on assistants, check OpenAI.

## Misc
exe in dist is created with pyinstaller<br>
pyinstaller --onefile /path/to/yourscript.py<br>
For more information, check pyinstaller
