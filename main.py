from lista import Lista

lista = Lista()

lista.adicionar(1)
lista.adicionar(2)
lista.adicionar(3, inicio=True)
lista.adicionar(4, inicio=True)
lista.adicionar(5)
lista.adicionar(6, inicio = True)


lista.remove(3)
lista.remove(6)


lista.show()
