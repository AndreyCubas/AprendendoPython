alunos = [
    ("Andrey",17,80),
    ("Jair", 17, 90),
    ("Valerio", 17, 85)
]
print("Lista de Alunos")
for aluno in alunos:
    nome, idade, nota = aluno
    print(f"Nome: {nome} Idade: {idade} Nota: {nota}")