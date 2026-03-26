from flask import Flask, render_template
from treinos import workouts

app = Flask(__name__)

@app.route('/')
def index():
    nomes_dos_treinos = list(workouts.keys())
    return render_template('index.html', treinos=nomes_dos_treinos)

# Rota quando o usuário clica no menu principal
@app.route('/treino/<nome>')
def abrir_treino_ou_pasta(nome):
    if nome not in workouts:
        return "Não encontrado", 404
    
    conteudo = workouts[nome]
    
    # Checa se eh dicionário, o que leva para o submenu
    if isinstance(conteudo, dict):
        nomes_subtreinos = list(conteudo.keys())
        return render_template('submenu.html', categoria=nome, subtreinos=nomes_subtreinos)
    
    #  Checa se eh lista, o que leva para o treino direto
    else:
        return render_template('treino.html', nome_treino=nome, blocos=conteudo)

# Quando o usuário clica dentro da subpasta
@app.route('/treino/<categoria>/<subtreino>')
def abrir_subtreino(categoria, subtreino):
    # Pega os blocos específicos daquela subpasta
    blocos = workouts[categoria][subtreino]
    
    # Junta os nomes para o título
    nome_completo = f"{categoria} - {subtreino}"
    
    return render_template('treino.html', nome_treino=nome_completo, blocos=blocos)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')