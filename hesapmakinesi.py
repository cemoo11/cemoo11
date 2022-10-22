print("""*** HESAP MAKİNESİ ***
***İŞLEMLER***
toplama için---> 1
çarpma için---> 2 
bölme için---> 3 
çıkarma için---> 4'ü seçin.

""")
sayı1 = int(input("birinci sayıyı girin: "))
işlem = int(input("girilecek işlemi seçin:"))
sayı2 = int(input("ikinci sayıyı girin: "))

if işlem ==1:
    print(sayı1+sayı2)
if işlem==2:
    print(sayı1*sayı2)
if işlem==3:
    print(sayı1/sayı2)
if işlem==4:
    print(sayı1-sayı2)






