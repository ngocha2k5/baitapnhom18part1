a=float(input("Canh a="))
b=float(input("Canh b="))
c=float(input("Canh c="))

if a==b==c:
    tamgiac="Tam giac deu"

elif a==b or b==c or c==a:
    tamgiac="Tam giac can"

else:
    tamgiac="Tam giac thuong"

print(tamgiac)