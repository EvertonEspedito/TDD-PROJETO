# 🧪 Projeto TDD em Python Backend

Este repositório contém um projeto desenvolvido durante o **bootcamp Santander Fullstack Developer**, promovido pela **Digital Innovation One (DIO)**. O objetivo principal foi aprender e aplicar **Test-Driven Development (TDD)** no desenvolvimento de uma aplicação backend com **Python**.

## 🚀 Objetivo do Projeto

Implementar uma API de forma **orientada a testes**, utilizando boas práticas de desenvolvimento backend. A ideia central é reforçar o ciclo **Red → Green → Refactor** do TDD, onde cada funcionalidade é guiada pela criação de testes automatizados antes da implementação do código real.

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **Pytest** — para criação e execução de testes automatizados
- **unittest** — biblioteca de testes nativa do Python (em conjunto com Pytest)
- **FastAPI** — framework leve e moderno para construção de APIs REST (se aplicável)
- **Poetry** — gerenciamento de dependências e ambiente virtual

## 📁 Estrutura do Projeto

TDD-PROJETO/
├── app/ # Código-fonte da aplicação
│ ├── init.py
│ └── main.py # Código principal
├── tests/ # Testes automatizados
│ └── test_main.py # Casos de teste
├── pyproject.toml # Configuração do Poetry e dependências
├── README.md # Documentação do projeto


## 🧪 O que é TDD?

**TDD (Test-Driven Development)** é uma metodologia de desenvolvimento de software onde os testes são escritos antes da implementação do código funcional. O ciclo básico é:

1. **Red** — Escrever um teste que falha
2. **Green** — Implementar o código mínimo necessário para passar no teste
3. **Refactor** — Melhorar o código mantendo os testes verdes

## ▶️ Como Executar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/EvertonEspedito/TDD-PROJETO.git
cd TDD-PROJETO
2. Instale o Poetry (caso não tenha)
pip install poetry
3. Instale as dependências

poetry install
4. Ative o ambiente virtual

poetry shell
5. Execute os testes

pytest
✅ Funcionalidades Implementadas
Estrutura básica com TDD

Casos de teste com pytest e unittest

Separação entre código e testes

Uso do assert para validações

Utilização do Poetry para gerenciamento de dependências

📚 Aprendizados
Durante o desenvolvimento deste projeto, foram praticados:

Fundamentos de TDD

Escrita de testes automatizados com pytest

Execução de testes no terminal

Integração de testes com a lógica de negócio

Organização de projetos Python com poetry

📄 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

👨‍💻 Desenvolvido por Everton Espedito
Durante o Bootcamp Santander | DIO
