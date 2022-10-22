class Ev():
    def __init__(self,sahibi,kaçoda,kaçıncıkat,fiyat,semt,):
        self.sahibi = sahibi
        self.kaçoda = kaçoda
        self.kaçıncıkat = kaçıncıkat
        self.fiyat = fiyat
        self.semt = semt   
    def evinbilgileri(self):
        print("""{}'nin ev bilgileri :
         oda sayısı: {}\n kaçıncı katta:{}\n fiyatı:{}\n semti:{}""".format(self.sahibi,self.kaçoda,self.kaçıncıkat,self.fiyat,self.semt))      

ev = Ev("cemal satış",4,"5.kat",450000,"eyyubiye")
def __str__(self):
    return """{}'nin ev bilgileri :
     oda sayısı: {}\n kaçıncı katta:{}\n fiyatı:{}\n semti:{}""".format(self.sahibi,self.kaçoda,self.kaçıncıkat,self.fiyat,self.semt)               

print(ev.evinbilgileri())












