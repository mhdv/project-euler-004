maxnum = 0
for v in range(1000,100,-1):
	for i in range(1000,100,-1):
		if str(v*i)==str(v*i)[::-1]:
			if i*v > maxnum:
				maxnum = i*v
print(maxnum)