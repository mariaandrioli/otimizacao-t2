#!/usr/bin/env python3

from queue import Empty, Queue
        
def read_input():
  num_itens, num_pares_proibidos, capacidade = input().split(" ", 3)
  num_itens = int(num_itens)
  num_pares_proibidos = int(num_pares_proibidos)
  capacidade = int(capacidade)

  pesos = input().split()
  pesos = [ int(x) for x in pesos ]
  
  valores = input().split()
  valores = [ int(x) for x in valores ]
  
  valores_pesos = list(zip(valores, pesos))

  pares_proibidos = []
  for i in range(num_pares_proibidos):
    i, j = input().split()
    pares_proibidos.append((int(i), int(j)))

  return num_itens, num_pares_proibidos, capacidade, valores_pesos, pares_proibidos

def bound(valores_pesos, tam, capacidade, node):
  if node[3] >= capacidade:
    return 0
  
  lucro_bound = node[1]
  j = node[0] + 1
  peso = node[3]
  
  while j < tam and peso + valores_pesos[j][1] <= capacidade:
    peso = peso + valores_pesos[j][1]
    lucro_bound = lucro_bound + valores_pesos[j][0]
    j = j + 1
    
  if j < tam:
    lucro_bound = lucro_bound + (capacidade - peso) * valores_pesos[j][0]/valores_pesos[j][1]
    
  return lucro_bound
  
def knapsack(num_pares_proibidos, capacidade, valores_pesos, pares_proibidos):
  sorted_valores_pesos = sorted(valores_pesos, key=lambda t: float(t[0])/t[1])
  tam = len(sorted_valores_pesos)
  # val : tupla(level, profit, bound, weight)
  max = 0
  fila = []
  fila.append([-1, 0, 0 ,0])
  n1 = n2 = [0, 0, 0, 0]
  
  while (len(fila) > 0):
    n1 = fila[0]
    fila.pop(0)
    
    if (n1[0] == -1):
      n2[0] = 0
      
    if (n1[0] == tam-1):
      continue
    
    n1[1] = n2[1] + sorted_valores_pesos[n2[0]][0]
    n1[3] = n2[3] + sorted_valores_pesos[n2[0]][1]
    
    if n2[3] <= capacidade and n2[1] > max:
      max = n2[1]
      
    n2[2] = bound(sorted_valores_pesos, tam, capacidade, n2)
    
    if n2[2] > max:
      fila.append(n2)
      
    n2[3] = n1[3]
    n2[1] = n1[1]
    
    n2[2] = bound(sorted_valores_pesos, tam, capacidade, n2)
    if n2[2] > max:
      fila.append(n2)
    
  # print(valores_pesos)
  print(sorted_valores_pesos)
  return max

def main():
  num_itens, num_pares_proibidos, capacidade, valores_pesos, pares_proibidos = read_input()
  
  print(num_itens, num_pares_proibidos, capacidade, pares_proibidos)
  print("max: ", knapsack(num_pares_proibidos, capacidade, valores_pesos, pares_proibidos))
  return 0

if __name__ == "__main__":
  main()