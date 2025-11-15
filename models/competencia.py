class Competencia:
    def __init__(self, nome: str, nivel: int):
        self.nome = nome
        self.nivel = nivel  # 0 a 10

    def __repr__(self):
        return f"{self.nome}: {self.nivel}/10"