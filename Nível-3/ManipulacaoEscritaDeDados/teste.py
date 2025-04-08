import json

nome = str(input("Digite o seu nome"))
idade = int(input("Digite a sua idade"))
dados = {"Nome":  nome, "Idade ": idade}

with open ("Dados-do-Aluno.json", "w") as f:
    json.dump(dados, f)

with open("Dados-do-Aluno.json", "r") as f:
    dados = json.load(f)
    print(dados["Nome"]) 