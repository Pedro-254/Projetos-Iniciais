game = 1
X = " X "
O = " O "
spc = "   "
sep = "############"
	
linha1 = ["   ","   ","   "]
linha2 = ["   ","   ","   "]
linha3 = ["   ","   ","   "] 
	
cord = [0,0,0,0,0,0,0,0,0]

ia = 0
i = 0
j = 0
k = 0
p = 1
travaativador = 0

while game == 1:
	import sys
	import os
	
	#cerebro da ia
	if ia == 1:
		while True:
			import random
			random = random.randint(0,8)
			if(cord[random] == 0):
				break

	if travaativador == 0:		
		ativador = input("Deseja jogar contra a IA? (s ou n)")
		if ativador == "s":
			ia = 1
			travaativador = 1
		else:
			travaativador = 1
			

	c = 0
	while c == 0:
		
		# Printando jogo
		os.system("clear")
		
		print("%s#%s#%s" % (linha1[0], linha1[1], linha1[2]))
		print(sep)
		print("%s#%s#%s" % (linha2[0], linha2[1], linha2[2]))
		print(sep)
		print("%s#%s#%s" % (linha3[0], linha3[1], linha3[2]))

		if ia == 1 and p == 2:
			c = 1
			cord[random] = 2
			ia = 1
		else:
			#Pegando cordenadas
			print("Ex: x y")
			x,y = input("De as cordenadas: ").split()
			x = int(x) - 1
			y = int(y) - 1
		

		#Registrando a escolha
		k = 0
		i = 0
		j = 0
		
		if ia == 1 and p == 2:
			ia = 1
		else:
			while k < 9:
				while i < 3:
					while j < 3:
						if x == i and y == j:
							if cord[k] == 0:
								cord[k] = p
								c = 1
						j += 1
						k += 1
					j = 0
					i += 1
				i = 0
	
	#Guardar escolha em linha
	i = 0
	j = 0
	k = 0
	while i < 9:
		while j < 3:
			if k == 0:
				if cord[i] == 1:
					linha1[j] = X
				elif cord[i] == 2:
					linha1[j] = O
				elif cord[i] == 0:
					linha1[j] = spc
			elif k == 1:
				if cord[i] == 1:
					linha2[j] = X
				elif cord[i] == 2:
					linha2[j] = O
				elif cord[i] == 0:
					linha2[j] = spc
			elif k == 2:
				if cord[i] == 1:
					linha3[j] = X
				elif cord[i] == 2:
					linha3[j] = O
				elif cord[i] == 0:
					linha3[j] = spc
			i += 1
			j += 1
			
		j = 0
		k += 1
		
	if p == 1:
		p = 2
	elif p == 2:
		p = 1
	
	z = 0
	i  = 0
	j = 1
	k = 2

	while z < 3:
		
		if cord[i] == cord[j] and cord[i] == cord[k] and cord[j] == cord[k]:
			if cord[i]+cord[j]+cord[k] > 0:
				game = 0
				z = 3
		i += 3
		j += 3
		k += 3
		z +=1

	z = 0
	i  = 0
	j = 3
	k = 6
	while z < 3:
		
		if cord[i] == cord[j] and cord[i] == cord[k] and cord[j] == cord[k]:
			if cord[i]+cord[j]+cord[k] > 0:
				game = 0
				z = 3
		i += 1
		j += 1
		k += 1
		z += 1
		
	z = 0
	i  = 0
	j = 4
	k = 8
	while z < 2:
		
		if cord[i] == cord[j] and cord[i] == cord[k] and cord[j] == cord[k]:
			if cord[i]+cord[j]+cord[k] > 0:
				game = 0
				z = 3
		i += 2
		j += 0
		k -= 2
		z += 1
	
	i = 0
	empate = 0
	while i < 9:
		if cord[i] != 0:
			empate += 1
		i += 1
	if empate >= 9:
		os.system("clear")
		print("TIE")
		sys.exit()

if p == 1:
	p = 2
elif p == 2:
	p = 1
elif ia == 1 and p == 2:
	ia = 0
	p = 1


#Declarar vencedor + placar
os.system("clear")
		
print("%s#%s#%s" % (linha1[0], linha1[1], linha1[2]))
print(sep)
print("%s#%s#%s" % (linha2[0], linha2[1], linha2[2]))
print(sep)
print("%s#%s#%s" % (linha3[0], linha3[1], linha3[2]))
			
print( "\nPlayer %d WIN" % p)