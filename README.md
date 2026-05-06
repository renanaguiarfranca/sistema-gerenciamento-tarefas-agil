# Sistema de Gerenciamento de Tarefas Ágil

## Objetivo do Projeto
Desenvolver um sistema de gerenciamento de tarefas baseado em metodologias ágeis para uma startup de logística. O sistema permite acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe.

## Escopo
- Funcionalidades básicas: CRUD para tarefas (Criar, Ler, Atualizar, Deletar).
- Interface simples via terminal (para simplicidade).
- Controle de qualidade com testes automatizados.
- Gestão ágil usando Kanban no GitHub Projects.

## Metodologia Adotada
Utilizamos a metodologia Kanban para gestão de tarefas, com um quadro dividido em colunas: A Fazer, Em Progresso e Concluído. O desenvolvimento segue princípios ágeis, com iterações curtas e foco na entrega incremental.

## Como Executar
1. Instale Python 3.x.
2. Execute `python a.py` para iniciar o sistema.
3. Siga as instruções no terminal para gerenciar tarefas.

## Mudanças no Escopo
Inicialmente, o escopo era apenas CRUD básico. Posteriormente, adicionamos uma funcionalidade de priorização de tarefas para atender melhor às necessidades do cliente, simulando uma mudança ágil.

## Testes Automatizados
Utilizamos Pytest para testes unitários. Execute `pytest` na raiz do projeto.

## CI/CD
Configurado com GitHub Actions para executar testes automaticamente em cada push.