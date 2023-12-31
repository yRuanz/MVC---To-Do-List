#Interação com o usuário
from Controller import *
import os

sair = 0
while sair == 0:
    os.system("cls")
    print("  SOFTWARE DE TO-DO 1")
    print("----------------------")
    print("01 - ADICIONAR TAREFA")
    print("02 - LISTAR TAREFAS")
    print("03 - EXCLUIR TAREFA")
    print("04 - SAIR")
    print("")
    menu = int(input("QUAL OPÇÃO DESEJA > "))

    try:
        match menu:
            case 1:
                os.system("cls")
                tarefa = input("Adicione uma TAREFA >> ")
                adicionarTarefa = ControllerAdicionarTarefa(tarefa)
                os.system("pause")
                os.system("cls")

            case 2:
                os.system("cls")
                listarTarefa = ControllerListarTarefa()
                os.system("pause")
                os.system("cls")

            case 3:
                os.system("cls")
                listarTarefa = ControllerListarTarefa()
                alterar = int(input("Qual o índice da tarefa que deseja alterar >> "))

            case 4:
                os.system("cls")
                listarTarefa = ControllerListarTarefa()
                concluir = int(input("Qual o índice da tarefa que deseja concluir >> "))

            case 5:
                os.system("cls")
                listarTarefa = ControllerListarTarefa()
                excluir = int(input("Qual o índice da tarefa que deseja excluir >> "))
                excluirTarefa = ControllerExcluirTarefa(excluir)
                os.system("pause")
                os.system("cls")

            case 6:
                sair = 1
                os.system("cls")

            case _:
                print("Opção Inválida.")
    except Exception as erro:
        print("Opção inválida.")
        print("Erro:", erro.__class__.__name__)
        os.system("pause")
        os.system("cls")