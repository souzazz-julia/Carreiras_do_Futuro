from models.competencia import Competencia

class Perfil:
    """
    Representa o perfil de uma pessoa que quer descobrir carreiras do futuro.

    Atributos:
        nome (str): nome do usuário.
        competencias (list[Competencia]): lista de competências avaliadas.
    """

    def __init__(self, nome: str):
        self.nome = nome
        self.competencias = []

    def limpar_competencias(self):
        """
        Remove todas as competências cadastradas para permitir
        preencher o questionário novamente do zero.
        """
        self.competencias = []

    def adicionar_competencia(self, nome: str, nivel: int):
        """
        Adiciona uma nova competência ao perfil.

        O nome é normalizado para formato Título (ex: 'lógica' -> 'Lógica').
        """
        nome_normalizado = nome.strip().title()
        comp = Competencia(nome_normalizado, nivel)
        self.competencias.append(comp)

    def obter_dicionario(self):
        """
        Retorna as competências como dicionário:
        { 'Lógica': 8, 'Criatividade': 6, ... }
        """
        return {c.nome: c.nivel for c in self.competencias}

    def __repr__(self):
        return f"Perfil: {self.nome}\nCompetências: {self.competencias}"