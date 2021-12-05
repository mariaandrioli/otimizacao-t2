#!/usr/bin/env python3

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
    i.append([])
  
  pares_proibidos = []
  for k in range(num_pares_proibidos):
    i, j = input().split()
    pares_proibidos.append([int(i), int(j)])
  
  for i in range(num_itens):
    for x in pares_proibidos:
      if i+1 in x:
        valores_pesos_classes[i][2].append(x)
            
  for i in range(num_itens):
    valores_pesos_classes[i][2] = list(set([item for sublist in valores_pesos_classes[i][2] for item in sublist]))

  return capacidade, valores_pesos_classes

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
  tam = len(sorted_valores_pesos)
  
  max = 0
  u = [-1, 0, 0, 0, [], -1]
  fila = [u]
  escolhidos = []
  classes_escolhidas = []
  
  # val : tupla(level 0, profit 1, bound 2, weight 3)
  while (len(fila) > 0):
    u = fila[0]
    fila.pop(0)
    v = [0,0,0,0, [], -1]
    
    if (u[0] == -1):
      v[0] = 0
      
    if (u[0] == tam-1):
      continue
    
    v[0] = u[0] + 1
    v[1] = u[1] + sorted_valores_pesos[v[0]][0]
    v[3] = u[3] + sorted_valores_pesos[v[0]][1]
    v[5] = sorted_valores_pesos[v[0]][2]
    v[4] = list(u[4])
    v[4].append(valores_pesos.index(sorted_valores_pesos[v[0]]))
    
    if v[3] <= capacidade and v[1] > max and v[5] not in classes_escolhidas and valores_pesos.index(sorted_valores_pesos[v[0]]) not in escolhidos:
      max = v[1]
      escolhidos = v[4]
      classes_escolhidas.append(sorted_valores_pesos[v[0]][2])
      
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
      
  escolhidos = sorted([ x+1 for x in escolhidos])

  return max, escolhidos

def main():
  capacidade, valores_pesos_classes = read_input()
  max, escolhidos = knapsack(capacidade, valores_pesos_classes)
  print(max)
  print(*escolhidos)
  return 0

if __name__ == "__main__":
  main()