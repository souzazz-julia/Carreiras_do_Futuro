from models.carreira import Carreira


class Recomendador:
    """
    Centraliza o catálogo de competências e carreiras
    e recomenda quais profissões do futuro combinam mais com o perfil.
    """

    def __init__(self):
        self.competencias_disponiveis = [
            "Lógica",
            "Matemática",
            "Programação",
            "Criatividade",
            "Comunicação",
            "Colaboração",
            "Pensamento Crítico",
            "Adaptabilidade",
            "Aprendizado Contínuo",
            "Empatia",
            "Liderança",
            "Organização",
            "Foco No Usuário",
            "Segurança Digital",
            "Resolução De Problemas",
            "Gestão De Tempo",
            "Inovação",
            "Visão De Negócio",
            "Inglês",
            "Excel",
            "Curiosidade",
            "Atenção A Detalhes",
        ]

        self.carreiras = [
            Carreira(
                "Desenvolvedor de IA",
                {
                    "Programação": 9,
                    "Lógica": 8,
                    "Matemática": 8,
                    "Resolução De Problemas": 8,
                    "Aprendizado Contínuo": 7,
                    "Inglês": 6,
                },
                "Cria e treina modelos de inteligência artificial para automatizar decisões "
                "e resolver problemas complexos em empresas digitais."
            ),
            Carreira(
                "Cientista de Dados",
                {
                    "Matemática": 9,
                    "Programação": 8,
                    "Curiosidade": 8,
                    "Resolução De Problemas": 8,
                    "Excel": 7,
                    "Pensamento Crítico": 7,
                    "Inglês": 6,
                },
                "Analisa grandes volumes de dados para gerar insights e apoiar decisões "
                "estratégicas em organizações orientadas a dados."
            ),
            Carreira(
                "Designer UX/UI",
                {
                    "Criatividade": 9,
                    "Foco No Usuário": 9,
                    "Empatia": 8,
                    "Comunicação": 7,
                    "Colaboração": 7,
                    "Pensamento Crítico": 6,
                },
                "Planeja experiências digitais centradas no usuário, desenhando interfaces "
                "intuitivas para produtos e serviços digitais."
            ),
            Carreira(
                "Product Owner",
                {
                    "Comunicação": 9,
                    "Visão De Negócio": 9,
                    "Colaboração": 8,
                    "Organização": 8,
                    "Foco No Usuário": 8,
                    "Gestão De Tempo": 7,
                    "Liderança": 7,
                    "Inovação": 6,
                },
                "Atua como ponte entre negócio e tecnologia, priorizando o backlog e "
                "garantindo que o produto entregue gere valor real."
            ),
            Carreira(
                "Gerente de Inovação",
                {
                    "Inovação": 10,
                    "Visão De Negócio": 9,
                    "Pensamento Crítico": 8,
                    "Comunicação": 8,
                    "Colaboração": 7,
                    "Adaptabilidade": 7,
                    "Liderança": 7,
                    "Curiosidade": 7,
                },
                "Lidera iniciativas de inovação, testando novas ideias e modelos de negócio "
                "para preparar a empresa para o futuro do trabalho."
            ),
            Carreira(
                "Especialista em Segurança Cibernética",
                {
                    "Segurança Digital": 10,
                    "Lógica": 8,
                    "Programação": 7,
                    "Resolução De Problemas": 8,
                    "Atenção A Detalhes": 9,
                    "Inglês": 7,
                    "Pensamento Crítico": 7,
                },
                "Protege sistemas e dados contra ataques, fraudes e vulnerabilidades em um "
                "mundo cada vez mais conectado."
            ),
            Carreira(
                "Desenvolvedor de Wearables (IoT)",
                {
                    "Programação": 9,
                    "Lógica": 8,
                    "Resolução De Problemas": 8,
                    "Inovação": 8,
                    "Foco No Usuário": 7,
                    "Curiosidade": 7,
                    "Adaptabilidade": 6,
                },
                "Desenvolve soluções de software embarcado em dispositivos vestíveis "
                "(wearables) e Internet das Coisas para o dia a dia."
            ),
            Carreira(
                "Gerente de Projetos (Agile)",
                {
                    "Organização": 9,
                    "Colaboração": 8,
                    "Comunicação": 8,
                    "Gestão De Tempo": 8,
                    "Adaptabilidade": 7,
                    "Liderança": 7,
                },
                "Coordena times multidisciplinares usando métodos ágeis para entregar "
                "projetos de forma rápida e iterativa."
            ),
        ]

    def obter_competencias(self):
        """Retorna a lista de competências disponíveis para o questionário."""
        return self.competencias_disponiveis

    def recomendar(self, perfil):
        """
        Calcula a compatibilidade do perfil com cada carreira.

        Retorna uma lista de dicionários, cada um contendo:
            - 'carreira' (objeto Carreira)
            - 'compatibilidade' (float)
            - 'score_bruto' (float)
            - 'forcas' (list[tuple])
            - 'a_desenvolver' (list[tuple])
        """
        competencias_perfil = perfil.obter_dicionario()
        resultados = []

        for carreira in self.carreiras:
            resultado = carreira.calcular_compatibilidade(competencias_perfil)
            resultado["carreira"] = carreira
            resultados.append(resultado)

        resultados.sort(key=lambda x: x["compatibilidade"], reverse=True)
        return resultados