from main import app
from flask import render_template, request
from calc import calcular

expressao= ""
@app.route("/", methods=['GET', 'POST'])



def homepage():
  global expressao

  
  if request.method== 'POST':
    botao= request.form['botao']
    
    if botao == "C":
      expressao=""
    elif botao =='+-':
      if expressao:
        if expressao.startswith('-'):
          expressao = expressao[1:]
        else:
          expressao='-' + expressao
    elif botao == "=":
      expressao = calcular(expressao)
    else:
      expressao += botao
      
  
  return render_template("homepage.html", resultado =expressao)
