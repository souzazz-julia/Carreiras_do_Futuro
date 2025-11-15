from models.perfil import Perfil
from services.recomendador import Recomendador

def menu():
    """
    Exibe o menu principal da aplicação e retorna a opção escolhida.
    """
    print("\nFuture Skills Lab — Orientação de Carreiras do Futuro")
    print("1. Criar / trocar perfil")
    print("2. Responder questionário de competências (0 a 10)")
    print("3. Ver perfil atual")
    print("4. Ver recomendações de carreira")
    print("5. Sair")
    return input("Escolha uma opção: ").strip()


def preencher_competencias(perfil: Perfil, recomendador: Recomendador):
    """
    Pergunta ao usuário uma nota de 0 a 10 para cada competência disponível.

    As respostas são gravadas no objeto Perfil.
    """
    print("\nQuestionário de Competências")
    print("Avalie cada competência de 0 a 10.")
    print("0 = não tenho essa habilidade | 10 = muito forte em mim\n")

    perfil.limpar_competencias()
    for nome_comp in recomendador.obter_competencias():
        while True:
            try:
                entrada = input(f"{nome_comp}: ")
                nivel = int(entrada)
                if 0 <= nivel <= 10:
                    perfil.adicionar_competencia(nome_comp, nivel)
                    break
                else:
                    print("Por favor, digite um número inteiro de 0 a 10.")
            except ValueError:
                print("Entrada inválida. Digite apenas números inteiros de 0 a 10.")


def mostrar_perfil(perfil: Perfil):
    """
    Exibe na tela o perfil atual e as competências já preenchidas.
    """
    if not perfil:
        print("Nenhum perfil criado ainda.")
        return

    print(f"\nPerfil de {perfil.nome}")
    if not perfil.competencias:
        print("Ainda não há competências cadastradas. "
              "Use a opção 2 para responder o questionário.")
        return

    for comp in perfil.competencias:
        print(f"- {comp.nome}: {comp.nivel}/10")


def mostrar_recomendacoes(perfil: Perfil, recomendador: Recomendador):
    """
    Exibe as recomendações de carreira, mostrando:
      - compatibilidade (%)
      - pontos fortes
      - competências para desenvolver
      - breve descrição da carreira.
    """
    if not perfil:
        print("Crie um perfil primeiro!")
        return

    if not perfil.competencias:
        print("Você ainda não respondeu o questionário de competências.")
        print("Use a opção 2 do menu para preencher suas habilidades.")
        return

    resultados = recomendador.recomendar(perfil)

    print(f"\nRecomendações para {perfil.nome}")
    for resultado in resultados:
        carreira = resultado["carreira"]
        compat = resultado["compatibilidade"]
        forcas = resultado["forcas"]
        a_desenvolver = resultado["a_desenvolver"]

        print("\n-------------------------------------")
        print(f"   Carreira do futuro: {carreira.nome}")
        print(f"   Sobre a carreira: {carreira.descricao}")
        print(f"   Compatibilidade estimada: {compat}%")

        if forcas:
            print("Seus pontos fortes para essa carreira:")
            for nome, nivel in forcas:
                print(f"      - {nome}: nível {nivel}")
        else:
            print("Ainda não há competências fortes para essa carreira.")

        if a_desenvolver:
            print("Competências para desenvolver para essa carreira no futuro do trabalho:")
            for nome, nivel_atual, nivel_meta in a_desenvolver:
                print(f"      - {nome}: você tem {nivel_atual}, ideal ≥ {nivel_meta}")
        else:
            print("Você já tem nível forte nas competências principais dessa carreira!")


def main():
    """
    Ponto de entrada da aplicação (CLI).
    Organiza o fluxo principal do sistema.
    """
    recomendador = Recomendador()
    perfil = None

    print("Bem-vindo ao Future Skills Lab!")
    print("Este simulador ajuda você a descobrir quais carreiras do futuro")
    print("mais combinam com o seu conjunto de competências.\n")

    while True:
        opcao = menu()

        if opcao == "1":
            nome = input("Nome do usuário: ").strip()
            if not nome:
                print("Nome não pode ser vazio.")
                continue
            perfil = Perfil(nome)
            print(f"Perfil criado para: {perfil.nome}")


        elif opcao == "2":
            if perfil is None:

                print("\nVocê ainda não tem um perfil. Vamos criar um agora.")

                nome = input("Nome do usuário: ").strip()

                while not nome:
                    print("Nome não pode ser vazio.")

                    nome = input("Nome do usuário: ").strip()

                perfil = Perfil(nome)

                print(f"Perfil criado para: {perfil.nome}")

            print(f"\nPreenchendo competências para o perfil: {perfil.nome}")

            preencher_competencias(perfil, recomendador)

            print("\nCompetências registradas com sucesso!")

        elif opcao == "3":
            mostrar_perfil(perfil)

        elif opcao == "4":
            mostrar_recomendacoes(perfil, recomendador)

        elif opcao == "5":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()