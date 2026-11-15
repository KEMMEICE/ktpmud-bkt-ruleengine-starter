# NHẬT KÝ TIẾN ĐỘ & BẰNG CHỨNG KHẮC PHỤC (PROGRESS REPORT)
**Dự án:** Track A — Dr May Day: Rule Engine Sprint  
**Mã nhóm:** Nhóm 07  

---

## 1. Môn học / Checkpoint 1 — Khắc phục Feedback (Mục 1.2)
- **Trạng thái:** Đã hoàn thành toàn bộ các điểm cần sửa theo yêu cầu của giảng viên.
- **Bằng chứng & Nội dung khắc phục:**
  - Cập nhật lại mô tả chi tiết cho **FR-02** trong `artifacts/REQUIREMENTS.md` (chuẩn hóa định nghĩa Tầng 1 kèm theo điều kiện tụt HATT theo 4 nhóm tuổi và quy định giảm $>30\%$ đối với người $\ge 18$ tuổi).
  - Chuẩn hóa chính sách ngoại lệ và `TC-MISSING-01` bám sát tinh thần của `issue #15` (thiếu tuổi quy về trạng thái `THEO_DOI`).
  - Khắc phục lỗi định dạng Markdown (thiếu dấu đóng khối code ` ``` `) trong `artifacts/TEST_REPORT.md` và lọc bỏ các ký hiệu thừa.
  - Thêm file cấu hình `pytest.ini` (`pythonpath = .`) vào thư mục gốc để khắc phục triệt để lỗi `ModuleNotFoundError` trên cả môi trường nội bộ lẫn GitHub Actions CI.
  - **Link commit minh chứng trên fork:** `[Dán link commit trên fork của nhóm tại đây]`

---

## 2. Tiến độ Checkpoint 2 / M2 — Build & Demo (Mục 2.2)
- **Trạng thái:** Đã hoàn thiện mã nguồn chức năng và vượt qua toàn bộ kiểm thử tự động.
- **Bằng chứng & Nội dung triển khai:**
  - Hiện thực hóa hoàn chỉnh hàm `classify()` trong `rule_engine/classifier.py` tuân thủ tuyệt đối đặc tả `docs/decision-table.md` và thứ tự ưu tiên `R01 > R02 > R03`.
  - Xây dựng thành công bộ unit test tự động trong `tests/test_classifier.py` bao phủ các ca chuẩn, ranh giới và ngoại lệ.
  - Chạy thành công lệnh `pytest -q` từ clean checkout (`4 passed`).
  - Tích hợp thành công cơ chế Audit Trail tuân thủ chuẩn 4 trường bắt buộc `[Timestamp, User_UUID, Action_Type, Status]` với chính sách bảo mật Zero PII Logging.
  - **Link commit minh chứng Checkpoint 2:** `[Dán link commit trên fork của nhóm tại đây]`