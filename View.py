from Controller import *
import os

sair = 0
while sair == 0:

    print("SOFTWARE TO-DO FAZER")
    print("--------------------")
    print("01 - ADICIONAR TAREFA") 
    print("02 - LISTAR TAREFA")
    print("03 - EXCLUIR TAREFA")
    print("04 - SAIR")
    print("")

    menu = int(input("Qual Opção deseja?\n>>"))

    match menu:
        case 1:
            os.system("cls")
            tarefa = input("Nome da tarefa >>")
            adicionarTarefa = ControllerAdicionarTarefa(tarefa)

        case 2:
            os.system("cls")
            ListarTarefa = ControllerListarTarefa()
            os.system("pause")
            os.system("cls")

        case 3:
            os.system("cls")
            ListarTarefa = ControllerListarTarefa()
            excluir = int(input("Digite o indice que deseja excluir\n>>"))
            ExcluirTarefa = ControllerExcluirTarefa(excluir)

        case 4:
            sair = 1
            

        case _:
            print("OPÇÃO INVÁLIDA")