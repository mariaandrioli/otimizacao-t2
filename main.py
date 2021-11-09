#!/usr/bin/env python3

def read_input():
	num_itens, num_pares_proibidos, capacidade = input().split()
	num_itens = int(num_itens)
	num_pares_proibidos = int(num_pares_proibidos)
	capacidade = int(capacidade)

	pesos = input().split()
	pesos = [ int(x) for x in pesos ]
	
	valores = input().split()
	valores = [ int(x) for x in valores ]

	pares_proibidos = []
	for i in range(num_pares_proibidos):
		i, j = input().split()
		pares_proibidos.append((int(i), int(j)))

	return num_itens, num_pares_proibidos, capacidade, pesos, valores, pares_proibidos

def main():
	print(read_input())
	return 0

if __name__ == "__main__":
	main()