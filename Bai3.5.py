# Mở file output.txt ở chế độ 'w' (ghi đè) với encoding utf-8
with open('output.txt', 'w', encoding='utf-8') as f:
    # --- BÀI TẬP 1 ---
    f.write("--- Kết quả Bài tập 1 ---\n")
    f.write("I'm a student.\n")
    f.write("\n") # Thêm một dòng trống để phân cách

    # --- BÀI TẬP 2 ---
    f.write("--- Kết quả Bài tập 2 ---\n")
    so_thuc = 1/7
    # Định dạng chuỗi trước khi ghi
    ket_qua_bai_2 = f"{so_thuc:.5f}\n"
    f.write(ket_qua_bai_2)
    f.write("\n") # Thêm một dòng trống

    # --- BÀI TẬP 3 ---
    f.write("--- Kết quả Bài tập 3 ---\n")
    # Phần nhập liệu vẫn diễn ra trên màn hình console
    try:
        a_str = input("Nhập số nguyên a: ")
        a = int(a_str)
        b_str = input("Nhập số nguyên b: ")
        b = int(b_str)
        tong = a + b
        
        # Ghi kết quả vào file
        f.write(f"Số a đã nhập: {a}\n")
        f.write(f"Số b đã nhập: {b}\n")
        f.write(f"Tổng của a và b là: {tong}\n")
    except ValueError:
        # Nếu người dùng không nhập số, ghi thông báo lỗi vào file
        f.write("Lỗi: Dữ liệu nhập vào không phải là số nguyên.\n")
    f.write("\n")

    # --- BÀI TẬP 4 ---
    f.write("--- Kết quả Bài tập 4 ---\n")
    # Người dùng nhập tên file từ màn hình console
    filename = input("Nhập tên file cần đọc (ví dụ: data.txt): ")
    f.write(f"Đã yêu cầu đọc file: {filename}\n")

    try:
        # Mở và đọc file mà người dùng yêu cầu
        with open(filename, "r", encoding="utf-8") as file_can_doc:
            content = file_can_doc.read()
            f.write(f"--- Nội dung của file '{filename}' ---\n")
            f.write(content)
            f.write(f"\n--- Kết thúc nội dung file '{filename}' ---\n")

    except FileNotFoundError:
        f.write(f"Lỗi: File '{filename}' không tồn tại.\n")
    except Exception as e:
        f.write(f"Đã xảy ra lỗi khi đọc file: {e}\n")

# In một thông báo ra màn hình để người dùng biết chương trình đã hoàn thành
print("Đã thực hiện xong tất cả các bài tập. Vui lòng kiểm tra file output.txt để xem kết quả.")