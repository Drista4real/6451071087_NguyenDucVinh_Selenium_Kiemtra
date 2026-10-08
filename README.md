# Kiểm thử đăng nhập UTC bằng Selenium

## Cài đặt và chạy

```powershell
python -m pip install -r requirements.txt
if (!(Test-Path .env)) { Copy-Item .env.example .env }
# Điền tài khoản kiểm thử vào .env
python -m pytest tests/test_tc01.py -v
```

Cần cài Chrome. Selenium điều khiển trình duyệt; pytest chạy testcase và báo kết quả.

## Cấu trúc

- `pages/login_page.py`: kết hợp các vùng của trang đăng nhập.
- `pages/components/login_form.py`: locator và thao tác trong form.
- `pages/components/login_help.py`: các liên kết trợ giúp.
- `pages/recover_password_page.py`: locator form lấy lại mật khẩu và CAPTCHA.
- `tests/test_tc*.py`: 20 testcase.

## Kết quả chạy gần nhất

Ngày chạy: 08/10/2026 — **12 đạt, 8 chưa đạt**.

| Testcase | Kết quả | Ghi nhận |
|---|---|---|
| TC01 | Chưa đạt | Sau khi gửi form, trang vẫn hiển thị ô username. |
| TC02 | Chưa đạt | Nhấn Enter nhưng trang vẫn hiển thị ô username. |
| TC03 | Chưa đạt | Trang vẫn hiển thị ô username sau khi đăng nhập có chọn ghi nhớ. |
| TC04 | Chưa đạt | Trang vẫn hiển thị ô username sau khi đăng nhập không chọn ghi nhớ. |
| TC05 | Đạt | Hiển thị thông báo khi bỏ trống cả username và password. |
| TC06 | Đạt | Hiển thị thông báo yêu cầu username. |
| TC07 | Đạt | Hiển thị thông báo yêu cầu password. |
| TC08 | Đạt | Có thông báo lỗi khi nhập sai password. |
| TC09 | Đạt | Có thông báo lỗi khi nhập username không hợp lệ. |
| TC10 | Đạt | Có thông báo lỗi khi nhập sai cả hai thông tin. |
| TC11 | Đạt | Có thông báo lỗi khi thay đổi chữ hoa/thường của password. |
| TC12 | Chưa đạt | Username có khoảng trắng nhưng trang vẫn hiển thị form đăng nhập. |
| TC13 | Đạt | Trường password có kiểu `password`, nội dung được che. |
| TC14 | Chưa đạt | Sau 5 lần nhập sai, test không phát hiện thông báo CAPTCHA/khóa như kỳ vọng. |
| TC15 | Đạt | Payload SQL không rời khỏi form đăng nhập và có thông báo lỗi. |
| TC16 | Chưa đạt | Truy cập `/trang-chu` không chuyển URL sang `/Login`. |
| TC17 | Chưa đạt | Không tìm thấy thao tác đăng xuất sau khi gửi thông tin đăng nhập. |
| TC18 | Đạt | Trang vẫn hiển thị, không phát hiện lỗi Server 500. |
| TC19 | Đạt | Phím Tab đi qua các phần tử và tới được nút đăng nhập. |
| TC20 | Đạt | Ảnh CAPTCHA, ô mã bảo mật và ô email hiện trên trang khôi phục mật khẩu. |
