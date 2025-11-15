class Competencia:
    """
    Representa uma competência avaliada no perfil do usuário.

    Atributos:
        nome (str): nome da competência (ex: 'Lógica', 'Criatividade').
        nivel (int): nível de 0 a 10 informado pelo usuário.
    """

    def __init__(self, nome: str, nivel: int):
        self.nome = nome
        self.nivel = nivel

    def __repr__(self):
        return f"{self.nome}: {self.nivel}/10"