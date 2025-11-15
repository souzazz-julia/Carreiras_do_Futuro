from models.perfil import Perfil
from services.recomendador import Recomendador

def menu():
    print("\n===== Future Skills Lab — Orientação de Carreiras =====")
    print("1. Criar perfil")
    print("2. Adicionar competência")
    print("3. Ver recomendações")
    print("4. Sair")
    return input("Escolha uma opção: ")

def main():
    recomendador = Recomendador()
    perfil = None

    while True:
        opcao = menu()

        if opcao == "1":
            nome = input("Nome do usuário: ")
            perfil = Perfil(nome)
            print(f"Perfil criado: {perfil.nome}")

        elif opcao == "2":
            if not perfil:
                print("Crie um perfil primeiro!")
                continue
            nome = input("Nome da competência: ")
            nivel = int(input("Nível (0 a 10): "))
            perfil.adicionar_competencia(nome, nivel)
            print("Competência adicionada!")

        elif opcao == "3":
            if not perfil:
                print("Crie um perfil primeiro!")
                continue
            ranking = recomendador.recomendar(perfil)
            print("\n===== Recomendações =====")
            for carreira, nota in ranking:
                print(f"{carreira}: score {nota}")

        elif opcao == "4":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()