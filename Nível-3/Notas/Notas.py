def pedir_notas ():
    notas = []
    for i in range(3):
        nota = float(input(f"Digite a sua {i + 1}º nota:"))
        notas.append(nota)
    return notas

print("Ola o sistema quer suas notas, informe abaixo: ")
notas_aluno = pedir_notas()

def maior_notas (notas_aluno):
    return max(notas_aluno)

def menor_notas (notas_aluno):
    return min(notas_aluno)

def media_notas(notas_aluno):
    return sum(notas_aluno) / len(notas_aluno)

def situacao_aluno (media):
    return "Aprovado!" if media > 5.9 else "Reprovado!"



def main(notas_aluno):
    print("---------------------------------------------------")
    media = media_notas(notas_aluno)
    print(f"A Media do Aluno foi: {media}")
    maior = maior_notas(notas_aluno)
    print(f"A Maior Nota do Aluno foi: {maior}")
    menor = menor_notas(notas_aluno)
    print(f"A Menor Nota do Aluno foi: {menor}")
    situacao = situacao_aluno(media)
    print(f"A Situacao do aluno: {situacao}")
    print("---------------------------------------------------")
main(notas_aluno)



