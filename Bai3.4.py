# Bài tập 4: Đọc nội dung của file nếu tồn tại, hoặc báo lỗi nếu không.

def main():
    filename = input("Nhập tên file cần đọc (kèm phần mở rộng, ví dụ: data.txt): ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

            print("\n--- Nội dung của file ---")
            print(content)
            print("--- Kết thúc nội dung ---")

    except FileNotFoundError:
        print(f"Lỗi: File '{filename}' không tồn tại hoặc đường dẫn sai.")

    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{filename}'.")

    except Exception as e:
        print(f"Đã xảy ra lỗi khi đọc file: {e}")


if __name__ == "__main__":
    main()
