# OneLogistics - Automation Tests

## 🛠️ Tech Stack
- **Tool:** Playwright (Python)
- **Framework:** Pytest
- **Pattern:** Page Object Model (POM)
- **Browser:** Chromium

## 📁 Project Structure
├── pages/ # Page Objects
├── tests/ # Test Scripts
├── data/ # Test Data
└── pytest.ini # Configuration


## 🧪 Test Cases
| ID | Test Case | Type |
|----|-----------|------|
| TC-001 | Login with valid credentials | Positive |
| TC-002 | Verify login page elements | Positive |
| TC-003 | Login with invalid username | Negative |
| TC-004 | Login with invalid password | Negative |
| TC-005 | Login with empty username | Negative |
| TC-006 | Login with empty password | Negative |
| TC-007 | Login with all empty fields | Negative |
| TC-008 | Password field is masked | Security |

## 🚀 How to Run
```bash
pip install pytest-playwright
playwright install
pytest tests/test_login.py -v --headed --browser chromium


## 6.5 Push code lên GitHub

```bash
# Trong Terminal VS Code:
git init
git add .
git commit -m "Initial commit: Login automation with Playwright POM"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/onelogistics-automation.git
git push -u origin main
