matrizA=[]
matrizR=[]
filasA =3
columnasA=3

print (".......Datos de la matriz 3x3.......")
for i in range(filasA):
	matrizA.append([0]*columnasA)
	
for f in range(filasA):
		for c in range (columnasA):
			matrizA[f][c]=int(input("Elemento matriz A %d ,%d:" % (f,c)))

print ("......Matriz Original.....\n")
print (matrizA,"\n")

print ("......Matriz Transpuesta.......\n")
for i in range(filasA):
	matrizR.append([0]*columnasA)
	
for f in range(filasA):
        for c in range(columnasA):
                matrizR[c][f]=matrizA[f][c];

print (matrizR)
