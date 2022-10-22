a = float(input("1st value: "))
islem = input("which do you make islem: ")
b = float(input("2nd value: "))

if islem == "+" :
    print(a+b)
if islem == "/":
    print(a/b)
if islem == "*":
    print(a*b)
if islem == "-":
    print(a-b)

else:
    print("valuerror")