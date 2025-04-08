
# ✅ Checklist: Gerenciador de Tarefas (To-Do List)

## 🔹 Parte 1: Estrutura Básica
- [ ] Criar uma estrutura para armazenar uma tarefa (ex: dicionário com título, descrição, status).
- [ ] Criar uma lista para armazenar todas as tarefas.
- [ ] Implementar um loop principal com um menu de opções.

## 🔹 Parte 2: Funcionalidades Principais
- [ ] **Adicionar tarefa:**
  - [ ] Receber do usuário o título da tarefa.
  - [ ] Receber a descrição da tarefa.
  - [ ] Definir status como "pendente" por padrão.
  - [ ] Adicionar a tarefa à lista.

- [ ] **Listar tarefas:**
  - [ ] Mostrar todas as tarefas registradas com título, status e um número de identificação.
  - [ ] (Opcional) Mostrar também a descrição.

- [ ] **Marcar tarefa como concluída:**
  - [ ] Permitir que o usuário escolha a tarefa pelo número ou nome.
  - [ ] Alterar o status para “concluída”.

- [ ] **Remover tarefa:**
  - [ ] Permitir selecionar uma tarefa para removê-la da lista.

## 🔹 Parte 3: Manipulação de Arquivos
- [ ] **Salvar tarefas em arquivo:**
  - [ ] Ao sair do programa, salvar todas as tarefas em um arquivo `.txt` ou `.csv`.

- [ ] **Carregar tarefas ao iniciar:**
  - [ ] Ao iniciar o programa, ler o arquivo e carregar as tarefas salvas.

## 🔹 Parte 4: Organização com Funções
- [ ] Criar uma função para cada ação:
  - [ ] `adicionar_tarefa()`
  - [ ] `listar_tarefas()`
  - [ ] `marcar_como_concluida()`
  - [ ] `remover_tarefa()`
  - [ ] `salvar_tarefas_em_arquivo()`
  - [ ] `carregar_tarefas_do_arquivo()`

## 🔹 Parte 5: Extras/Opcionais
- [ ] Permitir editar título ou descrição de uma tarefa.
- [ ] Filtrar tarefas por status (pendente/concluída).
- [ ] Adicionar data de criação da tarefa.
- [ ] Ordenar tarefas por título ou data.
- [ ] Interface mais amigável no console (separadores, cores com `colorama`, etc.)
