from flask import Flask
import pandas as pd
import requests

app = Flask(__name__)

@app.route('/<uf>/<cidade>/<logradouro>')
def index(uf, cidade, logradouro):
   
   try:
        uf = uf.upper()
        
        link = f"https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        for item in dic_requisicao:
            item["cep"] = item["cep"].replace("-", "")
        tabela = pd.DataFrame(dic_requisicao)
        tabela = tabela[["cep", "logradouro", "complemento", "bairro", "localidade", "uf"]]
        return tabela.to_html()
   except Exception as erro:
        return f"Erro: {erro}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)