# Group03---Lab01
text = "Hôm nay trời đẹp."
with open("output.txt", "wb") as f:     # mở file ở chế độ ghi nhị phân
    f.write(text.encode("utf-8"))      # mã hóa sang UTF-8 rồi ghi bytes
