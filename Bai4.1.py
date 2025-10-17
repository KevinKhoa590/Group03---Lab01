#  Nhập số nguyên y. Viết biểu thức điều kiện kiểm tra xem năm y có phải là năm nhuận hay không?

y = int(input("Nhập y: "))

if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print(f"{y} là năm nhuận")
else:
    print(f"{y} không phải là năm nhuận")