#!/usr/bin/env python3

from queue import Empty, Queue


class Tree:
  # val : tupla(level, profit, bound, weight)
  # level  --> Level of node in decision tree (or index
  #             in arr[]
  # profit --> Profit of nodes on path from root to this
  #            node (including this node)
  # bound ---> Upper bound of maximum profit in subtree
  #            of this node/
  
  def __init__(self, val = None):
    if val != None:
      self.val = val
    else:
        self.val = None
    self.left = None
    self.right = None

  def insert(self, val):
    if self.val:
        if val < self.val:
            if self.left is None:
              self.left = Tree(val)
            else:
              self.left.insert(val)
        elif val > self.val:
            if self.right is None:
              self.right = Tree(val)
            else:
              self.right.insert(val)
    else:
        self.val = val

  def printValues(self):
    if self.left:
        self.left.printValues()
    print(self.val)
    if self.right:
        self.right.printValues()
        
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

def bound():
  return 0
  
def knapsack(num_pares_proibidos, capacidade, valores_pesos, pares_proibidos):
  sorted_valores_pesos = sorted(valores_pesos, key=lambda t: float(t[0])/t[1])
  tam = len(valores_pesos)
  # val : tupla(level, profit, bound, weight)
  max = 0
  fila = []
  fila.append((-1, 0, 0 ,0))
  n1 = n2 = (0, 0, 0, 0)
  # queue = Tree((-1, 0, 0 ,0))
  
  while (len(fila) > 0):
    n1 = fila[0]
    fila.pop(0)
    
    if (n1[0] == -1):
      n2[0] = 0
      
    if (n1[0] == tam-1):
      continue
    
    n1[1] = n2[1] + valores_pesos[n2[0]][0]
    n1[3] = n2[3] + valores_pesos[n2[0]][1]
    
    if n2[3] <= capacidade and n2[1] > max:
      max = n2[1]
      
    n2[2] = bound(valores_pesos, tam, capacidade, n2)
    
    if n2[2] > max:
      fila.append(n2)
      
    n2[3] = n1[3]
    n2[1] = n1[1]
    
    n2[2] = bound(valores_pesos, tam, capacidade, n2)
    if n2[2] > max:
      fila.append(n2)
    
  print(valores_pesos)
  print(sorted_valores_pesos)
  return 0

def main():
  num_itens, num_pares_proibidos, capacidade, valores_pesos, pares_proibidos = read_input()
  
  print(num_itens, num_pares_proibidos, capacidade, pares_proibidos)
  knapsack(num_pares_proibidos, capacidade, valores_pesos, pares_proibidos)
  return 0

if __name__ == "__main__":
  main()