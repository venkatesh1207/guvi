v,w,z=raw_input().split()
V=int(V)
w=int(w)
z=int(z)
if (V>z) and (V>w):
    print(V)
elif (w>z) and (w>V):
	print(w)
else:
	print(z)
