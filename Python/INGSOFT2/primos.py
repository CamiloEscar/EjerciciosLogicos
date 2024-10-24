def imprimirNumerosPrimos(maximo = 100):
	#Calcolatore dei numeri primi: trova tutti i numeri primi fino a N
	primeList = []
	#loop per controllare ogni numero
	for x in range(2, maximo + 1):
		isPrime = True
		index = 0
		root = int(x ** 0.5) + 1
		while index < len(primeList) and primeList[index] <= root:
			if x % primeList[index] == 0:
				isPrime = False
				break
			index += 1
		if isPrime:
			primeList.append(x)
	print(primeList)

def imprimirNCantidadDeNumerosPrimos(cantidad = 10):
	#-------------------------------------------------------------
	#Calcolatrice dei numeri primi: trova i primi N primi

	primeList = []
	x = 2
	
	while len(primeList) < cantidad:
		isPrime = True
		index = 0
		root = int(x ** 0.5) + 1
		while index < len(primeList) and primeList[index] <= root:
			if x % primeList[index] == 0:
				isPrime = False
				break
			index += 1
		if isPrime:
			primeList.append(x)
		x += 1
	print(primeList)

opcion = input('vuoi inserire i dati? (s/n): ')

if opcion == 'y':
	max = int(input("cercare numeri primi fino a quale numero?: "))
	count = int(input("trovare quanti numeri primi?:"))
else:
	max = 100
	count = 10
	
imprimirNCantidadDeNumerosPrimos(max)
imprimirNumerosPrimos(count)