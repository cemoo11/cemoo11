dosya = open("program.txt","r",encoding="utf-8")

print(dosya.readlines()) #int değer alır

dosya.close()

#"r"--> dosyayı okur
#"w"--> dosya yazılacak
#"a"--> dosya ekleme yapılacak
#"a+"--> dosya ekleme ve okuma 