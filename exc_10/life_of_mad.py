from combat import combat_full
from inventory import *

player = {
    "NAME": "MAD",
    "CLASS": "TEACHER",
    "HP": 60,
    "STR": 7,
    "DEF": 10,
    "AGI": 1,
    "LVL": 1,
    "LUCK": 10,
}
items.append(generate_item())
cmd = input("Your command? ")

if cmd == "stats":
    print("NAME:", player["NAME"])
    print("CLASS:", player["CLASS"])
    print("HP:", player["HP"])
    print("STR:", player["STR"])
    print("DEF:", player["DEF"])
    print("LVL:", player["LVL"])
elif cmd == "here":
    print("Bạn đang ở trước cửa TechKids")
    print("Bạn có 2 lựa chọn")
    print("1. Về TechKids")
    print("2. Đi vào cánh rừng đối diện")
    option = input("Lựa chọn của bạn? ")
    if option == "1":
        print("Xin lỗi, đã hết giờ làm việc")
        print("Nhập lại đê!!!")
    elif option == "2":
        print("Bạn đã bước vào rừng")
        print("Bạn thấy một bình chất lỏng ở trên mặt đất")
        print("1. Bỏ qua")
        print("2. Nhặt lên uống")
        option = input("Lựa chọn của bạn? ")
        if option == "1":
            print("Tiếc quá")
        elif option == "2":
            player["HP"] = 100
            print("Bạn đã được hồi phục hoàn toàn HP")
            print("HP:", player["HP"])

        print("Bạn gặp 1 con Orc chưa trưởng thành")
        print("Bạn sẽ:")
        print("1. Chạy trốn")
        print("2. Nấp vào hang đá bên cạnh")
        print("3. ĐÁNH!")
        option = input("Lựa chọn của bạn?")
        if option == "1":
            print("Do bạn chạy quá chậm nên đã bị Orc bắt đi")
        elif option == "2":
            print("Con Orc không nhìn thấy bạn và bỏ đi")
            print("Tuy nhiên, khi bạn quay lại nhìn vào trong hang, bạn thấy một đàn sói")
        elif option == "3":
            orc = {
                "NAME": "SMALL ORC",
                "CLASS": "ORC",
                "STR": 1,
                "DEF": 2,
                "AGI": 1,
                "HP": 60,
                "LUCK": 2,
            }

            print("OPPONENT:", orc["NAME"])
            print("CLASS:", orc["STR"])
            print("STR:", orc["STR"])
            print("DEF:", orc["DEF"])
            print("HP:", orc["HP"])

            combat_full(player, orc)

    else:
        print("Nhập lại đê!!!")
