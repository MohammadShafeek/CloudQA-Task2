
import json
import re
from datetime import datetime
from playwright.sync_api import sync_playwright

# Read test case
with open("test_cases.json", "r") as file:
    test_data = json.load(file)

url = test_data["url"]
test_case = test_data["test_case"].lower()

print("Test Case:", test_case)

# Initialize report
report = {
    "test_case": test_case,
    "url": url,
    "status": "FAIL",
    "message": "",
    "timestamp": datetime.now().isoformat()
}

def pass_test(message):
    report["status"] = "PASS"
    report["message"] = message
    print("PASS:", message)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        page.goto(url, wait_until="domcontentloaded", timeout=60000)

        # Verify page title
        if "title" in test_case:
            if page.title().strip():
                pass_test("Page title is not empty")
            else:
                raise AssertionError("Page title is empty")

        # Verify heading
        elif "heading" in test_case:
            headings = page.locator("h1, h2, h3")
            visible_heading = False

            for i in range(headings.count()):
                if headings.nth(i).is_visible():
                    visible_heading = True
                    break

            if visible_heading:
                pass_test("A heading is visible")
            else:
                raise AssertionError("No visible heading found")

        # Select Male gender
        elif "select male" in test_case:
            male_radio = page.locator(
                "xpath=//label[normalize-space()='Gender']/following-sibling::div//span[normalize-space()='Male']/preceding-sibling::input[@type='radio']"
            )

            male_radio.check()

            if male_radio.is_checked():
                pass_test("Male gender selected and verified")
            else:
                raise AssertionError("Male gender selection failed")

        # Select India from State dropdown
        elif "select india" in test_case and "state dropdown" in test_case:
            state_dropdown = page.locator(
                "//label[normalize-space()='State']/following-sibling::select"
            )

            state_dropdown.select_option(label="India")

            selected_value = state_dropdown.locator(
                "option:checked"
            ).inner_text()

            if selected_value.strip() == "India":
                pass_test("India selected and verified in State dropdown")
            else:
                raise AssertionError("State dropdown selection failed")

        # Enter and verify First Name
        elif "enter" in test_case and "first name" in test_case:
            match = re.search(
                r"enter\s+(.+?)\s+in the first name textbox",
                test_case
            )

            if not match:
                raise AssertionError("Could not identify the text to enter")

            expected_value = match.group(1).strip()

            first_name = page.get_by_label("First Name")
            first_name.fill(expected_value)

            actual_value = first_name.input_value()

            if actual_value == expected_value:
                pass_test("First Name entered and verified successfully")
            else:
                raise AssertionError("First Name verification failed")

        # Verify radio button
        elif "radio button" in test_case:
            radio_buttons = page.get_by_role("radio")
            visible_radio = False

            for i in range(radio_buttons.count()):
                if radio_buttons.nth(i).is_visible():
                    visible_radio = True
                    break

            if visible_radio:
                pass_test("A radio button is visible")
            else:
                raise AssertionError("No visible radio button found")

        # Verify button
        elif "button" in test_case:
            buttons = page.get_by_role("button")

            if buttons.count() > 0 and buttons.first.is_visible():
                pass_test("A button is visible")
            else:
                raise AssertionError("No visible button found")

        # Verify link
        elif "link" in test_case:
            links = page.get_by_role("link")
            visible_link = False

            for i in range(links.count()):
                if links.nth(i).is_visible():
                    visible_link = True
                    break

            if visible_link:
                pass_test("A link is visible")
            else:
                raise AssertionError("No visible link found")

        # Verify textbox
        elif "textbox" in test_case:
            textboxes = page.get_by_role("textbox")
            visible_textbox = False

            for i in range(textboxes.count()):
                if textboxes.nth(i).is_visible():
                    visible_textbox = True
                    break

            if visible_textbox:
                pass_test("A textbox is visible")
            else:
                raise AssertionError("No visible textbox found")

        # Verify dropdown
        elif "dropdown" in test_case:
            dropdowns = page.locator("select")
            visible_dropdown = False

            for i in range(dropdowns.count()):
                if dropdowns.nth(i).is_visible():
                    visible_dropdown = True
                    break

            if visible_dropdown:
                pass_test("A dropdown is visible")
            else:
                raise AssertionError("No visible dropdown found")

        # Verify website loading
        elif "page loads" in test_case:
            if page.url:
                pass_test("Website loaded successfully")
            else:
                raise AssertionError("Website did not load")

        else:
            raise AssertionError("Unsupported test instruction")

    except Exception as error:
        report["status"] = "FAIL"
        report["message"] = str(error)
        print("FAIL:", error)

    finally:
        browser.close()

# Save report
with open("report.json", "w") as file:
    json.dump(report, file, indent=4)

print("\nTest report saved successfully!")
print("Final Status:", report["status"])
