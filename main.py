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
  pesos = [ float(x) for x in pesos ]
  
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
  return num_itens, num_pares_proibidos, capacidade, valores_pesos_classes

def bound(valores_pesos, tam, capacidade, node):
  # val : tupla(level 0, profit 1, bound 2, weight 3)
  if node[3] >= capacidade:
    return 0
  
  profit_bound = int(node[1])
  j = node[0] + 1
  peso_total = int(node[3])
  
  while j < tam and peso_total + valores_pesos[j][1] <= capacidade:
    peso_total = peso_total + valores_pesos[j][1]
    profit_bound = profit_bound + valores_pesos[j][0]
    j = j + 1
    
  if j < tam:
    profit_bound += (capacidade - peso_total) * valores_pesos[j][0]/float(valores_pesos[j][1])
    
  return profit_bound
  
def knapsack(capacidade, valores_pesos):
  sorted_valores_pesos = sorted(valores_pesos, key=lambda t: t[0]/float(t[1]), reverse=True)
  print(sorted_valores_pesos)
  tam = len(sorted_valores_pesos)
  
  max = 0
  u = [-1, 0, 0, 0, []]
  fila = [u]
  escolhidos = []
  
  # val : tupla(level 0, profit 1, bound 2, weight 3)
  while (len(fila) > 0):
    u = fila[0]
    fila.pop(0)
    v = [0,0,0,0, []]
    
    if (u[0] == -1):
      v[0] = 0
      
    if (u[0] == tam-1):
      continue
    
    v[0] = u[0] + 1
    v[1] = u[1] + sorted_valores_pesos[v[0]][0]
    v[3] = u[3] + sorted_valores_pesos[v[0]][1]
    v[4] = list(u[4])
    v[4].append(valores_pesos.index(sorted_valores_pesos[v[0]]))
    
    if v[3] <= capacidade and v[1] > max:
      max = v[1]
      escolhidos = v[4]
      
    v[2] = bound(sorted_valores_pesos, tam, capacidade, v)
    if v[2] > max:
      fila.append(v)
      
    v = [0,0,0,0, []]  
    v[0] = u[0] + 1
    v[1] = u[1]
    v[3] = u[3]
    v[4] = list(u[4])
    
    v[2] = bound(sorted_valores_pesos, tam, capacidade, v)
    if v[2] > max:
      fila.append(v)
  
  # taken = [0] * len(sorted_valores_pesos)
  # for i in range(len(escolhidos)):
  #     taken[escolhidos[i]] = 1
      
  # print(taken)
  print("escolhidos:", escolhidos)
  return max

def main():
  num_itens, num_pares_proibidos, capacidade, valores_pesos_classes = read_input()
  
  print(num_itens, num_pares_proibidos, capacidade)
  print("max: ", knapsack(capacidade, valores_pesos_classes))
  return 0

if __name__ == "__main__":
  main()