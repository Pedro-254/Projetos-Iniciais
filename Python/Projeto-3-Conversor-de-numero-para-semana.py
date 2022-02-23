import math
import sys

x = input("Informe o dia: ")

x = int(x)

if x < 1 or x > 31:
  sys.exit("Digite um número entre 1 e 31")

while x > 7:
  x -= 7

if x == 1:
  print("Domingo")
elif x == 2:
  print("Segunda")
elif x == 3:
  print("Terça")
elif x == 4:
  print("Quarta")
elif x == 5:
  print("Quinta")
elif x == 6:
  print("Sexta")
elif x == 7:
  print("Sabado")