def calcular(expressao):
  try:
    expressao = expressao.replace('÷', '/').replace('x', '*')
    
    resultado = eval(expressao)
    
    return str(resultado)
  except Exception as e:
    return "ERRO"