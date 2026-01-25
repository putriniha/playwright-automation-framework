## 📌 Overview
This repository contains an **end-to-end test automation framework** built using **Playwright with Python and Pytest**.  
The framework is designed following **Page Object Model (POM)** principles to ensure **maintainability, readability, and scalability**.

It covers:
- UI functional testing
- Positive & Negative test scenarios
- Smoke & Regression test suites
- Parametrerized test execution

This project is intended for **learning purposes and portfolio demonstration** as a QA Automation Engineer.

## 🧰 Tech Stack
- **Language**: Python 3.11.7
- **Automation Tool**: Playwright
- **Test Framework**: Pytest 
- **Design Pattern**: Page Object Model (POM)
- **Reporting**: Pytest HTML
- **Version Control**: Git & Github

## 🧪 Test Scenarios Covered

### 🔐 Authentication
- Login with valid credentials
- Login with invalid credentials
- Login with empty username/password
- Error message validation

### 🛒 Checkout Flow
- Add product to cart
- Checkout flow
- Order confirmation validation

### 🏷️ Test Categorization
- **Smoke Tests** - Critical functionality validation
- **Regression Tests** - Full test coverage
- **Negative Tests** - Error handling & validation

## 📁 Project Structure
playwright-automation-framework/
├── pages/
│   ├── __init__.py
│   ├── cart_page.py
│   ├── checkout_complete_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
│
├── screenshots/
│
├── tests/
│   ├── __init__.py
│   ├── test_checkout_flow.py
│   ├── test_login_multiple_users.py
│   ├── test_login_negative.py
│   └── test_login_positive.py
│
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md


## ▶️ How to Run the Tests

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/putriniha/playwright-automation-framework.git
cd playwright-automation-framework 
```

### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv
```
#### Windows
```bash
venv\Scripts\activate
```
### Mac / Linux
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
playwright install
```

### 4️⃣ Run All Tests
```bash
pytest
```

### 5️⃣ Run Specific Test Suites
#### Smoke Tests
```bash
pytest -m smoke
```
#### Regression Tests
```bash
pytest -m regression
```
### Negatice Tests
```bash
pytest -m negative
```

## 🧠 Key Automation Practices Used
- Page Object Model (POM)
- Parametrized test cases
- Test tagging (smoke, regression, negative)
- Assertion best practices
- Reusable fixtures

## 🚀 Future Improvements
- CI/CD integration (GitHub Actions)
- Parallel execution
- Allure reporting
- Environment configuration support

## 👩‍💻 Author
Putri Nihayatul Husna
QA Engineer | Manual & Automation
GitHub: https://github.com/putriniha
