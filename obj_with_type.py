# build a class with type()
Obj = type("Obj", (object, ), dict(indice=0,
                                   add=(lambda self, x, y: x+y), 
                                   times=(lambda self, x, y: x*y), 
                                   exp=(lambda self, x, y: x**y),
                                  __str__=(lambda self:f"<{self.__class__.__name__} n°{self.indice}>"),
                                  __repr__=(lambda self: f"""<{self.__class__.__name__} -> {(
                                    {key:value for key,value in Obj.__dict__.items() if not key.startswith('__')
                                    and not key.endswith('__')})}>"""),
                                  caractere="Objeto exemplo",
                                   __annotations__="Doc de ajuda"
                                  )
          )
obj = Obj()
objn = Obj()
objn.indice = 17
print(f"Nome do objeto: --- {obj.__class__.__name__} ---\nTipo: {type(obj)}\nInstancia:\t{isinstance(obj, object)}")
print("Soma:%s\nMultiplicação:%s\nExponenciação:%s" % (obj.add(22.5, 12.5), obj.times(125, 25), obj.exp(2, 10)))
