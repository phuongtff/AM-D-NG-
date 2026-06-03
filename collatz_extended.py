#!/usr/bin/env python3
"""
collatz_extended.py
Hệ thống Collatz Mở rộng (giao diện GUI nhỏ + hàm lõi).
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext


def collatz_extended(n_start, max_steps=1000):
    """
    Hàm lõi: hệ Collatz mở rộng với 'cổng dịch chuyển' tại 0 -> '-0' -> -1.
    Trả về dict: {
      "start": int,
      "path": list,            # phần tử có thể là int hoặc string marker "-0"
      "steps": int,
      "peak": int or float,
      "conclusion": str
    }
    """
    n = n_start
    path = []
    visited = set()
    steps = 0
    peak = n
    conclusion = ""

    while steps < max_steps:
        # Nếu đã gặp n trước đó -> vòng lặp
        if n in visited:
            if n == 1:
                conclusion = "Hạ cánh an toàn tại Cực Dương (Vòng lặp 4 → 2 → 1)"
            elif n in (-1, -2):
                conclusion = "Hạ cánh an toàn tại Cực Âm (Vòng lặp -1 → -2)"
            else:
                conclusion = f"Rơi vào vòng lặp đóng tại số {n}"
            break

        # Ghi lại trạng thái hiện tại
        visited.add(n)
        path.append(n)

        # Teleport gate: 0 -> "-0" marker -> -1
        if n == 0:
            marker = "-0"
            # tránh lặp vô hạn qua marker
            if marker in visited:
                conclusion = "Rơi vào vòng lặp liên quan đến cổng -0"
                break
            visited.add(marker)
            path.append(marker)
            # hạ xuống -1 sau cổng
            n = -1
            steps += 1  # tính một bước cho hành động cổng
            # tiếp tục vòng lặp để xử lý -1 (n sẽ được kiểm tra ở đầu loop tiếp theo)
            continue

        # Quy tắc Collatz chuẩn cho cả số dương và số âm (theo cách bạn định nghĩa)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        # Cập nhật đỉnh nếu cần
        if isinstance(n, (int, float)) and n > peak:
            peak = n

        steps += 1

    else:
        conclusion = f"Đã đạt giới hạn {max_steps} bước (chưa phát hiện vòng lặp rõ ràng)."

    return {
        "start": n_start,
        "path": path,
        "steps": steps,
        "peak": peak,
        "conclusion": conclusion
    }

# --------- GUI nhỏ dùng tkinter ----------
def run_gui():
    def activate_system():
        raw = entry.get().strip()
        try:
            val = int(raw)
        except ValueError:
            messagebox.showerror("Lỗi dữ liệu", "Vui lòng nhập một số nguyên hợp lệ (ví dụ: 7, 0, -10).")
            return

        result = collatz_extended(val, max_steps=1000)
        display.delete('1.0', tk.END)
        display.insert(tk.END, "=== BÁO CÁO HỆ THỐNG COLLATZ MỞ RỘNG ===\n\n")
        display.insert(tk.END, f"Số bắt đầu: {result['start']}\n")
        display.insert(tk.END, f"Tổng bước: {result['steps']}\n")
        display.insert(tk.END, f"Đỉnh năng lượng: {result['peak']}\n")
        display.insert(tk.END, f"Trạng thái cuối: {result['conclusion']}\n\n")
        # Hiện đường đi dưới dạng mũi tên
        display.insert(tk.END, "Đường đi:\n")
        display.insert(tk.END, " → ".join(str(x) for x in result['path']))

    root = tk.Tk()
    root.title("Hệ thống Collatz Mở rộng")
    root.geometry("700x520")
    root.configure(bg="#f7fafc")

    tk.Label(root, text="HỆ THỐNG COLLATZ MỞ RỘNG", font=("Arial", 14, "bold"), bg="#f7fafc").pack(pady=12)

    frame = tk.Frame(root, bg="#f7fafc")
    frame.pack(pady=6)
    tk.Label(frame, text="Nhập số nguyên:", bg="#f7fafc").pack(side=tk.LEFT, padx=6)
    entry = tk.Entry(frame, width=16)
    entry.pack(side=tk.LEFT)
    entry.insert(0, "7")

    tk.Button(root, text="KÍCH HOẠT CỔNG DỊCH CHUYỂN", bg="#3182ce", fg="white",
              command=activate_system).pack(pady=8)

    display = scrolledtext.ScrolledText(root, width=82, height=22, font=("Courier New", 10))
    display.pack(padx=10, pady=10)

    # chạy thử mặc định
    activate_system()
    root.mainloop()

# --------- CLI thử nghiệm ----------
def demo_cli():
    tests = [7, 0, -10, -5]
    print("="*60)
    print("DEMO HỆ THỐNG COLLATZ MỞ RỘNG (CLI)")
    print("="*60)
    for t in tests:
        r = collatz_extended(t, max_steps=500)
        print(f"\nSố bắt đầu: {r['start']}")
        print("Đường đi:", " → ".join(str(x) for x in r['path']))
        print("Tổng bước:", r['steps'])
        print("Đỉnh:", r['peak'])
        print("Kết luận:", r['conclusion'])
        print("-"*40)

if __name__ == "__main__":
    # bạn có thể đổi thành run_gui() để khởi GUI, hoặc demo_cli() để in terminal
    run_gui()
