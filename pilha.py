from node import Node

class Pilha(Node):

  def __init__(self):
    self.inicio = None
    self.tamanho = 0

  def push(self, v):
    aux = Node(v)
    aux.setNext(self.inicio)
    self.inicio = aux
    self.tamanho = self.tamanho + 1

  def pop(self):
    aux = self.inicio
    self.inicio = self.inicio.getNext()
    self.tamanho = self.tamanho - 1
    return aux.getX()

  def isEmpty(self):
    return self.tamanho == 0
    