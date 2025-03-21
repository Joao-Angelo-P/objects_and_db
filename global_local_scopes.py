# Escopos locais e globais

def func():
  print(x) # gera um erro porque declaração de x está depois da funcao

def func2():
  try:
    from __main__ import y
    y = globals().get('y', False) 
    
  except ImportError:
    print('Não há a variavel \'y\' no escopo global')
  
  else:
    print(y) # importar do modulo a referencia

def func3(*args:object):
  # criar variavel global no escopo da função. 2 formas com palavra especial 
  # "global var" ou usando globals(). Vou usar segundo caso
  globals()['z'] = f"Sou do escopo da funcao -> {__name__}"
  print(z)
  for i in args: print(f"Funcao -> {i.__name__}")
  del i
  globals().pop('z')
  

# Teste de escopos locais e globais.
try:
  func() # aqui vai pra exceção
  x = "Não vai pra exceção"
  # func() # decomente esta linha e a refencia de x vai estar disponivel para função
except NameError as erro:
  x = "Entrou na exceção \"%s\"" % erro.__class__.__name__
  func()

y = "Existe"
func2()
func3(*[globals()[j] for j in globals() if type(globals()[j]).__name__=='function']) # func, func2, func3
#print(z)
#globals().pop('z') # para excluir
try:
  print(z)
except NameError:
  globals().get('z', None) or print('Realmente a variavel não existe no escopo do modulo')
