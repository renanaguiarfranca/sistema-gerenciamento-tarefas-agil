# Parte Teórica: Construindo um Projeto Ágil no GitHub

## Descrição do Projeto e Escopo Inicial
O projeto consiste em um sistema de gerenciamento de tarefas baseado em metodologias ágeis, desenvolvido para uma startup de logística fictícia. O escopo inicial inclui funcionalidades básicas de CRUD para tarefas, acompanhamento de status e priorização simples.

## Metodologia Ágil Utilizada
Adotamos o Kanban como metodologia ágil, utilizando um quadro com colunas "A Fazer", "Em Progresso" e "Concluído" para gerenciar o fluxo de trabalho.

## Importância da Modelagem na Engenharia de Software
A modelagem permite representar o sistema de forma abstrata, facilitando a comunicação entre stakeholders e a identificação de requisitos.

## Diagramas UML

### Diagrama de Casos de Uso
- Ator: Usuário
- Casos: Criar Tarefa, Listar Tarefas, Atualizar Tarefa, Deletar Tarefa

### Diagrama de Classes
- Classe Task: id, title, description, priority, status
- Classe TaskManager: métodos CRUD

## Breve Justificativa sobre a Mudança de Escopo
Adicionamos a funcionalidade de listagem por prioridade para melhor atender às necessidades de priorização crítica do cliente, demonstrando a adaptabilidade ágil.

## Explicação sobre os Testes Automatizados
Utilizamos Pytest para testes unitários, garantindo que cada funcionalidade opere corretamente e prevenindo regressões.

## Prints Comentados
- Kanban: Quadro com tarefas organizadas.
- Commits: Histórico de commits descritivos.
- Workflow CI: Execução automática de testes no GitHub Actions.