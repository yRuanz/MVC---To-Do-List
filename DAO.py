#Banco de Dados
import random


class DAO:

    #Instância as variáveis
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.ids_salvos = []
        self.id = random.randint(1000, 9999)
        self.titulos_adicionados = False

    #Cria a função de adicionar tarefa
    def adicionar_tarefa(self, tarefa):
        with open(self.arquivo, 'a') as Arquivo:
            if not self.titulos_adicionados:
                Arquivo.write("ID \t TAREFA\n\n")
                self.titulos_adicionados = True
    #Adiciona o ID e a TAREFA no arquivo txt quando não tiver títulos adicionados

    #Cria um while que verifica se o número aleatório gerado já está salvo 
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

    
