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
