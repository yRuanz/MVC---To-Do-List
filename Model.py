from DAO import *

dao = DAO("Tarefa.txt")

class ToDo():
    def __init__(self):
        self.lista = []
        

    def AdicionarTarefa(self, tarefa):
        dao.adicionar_tarefa(tarefa)
        self.lista.append(tarefa)  
        return True

    def ExcluirTarefa(self, excluir):
        if excluir >= 0 and excluir < len(self.lista):
            tarefa_removida = self.lista.pop(excluir)
            dao.listar_tarefa(self.lista) 
            return tarefa_removida
        else:
            return None

    def ListarTarefas(self):
        return self.lista

TODO = ToDo()