login = {
    "jeymsBond": "agent007",
    "tony_stark": "ironman101",
    "piterParker": "spider.12.12",
    "sherlok": "sher.l04"
}

ism = input("Username kiriting: ")
parol = input("Parol kiriting: ")

if ism not in login:
    print("Bunday foydalanuvchi mavjud emas")
elif login[ism] == parol:
    print("Hisobga kirdingiz")
else:
    print("Parol noto'g'ri")