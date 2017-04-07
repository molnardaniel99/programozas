import random
zsak=[]
while len (zsak)<5:
	x=random.randrange(1,91)
	if not (x in zsak):
		zsak.append(x)
print(zsak)

