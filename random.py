from math import *
from random import random

serie_i = open("serie_inicial.txt","w")
serie_t = open("serie_tiempo.txt","w")

s_inicial = [0]*10000000
serienp = [0]*1000000

N = 100000
NT = 10000000
P = N/NT

cuentaf = 0
for j in range (1.NT):
	r = random()
	if r = P:
		s_inicial[j] = 1
	else:
		s_inicial[j] = 0
	cuenta += s_inicial[j]
	serie_i.write(str(j)+"\t"+str(s_inicial[j])+"\n")
	print(f"Fotones contabilizados:{cuentaf}\n")
	
NP = 100
suma = 0
k = 0
for j in range(1,NT):
	m = j%NP
	suma += s_inicial[j]
	if m == 0:
		serie_t.write(str(j)+"\t"+str(suma)+"\n")
		serienp[k] = suma
		k = k+1
		suma = 0

prom = 0
for i in range(1,k):
	prom += serienp[i]/k
print(f"promedio = {prom}")

v=0
c0=0
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
c8=0

for i in range (1,k):
	if serienp[i] == 0:
		c0 += 1
	elif serienp[i] == 1:
		c1 += 1
	elif serienp[i] == 2:
		c2 += 1
	elif serienp[i] == 3:
		c3 += 1
	elif serienp[i] == 4:
		c4 += 1
	elif serienp[i] == 5:
		c5 += 1
	elif serienp[i] == 6:
		c6 += 1
	elif serienp[i] == 7:
		c7 += 1
	elif serienp[i] == 8:
		c8 += 1
	v += ((serienp[i]-prom)**2)/k
	
sd = sqrt(v)

print(f"Standard deviation = {sd}")
print(f"Fano factor = {sd/sqrt(prom)}\n")

print(f"cero = {c0}\t ratio = {c0/k}\n")
print(f"uno = {c1}\t ratio = {c1/k}\n")
print(f"dos = {c2}\t ratio = {c2/k}\n")
print(f"tres = {c3}\t ratio = {c3/k}\n")
print(f"cuatro = {c4}\t ratio = {c4/k}\n")
print(f"cinco = {c5}\t ratio = {c5/k}\n")
print(f"seis = {c6}\t ratio = {c6/k}\n")
print(f"siete = {c7}\t ratio = {c7/k}\n")
print(f"ocho = {c8}\t ratio = {c8/k}\n")

factorial = 1
for m in range(9):
	if m == 0:
		poisson = exp(-prom)
	else:
		factorial *= m
		poisson = (exp(-prom)*(prom**m))/factorial
	print(f"Poisson({m}) = {poisson}")
	

		
	
