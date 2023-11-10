nguoi = int(input('Tuổi chó theo năm của người:'))
if nguoi < 0:
	print('Không hợp lệ')
elif nguoi <= 2:
	cho = nguoi * 10.5
else:
	cho = 21 + (nguoi-2)*4
print('Tuổi chó là', cho)
