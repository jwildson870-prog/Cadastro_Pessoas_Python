from datetime import datetime


class Pessoa:

	def __init__(
		self,
		nome,
		idade,
		id,
		data_cadastro=None
	):
		self.id = id
		self.nome = nome
		self.idade = idade

		self.data_cadastro = (
			data_cadastro
			or datetime.now().strftime(
				"%d/%m/%Y %H:%M"
			)
		)

	def to_dict(self):
		return {
			"id": self.id,
			"nome": self.nome,
			"idade": self.idade,
			"data_cadastro": self.data_cadastro
		}

	@classmethod
	def from_dict(cls, dados):
		return cls(
			dados["nome"],
			dados["idade"],
			dados["id"],
			dados["data_cadastro"]
		)