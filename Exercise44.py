ngay=int(input('Ngày: '))
thang=int(input('Tháng: '))
Lễ=''
if ngay==1 and thang==1:
    print('New year’s day')

elif ngay==1 and thang==7:
    print('Canada day')

elif ngay==25 and thang==12:
    print('Christmas day')

else:
    print('Không có dữ liệu tương ứng')


