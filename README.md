# CloudQA Task 2 – Natural Language Browser Automation

## Project Overview
This project is a browser automation tool built using Python and Playwright. It reads a test instruction written in plain English, performs the corresponding browser action, verifies the result, and generates a JSON test report.

## Technologies Used
- Python
- Playwright
- JSON

## Project Structure
```text
CloudQA-Task2/
│
├── main.py
├── test_cases.json
├── report.json
├── README.md
└── venv/
```

## Setup Instructions

1. Clone the repository:
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Open the project folder:
```bash
cd CloudQA-Task2
```

3. Create and activate a virtual environment:
```bash
python -m venv venv
```

Windows PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```

4. Install dependencies:
```bash
pip install playwright
```

5. Install Chromium:
```bash
python -m playwright install chromium
```

## How to Run

1. Open `test_cases.json`.
2. Set the website URL and test instruction.

Example:
```json
{
  "url": "http://app.cloudqa.io/home/AutomationPracticeForm",
  "test_case": "Select India from the State dropdown and verify the selected value"
}
```

3. Run:
```bash
python main.py
```

4. Check `report.json` for the test result.

## Test Report
The tool generates a JSON report containing:
- Test case
- Website URL
- PASS/FAIL status
- Result message
- Execution timestamp

## Approach and Limitations
The current implementation uses Playwright with predefined natural-language instruction patterns to identify and execute supported browser actions. It supports selected visibility checks and form interactions.

It is a rule-based prototype, not a fully AI-powered system. Instructions outside the supported patterns may not execute and can return FAIL.

## Author
Mohammad Shafeek