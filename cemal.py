import sqlite3
bağlantı = sqlite3.connect("mertmekatronik.db")
imlec= bağlantı.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS ekip(isim TEXT,yas INT,cins TEXT)")
imlec.execute("INSERT INTO ekip VALUES('zühre',23,'kadın')")
imlec.execute("INSERT INTO ekip VALUES('aslı',45,'kadın')")
imlec.execute("INSERT INTO ekip VALUES('murat',35,'erkek')")
imlec.execute("INSERT INTO ekip VALUES('kazım',45,'erkek')")
imlec.execute("INSERT INTO ekip VALUES('merve',29,'kadın')")
imlec.execute("INSERT INTO ekip VALUES('murat',63,'kadın')")
bağlantı.commit()
bağlantı.close()



