# BẢNG KIỂM TRA BẢO MẬT VÀ QUYỀN RIÊNG TƯ (SECURITY & PRIVACY CHECKLIST)
**Dự án:** Track A — Dr May Day: Rule Engine Sprint  
**Mã nhóm:** Nhóm 07  

---

| STT | Tiêu chí kiểm tra bảo mật / dữ liệu | Trạng thái | Ghi chú / Minh chứng triển khai |
| :---: | :--- | :---: | :--- |
| 1 | **Cam kết dữ liệu giả lập (Synthetic Data):** Không sử dụng bất kỳ dữ liệu bệnh nhân thực tế (PII / PHI) nào trong mã nguồn và dữ liệu test. | **Đạt** | Toàn bộ fixture và test cases đều dùng dữ liệu giả lập theo `docs/decision-table.md`. |
| 2 | **Bảo mật thông tin xác thực (Secret Management):** Không chứa token, API key, mật khẩu hoặc file `.env` trong kho lưu trữ Git. | **Đạt** | Đã kiểm tra qua `git status` và `.gitignore`; không có thông tin nhạy cảm. |
| 3 | **An toàn Audit Trail (Zero PII Logging):** Đảm bảo bản ghi audit log chỉ chứa đúng 4 trường bắt buộc `[Timestamp, User_UUID, Action_Type, Status]` và không chứa triệu chứng thô. | **Đạt** | Hàm ghi log được thiết kế bộ lọc cắt tỉa payload trước khi xuất file log. |
| 4 | **Độc lập môi trường Production:** Không kết nối mã nguồn với cơ sở dữ liệu production hoặc hệ thống bên ngoài. | **Đạt** | Chạy độc lập cục bộ bằng mô hình deterministic rule engine và `pytest`. |