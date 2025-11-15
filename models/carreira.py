class Carreira:
    def __init__(self, nome: str, competencias_relevantes: dict):
        self.nome = nome
        # Ex: {"Lógica": 7, "Criatividade": 6}
        self.competencias_relevantes = competencias_relevantes

    def __repr__(self):
        return f"{self.nome} (requer: {self.competencias_relevantes})"