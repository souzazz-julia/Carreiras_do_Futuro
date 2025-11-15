class Carreira:
    """
    Representa uma carreira do futuro, com competências importantes
    e uma breve descrição sobre o papel desse profissional.

    Atributos:
        nome (str): nome da carreira (ex: 'Desenvolvedor de IA').
        competencias_relevantes (dict[str, int]): competências e pesos de importância (1 a 10).
        descricao (str): texto curto explicando a carreira.
    """

    def __init__(self, nome: str, competencias_relevantes: dict, descricao: str):
        self.nome = nome
        self.competencias_relevantes = competencias_relevantes
        self.descricao = descricao

    def calcular_compatibilidade(self, competencias_perfil: dict) -> dict:
        """
        Calcula a compatibilidade entre esta carreira e o perfil informado.

        Args:
            competencias_perfil (dict): mapa {competência: nível (0 a 10)} do usuário.

        Returns:
            dict com:
                - 'score_bruto': pontuação ponderada.
                - 'compatibilidade': porcentagem de 0 a 100.
                - 'forcas': lista de tuplas (competência, nível_usuario).
                - 'a_desenvolver': lista de tuplas (competência, nível_atual, nível_meta).
        """
        score = 0
        max_score = 0
        forcas = []
        a_desenvolver = []

        for competencia, peso in self.competencias_relevantes.items():
            max_score += 10 * peso

            nivel_usuario = competencias_perfil.get(competencia, 0)
            score += nivel_usuario * peso

            if nivel_usuario >= 7:
                forcas.append((competencia, nivel_usuario))
            else:
                nivel_meta = 7
                a_desenvolver.append((competencia, nivel_usuario, nivel_meta))

        if max_score == 0:
            compatibilidade = 0.0
        else:
            compatibilidade = round((score / max_score) * 100, 1)

        return {
            "score_bruto": score,
            "compatibilidade": compatibilidade,
            "forcas": forcas,
            "a_desenvolver": a_desenvolver,
        }

    def __repr__(self):
        return f"{self.nome} (carreira do futuro)"