import os
import json
import shutil
import logging
import uuid

from pessoa import Pessoa


ARQUIVO = "pessoas.json"
BACKUP = "pessoas_backup.json"


class BancoDeDados:

	def __init__(self):

		self.pessoas = []

		self.carregar()

	# =========================
	# CARREGAR DADOS
	# =========================

	def carregar(self):

		if not os.path.exists(ARQUIVO):
			return

		try:

			with open(
				ARQUIVO,
				"r",
				encoding="utf-8"
			) as arquivo:

				dados = json.load(arquivo)

			for dados_pessoa in dados:

				pessoa = Pessoa.from_dict(
					dados_pessoa
				)

				self.pessoas.append(pessoa)

			logging.info(
				"Dados carregados com sucesso."
			)

		except (
			json.JSONDecodeError,
			KeyError,
			TypeError
		) as erro:

			logging.error(
				f"Erro ao carregar dados: {erro}"
			)

	# =========================
	# SALVAR DADOS
	# =========================

	def salvar(self):

		try:

			if os.path.exists(ARQUIVO):

				shutil.copy(
					ARQUIVO,
					BACKUP
				)

			dados = []

			for pessoa in self.pessoas:

				dados.append(
					pessoa.to_dict()
				)

			with open(
				ARQUIVO,
				"w",
				encoding="utf-8"
			) as arquivo:

				json.dump(
					dados,
					arquivo,
					ensure_ascii=False,
					indent=4
				)

			logging.info(
				"Dados salvos com sucesso."
			)

		except OSError as erro:

			logging.error(
				f"Erro ao salvar dados: {erro}"
			)

	# =========================
	# GERAR ID
	# =========================

	def gerar_id(self):

		return uuid.uuid4().hex[:8]