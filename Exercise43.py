donvitiente=str(input("Menh gia:"))

if donvitiente=="$1":
    individual="George Washington"

elif donvitiente=='$2':
    individual="Thomas Jefferson" 

elif donvitiente=='$5':
    individual="Abraham Lincoln"

elif donvitiente=='$10':
    individual="Alexander Hamilton"

elif donvitiente=='$20':
    individual="Andrew Jackson"

elif donvitiente=='$50':
    individual="Ulysses S. Grant"

elif donvitiente=='$100':
    individual="Benjamin Franklin"

else:
    individual="Khong ton tai"

print(individual)