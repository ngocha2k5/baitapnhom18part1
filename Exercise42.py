f=float(input('tần suất='))
nốt=''

if f>260.63 and f<262.63:
	nốt = 'C4'

elif f>292.66 and f<294.66:
	nốt = 'D4'

elif f>328.63 and f<330.63:
	nốt = 'E4'

elif f>348.23 and f<350.23:
	nốt = 'F4'

elif f>391.00 and f<393.00:
	nốt = 'G4'

elif f>439.00 and f<441.00:
	nốt= 'A4'

elif f>492.88 and f<494.88:
	nốt = 'B4'

if nốt == '':
	print('Không có nốt tương ứng')
else:
	print('Nốt đó là', nốt)