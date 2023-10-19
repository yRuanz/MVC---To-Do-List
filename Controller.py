from Model import *

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


class ControllerListarTarefa():
    def __init__(self):
        ControllerLista = TODO.ListarTarefas()
        cont = 1
        for tarefas in ControllerLista:
            print(f"{cont} -- {tarefas}")
            cont += 1