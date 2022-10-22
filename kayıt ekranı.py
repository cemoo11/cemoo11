print("""***HOŞ GELDİNİZ***

1.KAYIT OL
2.GİRİŞ YAP
3.ŞİFREMİ UNUTTUM
4.ÇIKIŞ

""")
while True:
    seçim = int(input("lütfen yapmak istediğiniz işlemi seçin: "))
    if seçim ==1:

        ad = str(input("adınız: "))
        mail = input("lütfen gmail i girin: ")
        şifre = int(input("şifre belirleyin: "))
        kullanıcılar=str((ad,mail,şifre)) 

        dosya= open("kullanıcılar.txt","w",encoding="utf-8")

        dosya.write(str(kullanıcılar))

        print((kullanıcılar))
    
        dosya.close()



