import sqlite3
bağlantı = sqlite3.connect("veritabanı.db")
imleç = bağlantı.cursor()
imleç.execute("CREATE TABLE IF NOT EXIST data("isim" TEXT,"yas" INT,"cinsiyet" TEXT)")
bağlantı.close()





