class Contacto:
	"""Entidad Contacto.

	Implementación mínima: métodos y firmas listos para completar.
	"""

	def __init__(self, id, nombre, telefono=None, correo=None):
		"""Inicializa un contacto.

		Args:
			id: Identificador del contacto (puede ser None al crear uno nuevo).
			nombre: Nombre del contacto.
			telefono: Teléfono (opcional).
			correo: Correo electrónico (opcional).
		"""
		self.id = id
		self.nombre = nombre
		self.telefono = telefono
		self.correo = correo

	def __str__(self):
		"""Representación legible del contacto."""
		# TODO: completar la representación
		return f"Contacto(id={self.id}, nombre={self.nombre}, telefono={self.telefono}, correo={self.correo})"

	def to_dict(self):
		"""Serializar a diccionario.

		Devuelve un dict con las claves: 'id', 'nombre', 'telefono', 'correo'.
		"""
		# TODO: ajustar serialización si añades campos
		return {
			'id': self.id,
			'nombre': self.nombre,
			'telefono': self.telefono,
			'correo': self.correo,
		}

	@staticmethod
	def from_dict(d):
		"""Crear un Contacto a partir de un diccionario.

		Args:
			d: dict con claves compatibles.
		"""
		# TODO: validar campos y tipos si es necesario
		return Contacto(
			id=d.get('id'),
			nombre=d.get('nombre'),
			telefono=d.get('telefono'),
			correo=d.get('correo'),
		)
