from models.carreira import Carreira

class Recomendador:

    def __init__(self):
        self.carreiras = [
            Carreira("Desenvolvedor de IA", {
                "Lógica": 7, "Matemática": 7, "Análise de Problemas": 6
            }),
            Carreira("Designer UX/UI", {
                "Criatividade": 8, "Comunicação": 6, "Empatia": 7
            }),
            Carreira("Cientista de Dados", {
                "Lógica": 8, "Matemática": 9, "Curiosidade": 7
            }),
            Carreira("Gerente de Projetos", {
                "Organização": 7, "Colaboração": 7, "Adaptabilidade": 6
            }),
        ]

    def recomendar(self, perfil):
        perfil_dict = perfil.obter_dicionario()
        ranking = []

        for carreira in self.carreiras:
            score = 0
            for comp, nivel_min in carreira.competencias_relevantes.items():
                nivel_usuario = perfil_dict.get(comp, 0)
                score += min(nivel_usuario, nivel_min)

            ranking.append((carreira.nome, score))

        ranking.sort(key=lambda x: x[1], reverse=True)
        return ranking