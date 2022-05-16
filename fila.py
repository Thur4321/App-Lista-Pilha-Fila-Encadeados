from node import Node

class Fila(Node):

  def __init__(self):
    self.inicio = self.fim =None
    self.tamanho = 0

  def push(self, v):
    aux = Node(v)
    if (self.fim is None):
      self.fim = aux
    else:
      self.fim.setNext(aux)
      self.fim = aux
    if self.inicio is None:
      self.inicio = aux
    self.tamanho = self.tamanho + 1

  def pop(self):
    aux = self.inicio.getX()
    self.inicio = self.inicio.getNext()
    if self.inicio is None:
      self.fim = None
    self.tamanho = self.tamanho - 1
    return aux

  def isEmpty(self):
    return self.tamanho == 0
    