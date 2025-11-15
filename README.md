# Future Skills Lab — Orientação de Carreiras do Futuro

Projeto desenvolvido para a **Global Solution 2025.2** de  
**Pensamento Computacional e Automação com Python**.

O objetivo é simular uma ferramenta inteligente de **orientação de carreiras**, focada em
**profissionais do futuro**. A aplicação analisa um conjunto de competências técnicas e
comportamentais e estima a compatibilidade do usuário com diferentes carreiras emergentes.

---

## Propósito do Projeto

No contexto do **Future Skills Lab**, o sistema ajuda a responder:

> “Como minhas competências atuais se conectam com as profissões do futuro?”

A aplicação:

- coleta uma autoavaliação do usuário (0 a 10) em várias competências;
- compara o perfil com diferentes carreiras do futuro;
- calcula uma **porcentagem de compatibilidade** para cada carreira;
- mostra **pontos fortes** e **competências a desenvolver**.

---

## Tecnologias e Conceitos Utilizados

- Linguagem: **Python 3**
- Paradigma: **Programação Orientada a Objetos (POO)**
- Estruturas de dados: **listas, dicionários e tuplas**
- Organização em **módulos e classes**
- Interface textual simples (**CLI**)

Classes principais:

- `Competencia` — representa uma competência com nível de 0 a 10.
- `Perfil` — armazena o nome do usuário e suas competências.
- `Carreira` — descreve uma carreira do futuro e as competências mais importantes.
- `Recomendador` — calcula a compatibilidade entre o perfil e cada carreira.

---

## Estrutura de Arquivos

```text
future-skills-lab/
│
├── main.py
├── models/
│   ├── competencia.py
│   ├── perfil.py
│   └── carreira.py
└── services/
    └── recomendador.py