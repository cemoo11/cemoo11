while True:
    try:
        boy = float(input("LÜTFEN BOYUNUZU GİRİN :"))
        break
    except ValueError:
        print("LÜTFEN DEĞERİ DOĞRU GİRİNİZ!")
    break
while True:       
    try:
        kütle = float(input("LÜTFEN KİLONUZU GİRİN: "))
        break
    except ValueError:
        print("LÜTFEN DEĞERİ DOĞRU GİRİNİZ!")

print(kütle/boy**2)




















