import os

from cadastro import Cadastro
from validacoes import validar_numero


# =========================
# FUNÇÕES AUXILIARES
# =========================

def limpar_tela():
	os.system("clear")


def pausar():
	input("\nPressione ENTER para continuar...")


def erro(mensagem):
	print(f"\n❌ {mensagem}")
	pausar()
	limpar_tela()


# =========================
# PROGRAMA PRINCIPAL
# =========================

cadastro = Cadastro()


while True:

	limpar_tela()

	print("╔══════════════════════════╗")
	print("║     SISTEMA DE PESSOAS   ║")
	print("╠══════════════════════════╣")
	print("║ 1 - Cadastrar            ║")
	print("║ 2 - Listar               ║")
	print("║ 3 - Buscar               ║")
	print("║ 4 - Editar               ║")
	print("║ 5 - Excluir              ║")
	print("║ 6 - Sair                 ║")
	print("╚══════════════════════════╝")

	escolha = validar_numero("\nEscolha: ")

	if escolha is None:
		continue

	match escolha:

		case 1:
			limpar_tela()
			cadastro.cadastrar()

		case 2:
			limpar_tela()
			cadastro.listar()

		case 3:
			limpar_tela()
			cadastro.buscar()

		case 4:
			limpar_tela()
			cadastro.editar()

		case 5:
			limpar_tela()
			cadastro.excluir()

		case 6:
			limpar_tela()
			print("Saindo...")
			break

		case _:
			erro("Opção inválida.")