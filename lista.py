from node import Node

class Lista(Node):

  def __init__(self):
    self.inicio = self.fim = None

  def add(self, v):
    if self.inicio == None:
      self.inicio = Node(v)
      self.fim = self.inicio
    else:
      self.fim.setNext(Node(v))
      self.fim = self.fim.getNext()

  def showList(self):
    aux = self.inicio
    while aux != None:
      print(aux.getX())
      aux = aux.getNext()

  def listSize(self):
    aux  = self.inicio
    tam = 0
    while aux != None:
      tam += 1
      aux = aux.getNext()
    print(tam)

  def listSum(self):
    aux = self.inicio
    sum = 0
    while aux != None:
      sum += aux.getX()
      aux = aux.getNext()
    print(sum)

  def returnList(self):
    aux = self.inicio
    arr = []
    while aux != None:
      arr.append(aux.getX())
      aux = aux.getNext()
    return arr

  

  
    