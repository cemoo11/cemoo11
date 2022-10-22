import random
yazıgelen = 0 
turagelen = 0
parayüzeyi = ["tura","yazı"]
kaçkere = int(input("para kaç kere atılacak:"))

while kaçkere > 0:
    paraüstü = random.choice(parayüzeyi)
    if paraüstü == "tura": 
        turagelen +=1
        print("tura geldi")
    else:
        yazıgelen +=1
        print("yazı geldi")
    kaçkere -=1

print("{} :tura geldi\n{} :yazı geldi".format(turagelen,yazıgelen))
