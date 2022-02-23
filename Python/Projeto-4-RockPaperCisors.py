res = "s"
p = 0
b = 0
i = 0
z = 0

print("Player %d x Bot %d" % (p,b))

while res == "s":
	import random
	import sys
	import os
	
	escolha = input("Escolha: Rock,Paper or Cisors. \n\n")
	
	escolha = escolha.lower()
	
	if escolha == "rock":
	  escolha = "Rock"
	elif escolha =="paper":
	  escolha = "Paper"
	elif escolha == "cisors":
	  escolha = "Cisors"
	
	if escolha == "Rock":
	  escolha = 1
	  i = 1
	elif escolha =="Paper":
	  escolha = 2
	  i = 1
	elif escolha == "Cisors":
	  escolha = 3
	  i = 1
	else:
		escolha = 0
		i = 0
	
	escolha = int(escolha)
	
	if i == 1:
		
		print('X')
		
		random = random.randint(1,3)
		
		if random == 1:
		  print("Rock")
		elif random == 2:
		  print("Paper")
		elif random == 3:
		  print("Cisors")
		
		print("\n")
		
		#Maquina pedra
		if random == 1 and escolha == 1:
		  print("TIE")
		elif random == 1 and escolha == 2:
		  print("WIN")
		  p +=1
		elif random == 1 and escolha == 3:
		  print("LOSE")
		  b +=1
		
		#Maquina papel
		elif random == 2 and escolha == 1:
		  print("LOSE")
		  b +=1
		elif random == 2 and escolha == 2:
		  print("TIE")
		elif random == 2 and escolha == 3:
		  print("WIN")
		  p +=1
		
		#Maquina tesoura
		elif random == 3 and escolha == 1:
		  print("WIN")
		  p +=1
		elif random == 3 and escolha == 2:
		  print("LOSE")
		  b +=1
		elif random == 3 and escolha == 3:
		  print("TIE")
		
		res = input("Quer jogar novamente? (s ou n)")
		
		if res == "s" or res == "n":
			z = 1
			
		while z == 0:
			os.system("clear")	
			print("Player %d x Bot %d \n" % (p,b))
			print("Opção invalida! Escolha entre as opçōes fornecidas. \n")
			res = input("Quer jogar novamente? (s ou n)")
			if res == "s" or res == "n":
				z = 1
			
		if res == "s":
		   os.system("clear")
		   print("Player %d x Bot %d" % (p,b))
		else:
			res = "n"
			os.system("clear")
			print("Placar final: Player %d x Bot %d" % (p,b) )
			print("Obrigado por jogar!")
			
	else:
		os.system("clear")
		print("Opção invalida! Escolha entre as opçōes fornecidas. \n")
		print("Player %d x Bot %d" % (p,b))