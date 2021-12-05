#!/usr/bin/env python3

from collections import defaultdict

def dfs(adj_list, visited, vertex, result, key):
    visited.add(vertex)
    result[key].append(vertex)
    for neighbor in adj_list[vertex]:
        if neighbor not in visited:
            dfs(adj_list, visited, neighbor, result, key)
            

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
  valores_pesos_classes = [list(elem) for elem in valores_pesos]
  
  for i in valores_pesos_classes:
    i.append(-1)
  

  pares_proibidos = []
  for i in range(num_pares_proibidos):
    i, j = input().split()
    pares_proibidos.append((int(i), int(j)))
  
  classes = {}
  
  adj_list = defaultdict(list)
  for x, y in pares_proibidos:
      adj_list[x].append(y)
      adj_list[y].append(x)
  
  result = defaultdict(list)
  visited = set()
  for vertex in adj_list:
      if vertex not in visited:
          dfs(adj_list, visited, vertex, result, vertex)
  
  comuns = list(result.values())
  if len(comuns) > 0:
    for i in range(len(comuns)):
      classes[i] = comuns[i]
      for j in range(len(comuns[i])):
        valores_pesos_classes[ comuns[i][j]-1 ][2] = i
    
  index = len(comuns)
  for i in range(len(valores_pesos)):
    element_in_sublists = [i+1 in list for list in comuns]
    if not any(element_in_sublists):
      classes[index] = [i + 1]
      valores_pesos_classes[i][2] = index
      index = index + 1

  # print(valores_pesos_classes) 
  return num_itens, num_pares_proibidos, capacidade, valores_pesos, classes

def bound(valores_pesos, tam, capacidade, node):
  if node[3] >= capacidade:
    return 0
  
  lucro_bound = int(node[1])
  j = node[0] + 1
  peso = int(node[3])
  
  while j < tam and peso + valores_pesos[j][1] <= capacidade:
    peso = peso + valores_pesos[j][1]
    lucro_bound = lucro_bound + valores_pesos[j][0]
    j = j + 1
    
  if j < tam:
    lucro_bound = lucro_bound + (capacidade - peso) * valores_pesos[j][0]/float(valores_pesos[j][1])
    
  return lucro_bound
  
def knapsack(num_pares_proibidos, capacidade, valores_pesos, pares_proibidos):
  sorted_valores_pesos = sorted(valores_pesos, key=lambda t: float(t[0])/float(t[1]), reverse=True)
  tam = len(sorted_valores_pesos)
  
  max = 0
  n1 = [-1, 0, 0, 0, []]
  fila = []
  fila.append(n1)
  # n2 = [0, 0, 0, 0]
  escolhidos = []
  
  # val : tupla(level 0, profit 1, bound 2, weight 3)
  while (len(fila) > 0):
    n1 = fila[0]
    fila.pop(0)
    n2 = [0,0,0,0, []]
    
    if (n1[0] == -1):
      n2[0] = 0
      
    if (n1[0] == tam-1):
      continue
    
    n2[0] = n1[0] + 1
    n2[1] = n1[1] + sorted_valores_pesos[n2[0]][0]
    n2[3] = n1[3] + sorted_valores_pesos[n2[0]][1]
    n2[4] = list(n1[4])
    n2[4].append(sorted_valores_pesos.index(sorted_valores_pesos[n2[0]]))
    
    if n2[3] <= capacidade and n2[1] > max:
      max = n2[1]
      escolhidos = n2[4]
      
    n2[2] = bound(sorted_valores_pesos, tam, capacidade, n2)
    
    if n2[2] > max:
      fila.append(n2)
      
    n2[0] = n1[0] + 1
    n2[1] = n1[1]
    n2[3] = n1[3]
    n2[4] = list(n1[4])
    
    n2[2] = bound(sorted_valores_pesos, tam, capacidade, n2)
    if n2[2] > max:
      fila.append(n2)
  
  print("escolhidos:", escolhidos)
  taken = [0] * len(sorted_valores_pesos)
  for i in range(len(escolhidos)):
      taken[escolhidos[i]] = 1
  print(sorted_valores_pesos)
  return max

def main():
  num_itens, num_pares_proibidos, capacidade, valores_pesos, classes = read_input()
  
  # print(num_itens, num_pares_proibidos, capacidade, classes)
  # print("max: ", knapsack(num_pares_proibidos, capacidade, valores_pesos, pares_proibidos))
  return 0

if __name__ == "__main__":
  main()