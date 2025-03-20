# build a class with type()
Obj = type("Obj", (object, ), dict(add=(lambda self, x, y: x+y), 
                                   times=(lambda self, x, y: x*y), 
                                   exp=(lambda self, x, y: x**y))
          )
obj = Obj()
print(f"Nome do objeto: --- {obj.__class__.__name__} ---\nTipo: {type(obj)}\nInstancia:\t{isinstance(obj, object)}")
print("Soma:%s\nMultiplicação:%s\nExponenciação:%s" % (obj.add(22.5, 12.5), obj.times(125, 25), obj.exp(2, 10)))
