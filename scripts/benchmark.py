import sys
import os

# Thêm thư mục gốc (parent của thư mục scripts) vào sys.path để Python nhận diện module rule_engine
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import time
import statistics
from rule_engine.classifier import classify

def run_performance_benchmark():
    # Chuẩn bị dữ liệu đầu vào mẫu hợp lệ (synthetic data) theo Data Dictionary
    sample_input = {
        "age": 30,
        "systolic_bp": 120,
        "diastolic_bp": 80,
        "symptoms": ["chong_mat"]
    }

    print("Đang tiến hành giai đoạn Warm-up (Khởi động hệ thống)...")
    # 1. Giai đoạn Warm-up: Chạy trước 100 lần để ổn định JIT/cache/import
    for _ in range(100):
        classify(sample_input)

    latencies = []
    iterations = 1000
    print(f"Đang thực thi đo lường {iterations} lần phân loại liên tục...")

    # 2. Thực thi tối thiểu 1.000 lần liên tục và đo thời gian chính xác
    for _ in range(iterations):
        start_time = time.perf_counter()
        classify(sample_input)
        end_time = time.perf_counter()
        
        # Chuyển đổi thời gian từ giây sang mili-giây (ms)
        latency_ms = (end_time - start_time) * 1000
        latencies.append(latency_ms)

    # 3. Tính toán các chỉ số thống kê (p50 và p95)
    latencies.sort()
    p50 = statistics.median(latencies)
    
    # Tính vị trí phần trăm thứ 95 (p95)
    p95_index = int(0.95 * len(latencies))
    p95 = latencies[p95_index]

    # In kết quả ra màn hình terminal
    print("\n================ KẾT QUẢ BENCHMARK ================")
    print(f"Tổng số lần chạy: {iterations}")
    print(f"Độ trễ trung vị (p50): {p50:.4f} ms")
    print(f"Độ trễ phân vị (p95):  {p95:.4f} ms")
    print("===================================================")

    # 4. Kiểm tra điều kiện đạt yêu cầu tiêu chí A-10 (< 100 ms)
    if p95 < 100.0:
        print("✅ ĐẠT TIÊU CHÍ A-10: p95 < 100 ms")
    else:
        print("❌ KHÔNG ĐẠT: p95 vượt ngưỡng 100 ms!")
        exit(1)

if __name__ == "__main__":
    run_performance_benchmark()