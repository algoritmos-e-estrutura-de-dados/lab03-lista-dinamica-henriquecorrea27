from node import Node

class Lista:
  inicio = None

  def __init__(self):
    self.inicio = None


  
  def adicionar(self, valor, inicio = False):
    if (inicio):
      self.adicionar_no_inicio(valor)
    else:
      self.adicionar_no_fim(valor)


    
  def adicionar_no_inicio(self, valor):
    ini = Node(valor, None)
    ini.proximo = self.inicio
    self.inicio = ini
    
  #adicionar no final da lista
  def adicionar_no_fim(self, valor):
    if self.inicio == None:
      self.inicio = Node(valor, None)
    else:
      aux = self.inicio
      while (aux.proximo != None):
        aux = aux.proximo

      aux.proximo = Node(valor, None)
      


  def remove(self, valor):
    aux = self.inicio
    if aux.valor == valor:
      self.inicio = aux.proximo
    else:
      ind = None
      while (aux.valor  != valor):
        ind = aux
        aux = aux.proximo
      if aux.valor == valor:
        ind.proximo = aux.proximo
        

  def show(self):
    aux = self.inicio
    print("[" , end='')
    while (aux.proximo != None):
      print(f"{aux.valor}" , end=', ')
      aux = aux.proximo
    print(aux.valor , end='')
    print("]")


    