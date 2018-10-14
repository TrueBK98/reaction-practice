from combat import *
from inventory import *
items.append(medkit)
player = {
    "NAME": "Unknown",
    "HP": 100,
    "STR": 8,
    "AGI": 15,
    "DEF": 8,
}
wolf = {
    "NAME": "Sói xám",
    "HP": 100,
    "STR": 10,
    "AGI": 20,
    "DEF": 7,
}
print("Đêm gió rét thổi lạnh, ánh trăng mờ, cạnh một khu rừng vắng vẻ, bạn đang đứng trước cổng một căn nhà gỗ")
print("Cánh cổng gỗ cũ kỹ, mục nát đang hé mở")
while True:
    print("Bạn sẽ:\n"
          "1. Đẩy cổng đi và đi vào\n"
          "2. Quay lưng và đi về khu rừng phía sau lưng")
    choice = input(">>>")
    if choice == "1":
        contin = 1
        print("Bạn đưa tay đẩy cánh cửa mục nát, kêu kẽo kẹ và kéo mở, bạn bước vào cổng")
        break
    elif choice == "2":
        print("Bạn bước chân vào bìa rừng, không gian tĩnh lặng, chỉ có tiếng côn trùng kêu rà rịch")
        print("Có một lực cản vô hình khiến bạn không thể tiến sâu thêm đươc")
    else:
        print("Đánh lại đê!")
while True:
    print("Bạn sẽ:\n"
          "1. Nhìn xung quanh\n"
          "2. Đi tiếp vào trong")
    choice = input(">>>")
    if choice == "1":
        print("Hai bên lối đi là vườn hoa đã héo úa, không còn sinh khí\n"
              "Bên cạnh một khóm hoa héo úa, có một tảng đá lớn, khắc dòng chữ đỏ:\n"
              "x = (5**2) + 3\n"
              "y = x + 100\n"
              "Trước mặt bạn là một cánh cửa sắt, cánh cửa được khóa bởi khóa điện tử")
        break
    elif choice == "2":
        print("Trước mặt bạn là một cánh cửa sắt, cánh cửa được khóa bởi khóa điện tử")
        break
    else:
        print("Đánh lại đê!")
while True:
    print("Bạn sẽ:\n"
          "1. Nhìn xung quanh\n"
          "2. Đi tiếp vào trong")
    choice = input(">>>")
    if choice == "1":
        print("Hai bên lối đi là vườn hoa đã héo úa, không còn sinh khí\n"
              "Bên cạnh một khóm hoa héo úa, có một tảng đá lớn, khắc dòng chữ đỏ:\n"
              "x = (5**2) + 3\n"
              "y = x + 100\n"
              "Trước mặt bạn là một cánh cửa sắt, cánh cửa được khóa bởi khóa điện tử")
    elif choice == "2":
        code = input("Mời bạn nhập mã: y = ")
        if code == "128":
            print("Cánh cửa mở toang, bạn bước vào trong nhà\n"
                  "Cả gian nhà trống trơn, bụi bặm đầy sàn, dường như người chủ căn nhà đã dọn đi từ rất lâu\n"
                  "Trên sàn nhà có một mẩu giấy nhỏ")
            break
        else:
            print("Sai mật mã")
while True:
    print("Bạn sẽ:\n"
          "1. Nhặt mẩu giấy lên và đọc\n"
          "2. Đi về phía cửa sau")
    choice = input(">>>")
    if choice == "1":
        print("Bạn nhặt mẩu giấy lên và đọc:\n"
              "Chào mừng đến vào thế giới song song, ở đây bạn sẽ bắt đầu cuộc phiêu lưu của mình, "
              "phá bỏ những giới hạn, lập lại trật tự của chính thế giới\n"
              "này và đưa mọi thứ trở lại đúng trạng thái trước kia\n"
              "Cánh cửa sau mở toang, một con sói xám nhảy xổ ra gầm gừ, ánh mắt nhìn bạn thèm thuồng")
        break
    elif choice == "2":
        print("Cánh cửa sau mở toang, một con sói xám nhảy xổ ra gầm gừ, ánh mắt nhìn bạn thèm thuồng")
        break
    else:
        print("Đánh lại đê!")
while True:
    print("Bạn sẽ:\n"
          "1. Bỏ chạy\n"
          "2. Đứng yên chờ đợi\n"
          "3. Lao về phía con sói")
    choice = input(">>>")
    if choice == "1":
        print("Bạn định bỏ chạy nhưng cánh cửa đóng lại")
    elif choice == "2":
        print("Bạn và sói gườm gườm nhìn nhau, không bên nào động thủ\n"
              "Bạn và sói cứ nhìn nhau như vậy tầm 10 phút, sói do bỏ đói "
              "lâu ngày không chịu được đã lao vào tấn công bạn")
        break
    elif choice == "3":
        break
    else:
        print("Đánh lại đê!")
print("----------")
for k, v in player.items():
    print(k, v)
print("----------")
print("Đấu với")
print("----------")
for k, v in wolf.items():
    print(k, v)
print("----------")
combat(player, wolf)