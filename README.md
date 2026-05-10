# Sistema de Gerenciamento de Tarefas Web

## Objetivo do Projeto
Desenvolver um sistema web básico de gerenciamento de tarefas com suporte a criação, listagem, atualização e remoção de tarefas. O projeto também inclui priorização de tarefas e testes automatizados para garantir qualidade.

## Estrutura do Projeto
- `src/` — código fonte do aplicativo e templates HTML.
- `tests/` — testes automatizados com Pytest.
- `docs/` — documentação teórica e materiais de entrega.
- `.github/workflows/ci.yml` — pipeline de integração contínua.

## Funcionalidades
- Criação de tarefas com título, descrição e prioridade.
- Listagem de tarefas em interface web.
- Atualização de status das tarefas.
- Exclusão de tarefas.
- Consulta de tarefas por prioridade.

## Pipeline de CI
O GitHub Actions configura um fluxo de CI que:
- instala dependências
- executa `pytest`
- valida o código com `flake8`

## Mudança de Escopo
O escopo foi atualizado durante o projeto para incluir uma interface web em Flask no lugar de uma aplicação apenas por terminal. Essa mudança foi necessária para cumprir o requisito de sistema web básico e melhorar a usabilidade.

## Documentação Teórica
A documentação teórica está disponível em `docs/parte_teorica.md` e em documento Word `docs/parte_teorica.docx`.

## Observações
A pasta `docs/` também deve incluir capturas e comentários sobre o fluxo de trabalho GitHub, o quadro Kanban e a execução da pipeline de CI.
#