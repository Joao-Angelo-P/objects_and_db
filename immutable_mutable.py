# Simulando um operador ternario em Python
# E teste de refencias e copias de objteos mutaveis

class Teste(object):
    def __init__(self, a: list = None, b: set = None, c: dict = None, d: str = None, e: int = False, f: float = False, g: complex = False, h: tuple = None):
        """
        Da letra a a c são objetos mutaveis, entao tem como mudar em loco. Por isso é bom fazer copia
        """

        # Copia do Objeto / Novo objeto / Nova atribuição
        #self.a = (a and list(a)) or list() # or (a and a[:]) or list()
        #self.b = (b and set(b)) or set() # (b and b.copy()) or set()
        #self.c = (c and dict(c)) or dict() # (c and c.copy()) or dict()

        """
        Da letra a a c são objetos mutaveis> So que agora sao as mesmas refencias dos objetos no
        escopo global. Mudanças em loco refelte mudanças nas variaveis globais passadas de a a c. Isso ocorre
        pela propriedade do objtos -> list, set e dict
        * Descomente e faça os testes. Seçao abaixo que estiver com "#" e comente a de cima*
        teste.a is obj_teste[0] # isso mostra que é a mesma referencia
        teste.a == obj_teste[0] # isso mostra que o conteudo dos objetos sao os mesmos. Nao quer dizer que sao dois objetos com mesma referencia
        teste.a is obj_teste[0] # -> False: entao é uma copia, mudanças em uma das 2 refencias nao reflete as mesmas mudanças
        teste.a is obj_teste[0] # -> True: entao sao a mesma refencia, mudanças em uma das 2 refencias reflete as mesmas mudanças
        """

        # mesma refencia, escopo da classe e escopo local tem a mesma refencia
        self.a = (a and a) or list() 
        self.b = (b and b) or set() 
        self.c = (c and c) or dict() 

        """
        Da letra d a g são objetos imutaveis, entao nao tem como mudar em loco
        """
        self.d = d or str()
        self.e = e or int(e)
        self.f = f or float(f)
        self.g = g or complex(g)
        self.h = h or tuple()


obj_teste = [[2, 3], {1, 6}, dict(a=0, b=1)]         
teste = Teste(a=obj_teste[0], b=obj_teste[1], c=obj_teste[2])
print("Antes dos Testes:\n" + str(obj_teste) + "\n------------------------")
# Testes
teste.a.append(4); teste.b.add(2); teste.c["c"] = 2
print("Depois dos Testes:")
for i in obj_teste: print(i)
del i
assert teste.a is obj_teste[0]
assert teste.b is obj_teste[1]
assert teste.c is obj_teste[2]
