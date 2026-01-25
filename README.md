## 📌 Overview
This project is an end-to-end (E2E) test automation framework built using Playwright 
to validate critical user flows of a web application.

The framework focuses on:
- Functional testing
- Regression testing
- Smoke testing
- Negative scenarios

It is designed with scalability, maintainability, and CI integration in mind.

## 🛠 Tech Stack
- **Playwright** – End-to-end test automation
- **Page Object Model (POM)** – Test design pattern
- **GitHub Actions** – CI/CD pipeline
- **Playwright HTML Reporter** – Test reporting

## 🧪 Test Scenarios Covered

### 🔐 Authentication
- Login with valid credentials
- Login with invalid email
- Login with incorrect password

### 🛒 Checkout Flow
- Add product to cart
- Remove product from cart
- Complete checkout process
- Handle empty cart scenario - Still in Progress

### 🚫 Negative Scenarios
- Invalid input validation
- Unauthorized access handling
- Error message verification

### 🔓 Logout - on progress to add
- Logout from authenticated session
- Redirect user to login page
- Prevent access to protected routes after logout
