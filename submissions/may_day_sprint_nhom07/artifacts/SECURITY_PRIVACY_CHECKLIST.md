# SECURITY & PRIVACY CHECKLIST — TRACK A (DR MAY DAY)

**Dự án:** Track A — Dr May Day: Rule Engine Sprint  
**Mã nhóm:** Nhóm 07  

---

| STT | Tiêu chí kiểm tra bảo mật / dữ liệu | Trạng thái | Ghi chú / Minh chứng triển khai |
| :---: | :--- | :---: | :--- |
| 1 | **Cam kết dữ liệu giả lập (Synthetic Data):** Không sử dụng bất kỳ dữ liệu bệnh nhân thực tế (PII / PHI) nào trong mã nguồn và dữ liệu test. | **Đạt** | Toàn bộ fixture và test cases đều dùng dữ liệu giả lập theo `docs/decision-table.md`. |
| 2 | **Bảo mật thông tin xác thực (Secret Management):** Không chứa token, API key, mật khẩu hoặc file `.env` trong kho lưu trữ Git. | **Đạt** | Đã kiểm tra qua `git status` và `.gitignore`; không có thông tin nhạy cảm. |
| 3 | **An toàn Audit Trail (Zero PII Logging):** Đảm bảo bản ghi audit log chỉ chứa đúng 4 trường bắt buộc `[Timestamp, User_UUID, Action_Type, Status]` và không chứa triệu chứng thô. | **Đạt** | Hàm ghi log được thiết kế bộ lọc cắt tỉa payload trước khi xuất file log. |
| 4 | **Độc lập môi trường Production:** Không kết nối mã nguồn với cơ sở dữ liệu production hoặc hệ thống bên ngoài. | **Đạt** | Chạy độc lập cục bộ bằng mô hình deterministic rule engine và `pytest`. |

## 1. Kiểm tra Quản lý Dữ liệu & Quyền riêng tư (Privacy)
* **Dữ liệu giả lập:** Mọi thông tin đầu vào, test cases đều là dữ liệu synthetic, hoàn toàn tách biệt với dữ liệu y tế thực tế.
* **Chính sách Zero PII Logging:** Tuyệt đối không lưu trữ định danh cá nhân (PII), thông tin sức khỏe nhạy cảm hay triệu chứng thô vào tệp log của hệ thống.

## 2. Kiểm toán Audit Trail (Tiêu chuẩn A-06)
* Mọi bản ghi kiểm toán sinh ra sau khi gọi hàm `classify()` đều tuân thủ cấu trúc chuẩn gồm đúng 4 trường:
  $$\text{[Timestamp, User_UUID, Action_Type, Status]}$$

## 3. Bảo mật Mã nguồn & Xử lý Ngoại lệ
* Đã xử lý triệt để các ca thiếu dữ liệu đầu vào (như thiếu tuổi quy về trạng thái `THEO_DOI` an toàn theo `issue #15`), tránh làm sập hệ thống (crash).
* Đảm bảo không để lộ khóa bí mật hay cấu hình môi trường nhạy cảm trên kho lưu trữ Git.

## 4. Tuyên bố Miễn trừ Trách nhiệm
* Sản phẩm phục vụ mục đích học tập và nghiên cứu: *"Educational/Synthetic — Not for clinical use"*.