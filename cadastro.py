from pessoa import Pessoa
from banco import BancoDeDados
from validacoes import (
	validar_texto,
	validar_idade,
	validar_numero,
	confirmar
)
import logging


class Cadastro:

	def __init__(self):
		self.banco = BancoDeDados()

	# =========================
	# CADASTRAR
	# =========================

	def cadastrar(self):

		print("\n=== CADASTRAR PESSOA ===")

		nome = validar_texto("Nome: ")

		if nome is None:
			return

		idade = validar_idade()

		if idade is None:
			return

		# Verificar se já existe
		for pessoa in self.banco.pessoas:

			if pessoa.nome.lower() == nome.lower():

				print("\n❌ Essa pessoa já está cadastrada.")
				input("\nPressione ENTER para continuar...")

				return

		# Criar ID
		id_pessoa = self.banco.gerar_id()

		# Criar objeto
		pessoa = Pessoa(
			nome,
			idade,
			id_pessoa
		)

		# Adicionar
		self.banco.pessoas.append(pessoa)

		# Salvar
		self.banco.salvar()

		logging.info(
			f"Pessoa cadastrada: {nome}"
		)

		print("\n✅ Pessoa cadastrada com sucesso!")
		print(f"ID: {pessoa.id}")

		input("\nPressione ENTER para continuar...")

	# =========================
	# LISTAR
	# =========================

	def listar(self):

		print("\n=== LISTA DE PESSOAS ===")

		if not self.banco.pessoas:

			print("\nNenhuma pessoa cadastrada.")

			input("\nPressione ENTER para continuar...")

			return

		for pessoa in self.banco.pessoas:

			print(f"\nID: {pessoa.id}")
			print(f"Nome: {pessoa.nome}")
			print(f"Idade: {pessoa.idade}")
			print(f"Cadastro: {pessoa.data_cadastro}")

		input("\nPressione ENTER para continuar...")

	# =========================
	# BUSCAR
	# =========================

	def buscar(self):

		print("\n=== BUSCAR PESSOA ===")

		if not self.banco.pessoas:

			print("\nNenhuma pessoa cadastrada.")

			input("\nPressione ENTER para continuar...")

			return

		print("\n1 - Buscar por nome")
		print("2 - Buscar por ID")
		print("3 - Buscar por idade")

		opcao = validar_numero("\nEscolha: ")

		if opcao is None:
			return

		encontradas = []

		# Buscar por nome
		if opcao == 1:

			nome = input("\nNome: ").strip().lower()

			if nome == "":
				print("\n❌ Digite um nome.")
				input("\nPressione ENTER para continuar...")
				return

			for pessoa in self.banco.pessoas:

				if nome in pessoa.nome.lower():
					encontradas.append(pessoa)

		# Buscar por ID
		elif opcao == 2:

			id_pessoa = validar_numero("\nID: ")

			if id_pessoa is None:
				return

			for pessoa in self.banco.pessoas:

				if pessoa.id == id_pessoa:
					encontradas.append(pessoa)

		# Buscar por idade
		elif opcao == 3:

			idade = validar_idade()

			if idade is None:
				return

			for pessoa in self.banco.pessoas:

				if pessoa.idade == idade:
					encontradas.append(pessoa)

		else:

			print("\n❌ Opção inválida.")
			input("\nPressione ENTER para continuar...")

			return

		if not encontradas:

			print("\n❌ Nenhuma pessoa encontrada.")

			input("\nPressione ENTER para continuar...")

			return

		print("\n=== RESULTADOS ===")

		for pessoa in encontradas:

			print(f"\nID: {pessoa.id}")
			print(f"Nome: {pessoa.nome}")
			print(f"Idade: {pessoa.idade}")
			print(f"Cadastro: {pessoa.data_cadastro}")

		input("\nPressione ENTER para continuar...")

	# =========================
	# EDITAR
	# =========================

	def editar(self):

		print("\n=== EDITAR PESSOA ===")

		if not self.banco.pessoas:

			print("\nNenhuma pessoa cadastrada.")

			input("\nPressione ENTER para continuar...")

			return

		self.listar()

		id_pessoa = validar_numero(
			"\nDigite o ID da pessoa: "
		)

		if id_pessoa is None:
			return

		for pessoa in self.banco.pessoas:

			if pessoa.id == id_pessoa:

				print(f"\nEditando: {pessoa.nome}")

				nome = validar_texto(
					"Novo nome: "
				)

				if nome is None:
					return

				idade = validar_idade()

				if idade is None:
					return

				pessoa.nome = nome
				pessoa.idade = idade

				self.banco.salvar()

				logging.info(
					f"Pessoa editada: ID {id_pessoa}"
				)

				print("\n✅ Pessoa editada com sucesso!")

				input("\nPressione ENTER para continuar...")

				return

		print("\n❌ ID não encontrado.")

		input("\nPressione ENTER para continuar...")

	# =========================
	# EXCLUIR
	# =========================

	def excluir(self):

		print("\n=== EXCLUIR PESSOA ===")

		if not self.banco.pessoas:

			print("\nNenhuma pessoa cadastrada.")

			input("\nPressione ENTER para continuar...")

			return

		self.listar()

		id_pessoa = validar_numero(
			"\nDigite o ID da pessoa: "
		)

		if id_pessoa is None:
			return

		for pessoa in self.banco.pessoas:

			if pessoa.id == id_pessoa:

				print(f"\nPessoa: {pessoa.nome}")

				if not confirmar(
					"Tem certeza que deseja excluir?"
				):

					print("\nOperação cancelada.")

					input(
						"\nPressione ENTER para continuar..."
					)

					return

				self.banco.pessoas.remove(pessoa)

				self.banco.salvar()

				logging.info(
					f"Pessoa excluída: ID {id_pessoa}"
				)

				print("\n✅ Pessoa excluída com sucesso!")

				input(
					"\nPressione ENTER para continuar..."
				)

				return

		print("\n❌ ID não encontrado.")

		input("\nPressione ENTER para continuar...")