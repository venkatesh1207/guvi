while True:
	try:
		v,w= raw_input().split()
		v=int(v)
		w=int(w)
		break
	except:
		print("Invalidinput")
		break
C=1
for x in range(w):
	C=C*w
print(C)
