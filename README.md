# UTC Login Selenium Tests

Selenium + pytest browser tests for the 19 login test cases in the supplied CSV.
The locator choices follow the accompanying UTC login page reference: `name=username`,
`name=userpwd`, `input.submit__login`, and `id=persistent`.

## Setup

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:HOME_URL = "https://vanphongdientu.utc.edu.vn/trang-chu"
$env:TEST_USERNAME = "your-test-account"
$env:TEST_PASSWORD = "your-test-password"
pytest
```

Chrome and a compatible Selenium Manager managed driver are required. `LOGIN_URL` defaults to the UTC login page. Override it only when testing another
environment. Tests involving successful login require the provided environment
credentials and, where relevant, `HOME_URL`.

Some expected behaviors (session persistence, lockout, logout, and server-side
validation) depend on the target environment and account policy. Keep those tests
on a dedicated test account.
