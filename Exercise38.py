thang=int(input("Thang:"))

if thang==2:
    ngay="Thang nay co 28 ngay hoac 29 ngay (nam du)"

elif thang in (1,3,5,7,8,10,12):
    ngay="Thang nay co 31 ngay"

elif thang in (4,6,9,11):
    ngay="Thang nay co 30 ngay"

print(ngay)
