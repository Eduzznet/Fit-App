from flask import Flask, render_template, request
from treinos import treinos_fixos, meses

app = Flask(__name__)

# ROTA INICIAL (Recebe o mês selecionado)
@app.route('/')
def index():
    # Pega o mês da URL (ex: /?mes=Abril 2026). Se não tiver, usa o primeiro da lista.
    lista_meses = list(meses.keys())
    mes_atual = request.args.get('mes')
    
    if mes_atual not in lista_meses:
        mes_atual = lista_meses[-1] # Padrão: exibe o mês mais novo/ultimo da lista

    # Junta os treinos daquele mês com os treinos fixos
    treinos_do_mes = list(meses[mes_atual].keys())
    treinos_gerais = list(treinos_fixos.keys())
    
    todos_os_treinos = treinos_do_mes + treinos_gerais

    return render_template('index.html', 
                           treinos=todos_os_treinos, 
                           mes_atual=mes_atual, 
                           lista_meses=lista_meses)

# ROTA DO TREINO (Inclui o mês na URL)
@app.route('/treino/<mes>/<nome>')
def abrir_treino_ou_pasta(mes, nome):
    # Primeiro procura se é um treino específico do mês
    if nome in meses.get(mes, {}):
        conteudo = meses[mes][nome]
    # Se não for, procura se é um treino fixo (Preventivo, etc)
    elif nome in treinos_fixos:
        conteudo = treinos_fixos[nome]
    else:
        return "Treino não encontrado", 404
    
    # Checa se é dicionário (Submenu) ou Lista (Treino direto)
    if isinstance(conteudo, dict):
        nomes_subtreinos = list(conteudo.keys())
        return render_template('submenu.html', mes=mes, categoria=nome, subtreinos=nomes_subtreinos)
    else:
        return render_template('treino.html', mes=mes, nome_treino=nome, blocos=conteudo)

# ROTA DA SUBPASTA (Agora inclui o mês na URL)
@app.route('/treino/<mes>/<categoria>/<subtreino>')
def abrir_subtreino(mes, categoria, subtreino):
    # Lógica igual: procura nos fixos primeiro, depois no mês
    if categoria in treinos_fixos:
        blocos = treinos_fixos[categoria][subtreino]
    else:
        blocos = meses[mes][categoria][subtreino]
        
    nome_completo = f"{categoria} - {subtreino}"
    return render_template('treino.html', mes=mes, nome_treino=nome_completo, blocos=blocos)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')