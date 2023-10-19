from Model import *
import os   

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
        self.tarefa = tarefa

        if self.tarefa == " ":
            print("Informe uma tarefa válida")
        
        else:
            if TODO.AdicionarTarefa(self.tarefa) == True:
                print("Tarefa Adicionada")
                os.system("cls")

            else:
                print("Algum problema foi encontrado")

class ControllerExcluirTarefa():
    def __init__(self, excluir):
        self.excluir = excluir - 1

        if TODO.ExcluirTarefa(self.excluir) == True:
            print("Tarefa Excluída")
            os.system("cls")
        else:
            print("Algum problema foi encontrado")

class ControllerListarTarefa():
    def __init__(self):
        ControllerLista = TODO.ListarTarefa()
        cont = 1
        for tarefas in ControllerLista:
            print(f"{cont} - {tarefas}")
            cont += 1  
