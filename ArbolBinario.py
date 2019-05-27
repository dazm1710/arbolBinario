class Nodo:
    def __init__(self, valor,izq=None,der=None):
        self.valor=valor
        self.izq=izq
        self.der=der

def buscar(arbol,valor):
    if(arbol==None):
        return False
    if(arbol.valor==valor):
        return True
    if(arbol.valor<valor):
        return buscar(arbol.der,valor)
    return buscar(arbol.izq,valor)
    
def sumar(arbol):
    if(arbol==None):
        return 0
    return sumar(arbol.izq)+arbol.valor+sumar(arbol.der)

def aLista(arbol):
    if arbol==None:
        return[]
    return aLista(arbol.izq)+[arbol.valor]+aLista(arbol.der)

def aArbol(lista,arbol):
    if len(lista)==0:
        return arbol
    return aArbol(lista[1:],insertar(arbol,lista[0]))

def insertar(arbol,valor):
    if(arbol==None):
        return Nodo(valor)
    if(arbol.valor>valor):
        return Nodo(arbol.valor,insertar(arbol.izq,valor),arbol.der)
    return Nodo(arbol.valor,arbol.izq,insertar(arbol.der,valor))

arbol=Nodo(25,Nodo(10,Nodo(5),Nodo(18)),Nodo(40,None,Nodo(50)))
lista=[5,4,6,3,7,2,8,1,9,0]

print aLista(aArbol(lista,None))
