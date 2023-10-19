class DAO():
    def init(self, arquivo):
        self.arquivo = arquivo

    def adicionar_tarefa(self, tarefa):
        with open(self.arquivo, 'a') as Arquivo:
            Arquivo.write(tarefa + '\\n')

    def listar_tarefa(self, lista):
        with open(self.arquivo, 'w') as Arquivo:
            for tarefa in lista:
                Arquivo.write(tarefa + '\\n')   