d,h,m,s = input("Digite  a quantidade de Dias, horas, minutos e segundos:").split()

d = int(d)
h = int(h)
m = int(m)
s = int(s)

Ds = d * 24 * 60**2
Hs = h * 60**2
Ms = m * 60

T = Ds + Hs + Ms + s

print("O tempo total em segundos é", T)