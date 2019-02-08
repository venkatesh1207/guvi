while True:
	try:
		v3=int(input())
		break
	except:
		print('invalid')
		break
if v3%400==0 or v3%4==0 and v3%100!=0:
	print('yes')
else:
	print('no')
