from lista import Lista

from pilha import Pilha

from fila import Fila

class Main(object):

  l = Lista()
        
  l.add(10)
  l.add(20)
  l.add(30)
  l.add(40)
  l.add(50)
  l.add(60)
  
  l.showList()
  print('\n')
  l.listSize()
  print('\n')
  l.listSum()
  print('\n')

  l1 = Lista()
  l2 = Lista()

  list1 = input('Qual sua lista 1?')
  list2 = input('Qual sua lista 2?\n')

  for i in list1:
    l1.add(i)
  for i in list2:
    l2.add(i)

  print(l1.returnList() == l2.returnList())
  print('\n')

  eq = ''
  for i in l.returnList()[::-1]:
    eq += str(i) + ' '
  print(eq)
  print('\n')

  p = Pilha()

  p.push(10)
  p.push(20)
  p.push(30)
  p.push(40)
  p.push(50)
  p.push(60)

  while p.isEmpty() == False:
    print(p.pop())

  print('\n')

  f = Fila()

  f.push(10)
  f.push(20)
  f.push(30)
  f.push(40)
  f.push(50)
  f.push(60)

  while f.isEmpty() == False:
    print(f.pop())

  
  