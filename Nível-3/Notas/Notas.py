def pedir_notas ():
    notas = []
    for i in range(3):
        nota = float(input(f"Digite a sua {i + 1}º nota:"))
        notas.append(nota)
    return notas

def printar_notas():
    for nota in notas:
        print(f"As Notas foram: {nota}")

def media_notas():
    media = sum(notas) / len(notas)
    print(f"Sua média é: {media}")
    return media

#
# def status():
#   media_notas
#   if(media > 5.9):
#       print("Aluno esta aprovado")
#   else: 
#       print("Aluno esta aprovado")
#

def maior_e_menor(notas):
    maior = max(notas)
    menor = min(notas)
    print(f"A maior nota foi: {maior}")
    print(f"A menor nota foi: {menor}")
    return maior, menor
print("Ola o sistema quer suas notas, informe abaixo: ")
pedir_notas()
maior_e_menor()


