C4=261.63
D4=293.66
E4=329.63
F4=349.23
G4=392.00
A4=440.00
B4=493.88
Not=input("Nhap not nhac: ")
if Not[0]=='C':
    print("Tan so cua ",Not," la: ",C4/(2**(4-int(Not[1]))),sep="")
if Not[0]=='D':
    print("Tan so cua ",Not," la: ",D4/(2**(4-int(Not[1]))),sep="")
if Not[0]=='E':
    print("Tan so cua ",Not," la: ",E4/(2**(4-int(Not[1]))),sep="")
if Not[0]=='F':
    print("Tan so cua ",Not," la: ",F4/(2**(4-int(Not[1]))),sep="")
if Not[0]=='G':
    print("Tan so cua ",Not," la: ",G4/(2**(4-int(Not[1]))),sep="")
if Not[0]=='A':
    print("Tan so cua ",Not," la: ",A4/(2**(4-int(Not[1]))),sep="")
if Not[0]=='B':
    print("Tan so cua ",Not," la :",B4/(2**(4-int(Not[1]))),sep="")