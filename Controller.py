#Racíocinio Lógico
from Model import *

#Lógica da verificação onde se o input da tarefa está vazia ou não, e adiciona ou não a tarefa
class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
        self.tarefa = tarefa
    
        try:
            if self.tarefa == " " or self.tarefa == "":
                print("Informe uma tarefa válida")
            elif self.tarefa == int:
                print("Informe uma tarefa válida")
            else:
                if TODO.AdicionarTarefa(self.tarefa) == True:
                    print("A Tarefa foi Adicionada!")
                else:
                    print("Algum problema foi encontrado.")
        except Exception as erro:
            print("Erro:", erro._class.name_)

#Lógica da exclusão da tarefa ao passar o índice da tarefa
class ControllerExcluirTarefa():
    def __init__(self, excluir):
        self.excluir = excluir - 1 

        try:
            if self.excluir >= 0 and self.excluir < len(TODO.ListarTarefas()):
                tarefa_removida = TODO.ExcluirTarefa(self.excluir) 
                if tarefa_removida:
                    print(f"A Tarefa {tarefa_removida} foi excluída.")
                else:
                    print("Algum problema foi encontrado.")
            else:
                print("Índice inválido. Certifique-se que o índice existe.")
        except Exception as erro:
            print("Erro:", type(erro).__name__)

#Lógica que lista a tarefa e adiciona o índice na lista
class ControllerListarTarefa():
    def __init__(self):
        ControllerLista = TODO.ListarTarefas()
        cont = 1
        for tarefas in ControllerLista:
            print(f"{cont} -- {tarefas}")
            cont += 1

class Validacao():  
    def __init__(self, id, ids_salvos):
#Verifica se o número aleatório gerado já está salvo 
        while True:
            self.id = random.randint(1000, 9999)
            if self.id not in self.ids_salvos:
                True
                break
            else:
                print("Esse ID já existe.")
                break

                Arquivo.write(f"{self.id} - \t{tarefa}\n")
        
            self.ids_salvos.append(self.id)

        #Lista as tarefas atualizadas
        def listar_tarefas(self):
            with open(self.arquivo, 'r') as Arquivo:
                tarefas = Arquivo.readlines()
            return tarefas
