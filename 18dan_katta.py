oquvchilar = {
    "Samandar": 18,
    "Abduqodir": 19,
    "Begzod": 16,
    "Usmon": 20,
    "Nurhayotxon": 14,
    "Kamron": 17,
    "Fazliddin": 20
}
katta = [ism for ism, yosh in oquvchilar.items()
if yosh >= 18]

print("18 va undan yuqori oquvchilar: ", (katta))