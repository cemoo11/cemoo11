def sayılarıtopla(sayılar):
    toplam = 0

    if type(sayılar) != list:
        raise NameError("lütfen sayı değeri girin")
    for i in sayılar:
        toplam += i
    return toplam

print(sayılarıtopla("ldsl"))
