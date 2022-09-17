def calcular(val1, val2, tipo):
  if tipo == 'soma':
    print(soma(val1, val2))

  if tipo == 'soma':
    print(menos(val1, val2))

def soma(val1, val2):
  return val1 + val2

def menos(val1, val2):
  return val1 - val2


calcular(10, 5, 'soma')