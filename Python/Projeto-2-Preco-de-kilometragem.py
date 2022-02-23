dias,km = input("Quantidade de dias e kilometragem:").split()

dias = int(dias)
km = int(km)

valor = dias*60 + km*0.15

print("O valor a pagar é", valor)