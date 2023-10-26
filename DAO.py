class DAO:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.cont = 1
        self.titulos_adicionados = False

    def adicionar_tarefa(self, tarefa):
        with open(self.arquivo, 'a') as Arquivo:
            if not self.titulos_adicionados:
                Arquivo.write("ID \t TAREFA\n\n")
                self.titulos_adicionados = True
            Arquivo.write(f"{self.cont}:\t{tarefa}\n")
        self.cont += 1

    def listar_tarefas(self):
        with open(self.arquivo, 'r') as Arquivo:
            tarefas = Arquivo.readlines()
        return tarefas