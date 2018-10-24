a=[[5,6,7],[7,2,3]]
matriz=[[0,0][0,0][0,0]]

for x in range(0,2):
	for y in range(0,3):
		matriz[y][x]=a[x][y]
		
for x in range(0,5):
	for y in range(0,2):
		print(str(matriz[x][y]))
		
	print("\n");