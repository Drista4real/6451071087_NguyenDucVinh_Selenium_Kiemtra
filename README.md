# Kiểm thử đăng nhập UTC bằng Selenium

Cài thư viện và tạo file cấu hình:

```powershell
python -m pip install -r requirements.txt
if (!(Test-Path .env)) { Copy-Item .env.example .env }
```

Điền tài khoản kiểm thử vào `.env`, sau đó chạy một testcase:

```powershell
python -m pytest tests/test_tc01.py -v
```

Cần cài Chrome. Selenium điều khiển trình duyệt; pytest chạy testcase và báo kết quả.

## Cấu trúc

- `pages/login_page.py`: kết hợp các vùng của trang đăng nhập.
- `pages/components/login_form.py`: locator và thao tác trong form.
- `pages/components/login_help.py`: các liên kết trợ giúp.
- `pages/recover_password_page.py`: locator form lấy lại mật khẩu và CAPTCHA.
- `tests/test_tc*.py`: 20 testcase.

TC14 được bỏ qua mặc định vì gửi sai mật khẩu 5 lần. Chỉ chạy riêng khi dùng tài khoản kiểm thử được phép:

```powershell
$env:RUN_TC14 = "1"
python -m pytest tests/test_tc14.py -v
```
