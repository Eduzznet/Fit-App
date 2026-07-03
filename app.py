from flask import Flask, render_template, request
from treinos import treinos_fixos, meses

app = Flask(__name__)

@app.route('/')
def index():
    """
    Ponto de entrada do aplicativo. 
    Lida com a seleção de planilhas mensais e mescla os treinos disponíveis.
    """
    lista_meses = list(meses.keys())
    mes_atual = request.args.get('mes')
    
    # Se o usuário acessar a raiz sem parâmetros, servimos a planilha mais recente.
    if mes_atual not in lista_meses:
        mes_atual = lista_meses[-1] 

    # Mescla as rotinas específicas do mês ativo com o banco de treinos atemporais (preventivos, etc)
    treinos_do_mes = list(meses[mes_atual].keys())
    treinos_gerais = list(treinos_fixos.keys())
    
    todos_os_treinos = treinos_do_mes + treinos_gerais

    return render_template('index.html', 
                           treinos=todos_os_treinos, 
                           mes_atual=mes_atual, 
                           lista_meses=lista_meses)

@app.route('/treino/<mes>/<nome>')
def abrir_treino_ou_pasta(mes, nome):
    """
    Roteador dinâmico. Decide se o usuário clicou em uma ficha de treino direta
    ou em uma categoria que exige a abertura de um submenu.
    """
    # Ordem de resolução: busca primeiro nas planilhas mensais, depois nos treinos fixos
    if nome in meses.get(mes, {}):
        conteudo = meses[mes][nome]
    elif nome in treinos_fixos:
        conteudo = treinos_fixos[nome]
    else:
        return "Treino não encontrado", 404
    
    # Identifica a estrutura de dados: dict = pasta com mais opções; list = ficha de exercícios
    if isinstance(conteudo, dict):
        nomes_subtreinos = list(conteudo.keys())
        return render_template('submenu.html', mes=mes, categoria=nome, subtreinos=nomes_subtreinos)
    else:
        return render_template('treino.html', mes=mes, nome_treino=nome, blocos=conteudo)

@app.route('/treino/<mes>/<categoria>/<subtreino>')
def abrir_subtreino(mes, categoria, subtreino):
    """
    Carrega a ficha de treino final a partir de um submenu.
    """
    if categoria in treinos_fixos:
        blocos = treinos_fixos[categoria][subtreino]
    else:
        blocos = meses[mes][categoria][subtreino]
        
    nome_completo = f"{categoria} - {subtreino}"
    return render_template('treino.html', mes=mes, nome_treino=nome_completo, blocos=blocos)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')