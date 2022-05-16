class Node(object):

  def __init__(self, v):
    self.x = v
    self.next = None

  def setX(self, v):
    self.x = v

  def getX(self):
    return self.x
    
  def setNext(self, n):
    self.next = n
  
  def getNext(self):
    return self.next

  