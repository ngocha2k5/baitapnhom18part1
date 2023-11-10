n=int(input("So canh:"))
if 3<=n<=10:
    if n==3:
        shape="Tam giac"
    elif n==4:
        shape="Tu giac"
    elif n==5:
        shape="Ngu giac"
    elif n==6:
        shape="Luc giac"
    elif n==7:
        shape="That giac"
    elif n==8:
        shape="Bat giac"
    elif n==9:
        shape="Cuu giac"
    else:
        shape="Thap giac"
    
    print(shape)

else:   
    print("Error")