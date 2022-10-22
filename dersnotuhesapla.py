vizenotu = int(input("vize notunuzu girin:  "))
finalnotu = int(input("final notunuzu girin:  "))
toplam_puan = vizenotu*(2/5) + finalnotu*(3/5)
if toplam_puan >70:
    print("ders notunuz BA'dır.")
elif toplam_puan >60:
    print("ders notunuz BB'dir.")
elif toplam_puan >50:
    print("ders notunuz CB'dir.")
elif toplam_puan >40:
    print("ders notunuz CC'dir.")
else:
    print("ders notunuz FF'dir. Kaldınız!")