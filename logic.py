# logic.py

def concluir_serie(exercicio):
    #Funcao para a contagem de series feitas de exercicios simples
    if exercicio["feitas"] < exercicio["series"]:
        exercicio["feitas"] += 1

    return exercicio["feitas"] == exercicio["series"]


def concluir_bloco(bloco):
    #Funcao para a contagem de series feitas de exercicios conjugados
    if bloco["feitas"] < bloco["series"]:
        bloco["feitas"] += 1

    return bloco["feitas"] == bloco["series"]


def verificar_treino_blocos(blocos):
    #Funcao para verificar o estado(completo ou nao) dos exercicio.
    for bloco in blocos:
        if bloco["tipo"] == "simples":
            for ex in bloco["exercicios"]:
                if ex["feitas"] < ex["series"]:
                    return False
        else:
            if bloco["feitas"] < bloco["series"]:
                return False
    return True


def resetar_blocos(blocos):
    #Funcao para zerar o estado dos exercicios apos finalizar o treino.
    for bloco in blocos:
        if bloco["tipo"] == "simples":
            for ex in bloco["exercicios"]:
                ex["feitas"] = 0
        else:
            bloco["feitas"] = 0