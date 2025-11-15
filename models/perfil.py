from models.competencia import Competencia

class Perfil:
    def __init__(self, nome: str):
        self.nome = nome
        self.competencias = []

    def adicionar_competencia(self, nome, nivel):
        comp = Competencia(nome, nivel)
        self.competencias.append(comp)

    def obter_dicionario(self):
        return {c.nome: c.nivel for c in self.competencias}

    def __repr__(self):
        return f"Perfil: {self.nome}\nCompetências: {self.competencias}"