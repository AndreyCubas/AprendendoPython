titulo = str(input("Digite o titulo da tarefa: "))
descricao = str(input("Digite uma descricao da tarefa: "))
status = False

tarefa = {
    "Titulo: " : titulo,
    "Descricao: " : descricao,
    "Status: " : status    
    }
listaTarefas = []

def adicionarTarefa(titulo, descricao, status):
    listaTarefas.append(tarefa)
    
    
while(True):
    print("--------MENU-------")
    print("1-Adicionar Tarefa")
    print("2-Listar Tarefas")
    print("3-Remover Tarefa")
    print("4-Concluir Tarefa")
    print("5-Sair")
    opcao = int(input("Escolha uma opcao: "))
    if opcao == 1:
