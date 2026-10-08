# UTC Login Selenium Tests

Selenium + pytest browser tests for the 19 login test cases in the supplied CSV.
The locator choices follow the accompanying UTC login page reference: `name=username`,
`name=userpwd`, `form[action="/Login"] input.submit_login`, and
`label.check[for="persistent"]` (the checkbox input itself is hidden by the page script).

## Setup

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
# Edit .env and enter your test account credentials
$env:HOME_URL = "https://vanphongdientu.utc.edu.vn/trang-chu"
pytest
```

Chrome and a compatible Selenium Manager managed driver are required. `LOGIN_URL` defaults to the UTC login page. Override it only when testing another
environment. Tests involving successful login require the provided environment
credentials from `.env` and, where relevant, `HOME_URL`. The local `.env` file is
ignored by Git; commit only `.env.example`, which contains placeholders.

Some expected behaviors (session persistence, lockout, logout, and server-side
validation) depend on the target environment and account policy. Keep those tests
on a dedicated test account.
