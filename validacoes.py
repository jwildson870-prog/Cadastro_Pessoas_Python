def pausar():
	input("\nPressione ENTER para continuar...")


def erro(mensagem):
	print(f"\n❌ {mensagem}")
	pausar()


# =========================
# VALIDAR TEXTO
# =========================

def validar_texto(mensagem):

	valor = input(mensagem).strip()

	if not valor:

		erro("O campo não pode ficar vazio.")

		return None

	if not valor.replace(" ", "").isalpha():

		erro("Digite apenas letras.")

		return None

	return valor


# =========================
# VALIDAR NÚMERO
# =========================

def validar_numero(mensagem):

	try:

		valor = int(input(mensagem))

		if valor < 0:

			erro("Digite um número positivo.")

			return None

		return valor

	except ValueError:

		erro("Digite apenas números.")

		return None


# =========================
# VALIDAR IDADE
# =========================

def validar_idade():

	idade = validar_numero("Idade: ")

	if idade is None:
		return None

	if idade > 120:

		erro("Digite uma idade válida.")

		return None

	return idade


# =========================
# CONFIRMAR
# =========================

def confirmar(mensagem):

	while True:

		resposta = input(
			f"\n{mensagem} (S/N): "
		).strip().lower()

		if resposta == "s":

			return True

		if resposta == "n":

			return False

		print("\n❌ Digite apenas S ou N.")