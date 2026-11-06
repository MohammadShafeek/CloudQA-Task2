# CloudQA Task 2 – Natural Language Browser Automation

## Project Overview

This project is a browser automation tool developed using Python and Playwright. It reads test instructions written in plain English, performs the corresponding browser actions, verifies the results, and generates a JSON test report.

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
├── .gitignore
└── venv/
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/MohammadShafeek/CloudQA-Task2.git
```

### 2. Navigate to the Project Folder

```bash
cd CloudQA-Task2
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it using Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install playwright
```

### 5. Install Chromium Browser

```bash
python -m playwright install chromium
```

## How to Run

1. Open `test_cases.json`.
2. Enter the website URL and test instruction.

Example:

```json
{
  "url": "http://app.cloudqa.io/home/AutomationPracticeForm",
  "test_case": "Select India from the State dropdown and verify the selected value"
}
```

3. Save the file.
4. Run the automation tool:

```bash
python main.py
```

5. Check `report.json` for the execution result.

## Test Report

After execution, the tool generates a JSON report containing:

- Test case description
- Website URL
- PASS/FAIL status
- Execution message
- Execution timestamp

## Approach and Limitations

The project currently uses predefined natural-language instruction patterns to identify and execute supported browser actions using Playwright.

Supported operations include:

- Website loading verification
- Page title verification
- Heading visibility verification
- Button and link visibility checks
- Textbox and radio button visibility checks
- First Name input and verification
- Gender selection and verification
- State dropdown selection and verification

**Limitations:** This is currently a rule-based prototype, not a fully AI-powered automation system. Only supported instruction patterns are recognized. Unsupported instructions may return a FAIL result.

## Author

**Mohammad Shafeek**

GitHub: https://github.com/MohammadShafeek