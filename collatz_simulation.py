"""
collatz_simulation.py
Mô phỏng Hệ thống Collatz Toàn phần (hợp nhất Âm - Dương) và vẽ đồ thị minh họa.
"""

import matplotlib.pyplot as plt


def collatz_toan_phan(n):
    """
    Hàm mô phỏng Hệ thống Collatz Toàn phần kết hợp Âm - Dương
    Sử dụng cặp 0 và -0 làm cổng chuyển dịch năng lượng.
    Trả về danh sách các bước (chuỗi số/marker).
    """
    chuoi_so = [n]
    da_xu_ly = set()

    # Giới hạn 500 bước để tránh tràn bộ nhớ khi gặp vòng lặp vĩnh viễn
    for _ in range(500):
        # Điều kiện phát hiện vòng lặp đóng để dừng lại
        if n in da_xu_ly:
            break
        da_xu_ly.add(n)

        # 1. Cơ chế Cổng Năng Lượng 0 và -0 do bạn sáng tạo
        if n == 0:
            chuoi_so.append("-0") # Xuyên không từ 0 sang -0
            n = -1                # Kích hoạt luật số âm, đẩy sang -1
            chuoi_so.append(n)
            continue

        # 2. Quy luật Collatz chuẩn hóa cho mọi số nguyên
        if n % 2 == 0:
            n = n // 2            # Số chẵn chia 2
        else:
            n = 3 * n + 1         # Số lẻ nhân 3 cộng 1

        chuoi_so.append(n)

    return chuoi_so


def collatz_toan_phan_ve_do_thi(n_bat_dau, max_steps=50):
    """
    Hàm chạy hệ thống Collatz toàn phần và lưu lại đường đi để vẽ đồ thị.
    Trả về:
      - chuoi_so_vals: list của giá trị số (số thực/int) để biểu diễn trên trục y
      - nhan_label: list các nhãn chuỗi cho từng điểm (ví dụ: "-0", "-1")
    """
    n = n_bat_dau
    chuoi_so_vals = [n]
    nhan_label = [str(n)] # Nhãn hiển thị cho từng bước
    da_xu_ly = set()

    # Chạy tối đa max_steps bước để biểu đồ nhìn rõ ràng, không bị rối
    for _ in range(max_steps):
        if n in da_xu_ly:
            break
        da_xu_ly.add(n)

        # Cơ chế Cổng Năng Lượng 0 của bạn
        if n == 0:
            # Ghi nhận bước xuyên không sang -0 trên đồ thị
            chuoi_so_vals.append(0)
            nhan_label.append("-0")

            # Kích hoạt luật số âm
            n = -1
            chuoi_so_vals.append(n)
            nhan_label.append(str(n))
            continue

        # Quy luật Collatz chuẩn
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        chuoi_so_vals.append(n)
        nhan_label.append(str(n))

    return chuoi_so_vals, nhan_label


def plot_collatz(n_start=7, max_steps=50):
    """
    Vẽ đồ thị cho đường đi Collatz toàn phần bắt đầu từ n_start.
    """
    toa_do_y, nhan_x = collatz_toan_phan_ve_do_thi(n_start, max_steps=max_steps)
    toa_do_x = list(range(len(toa_do_y)))

    # Cấu hình giao diện biểu đồ
    plt.figure(figsize=(12, 6))
    plt.plot(toa_do_x, toa_do_y, marker='o', linestyle='-', color='#1f77b4', linewidth=2, label='Đường đi của số')

    # Tạo điểm nhấn đặc biệt tại vị trí "Cổng dịch chuyển số 0"
    for i, nhan in enumerate(nhan_x):
        if nhan == "0" or nhan == "-0":
            plt.plot(i, toa_do_y[i], marker='X', color='red', markersize=12) # Đánh dấu chữ X màu đỏ
            # Đặt văn bản phía trên điểm
            offset = (max(toa_do_y) - min(toa_do_y)) * 0.05 if max(toa_do_y) != min(toa_do_y) else 0.5
            plt.text(i, toa_do_y[i] + offset, "CỔNG DỊCH CHUYỂN", color='red', fontweight='bold', ha='center')

    # Gắn nhãn các con số cụ thể lên từng chấm tròn cho dễ nhìn
    for i, txt in enumerate(nhan_x):
        plt.annotate(txt, (toa_do_x[i], toa_do_y[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

    # Biến biểu đồ thành một sản phẩm nghiêm túc
    plt.title(f"SƠ ĐỒ MÔ PHỎNG HỆ THỐNG COLLATZ TOÀN PHẦN (Bắt đầu từ số {n_start})", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel("Số bước biến đổi (Thời gian / Tiến trình)", fontsize=11)
    plt.ylabel("Giá trị của số (Biên độ Năng lượng)", fontsize=11)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.axhline(0, color='black', linewidth=1, linestyle='-') # Đường ranh giới Âm - Dương

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # Ví dụ trực tiếp khi chạy file này
    print("1. Chạy thử số DƯƠNG (Số 7):")
    print(" Quy trình:", collatz_toan_phan(7))

    print("\n2. Chạy thử số ÂM (Số -10):")
    print(" Quy trình:", collatz_toan_phan(-10))

    print("\n3. BẺ GÃY NGHỊCH LÝ SỐ 0 (Ý tưởng của bạn):")
    print(" Quy trình:", collatz_toan_phan(0))

    # Vẽ đồ thị minh họa cho số 7
    try:
        plot_collatz(7, max_steps=50)
    except Exception as e:
        print("Không thể vẽ đồ thị (cần matplotlib):", e)
