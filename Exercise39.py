dB=float(input('dB ban đầu= '))
	
if dB>0 and dB<40:
    print('nhỏ hơn quiet room')
		
elif dB==40:
    print('bằng quiet room')
	
elif dB>40 and dB<70:
    print('nhỏ hơn alarm clock')

elif dB==70:
    print('bằng alarm clock')
		
elif dB>70 and dB<106:
    print('nhỏ hơn Gas lawnmower')
	
elif dB==106:
    print('bằng Gas lawnmower')
	
elif dB>106 and dB<130:
    print('nhỏ hơn jackhammer')
		
elif dB==130:
    print('bằng jackhammer')
	
elif dB>130:
    print('rất to')
		
else:
    print('Hãy nhập giá trị thích hợp')  
