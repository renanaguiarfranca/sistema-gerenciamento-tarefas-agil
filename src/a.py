class Task:
    """Classe que representa uma tarefa no sistema."""
    def __init__(self, id, title, description, priority, status='A Fazer'):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority  # Alta, Média, Baixa
        self.status = status  # A Fazer, Em Progresso, Concluído

class TaskManager:
    """Gerenciador de tarefas com operações CRUD."""
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, title, description, priority):
        task = Task(self.next_id, title, description, priority)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def read_tasks(self):
        return self.tasks

    def update_task(self, id, **kwargs):
        for task in self.tasks:
            if task.id == id:
                for key, value in kwargs.items():
                    setattr(task, key, value)
                return task
        return None

    def list_by_priority(self):
        priority_order = {'Alta': 1, 'Média': 2, 'Baixa': 3}
        return sorted(self.tasks, key=lambda t: priority_order.get(t.priority, 4))

    def delete_task(self, id):
        for i, task in enumerate(self.tasks):
            if task.id == id:
                return self.tasks.pop(i)
        return None

# CLI simples
def main():
    manager = TaskManager()
    while True:
        print("\n1. Criar Tarefa")
        print("2. Listar Tarefas")
        print("3. Listar por Prioridade")
        print("4. Atualizar Tarefa")
        print("5. Deletar Tarefa")
        print("6. Sair")
        choice = input("Escolha: ")
        if choice == '1':
            title = input("Título: ")
            desc = input("Descrição: ")
            prio = input("Prioridade (Alta/Média/Baixa): ")
            manager.create_task(title, desc, prio)
            print("Tarefa criada.")
        elif choice == '2':
            for task in manager.read_tasks():
                print(f"ID: {task.id}, Título: {task.title}, Status: {task.status}")
        elif choice == '3':
            for task in manager.list_by_priority():
                print(f"ID: {task.id}, Título: {task.title}, Prioridade: {task.priority}")
        elif choice == '4':
            id = int(input("ID da tarefa: "))
            status = input("Novo status (A Fazer/Em Progresso/Concluído): ")
            manager.update_task(id, status=status)
            print("Tarefa atualizada.")
        elif choice == '5':
            id = int(input("ID da tarefa: "))
            manager.delete_task(id)
            print("Tarefa deletada.")
        elif choice == '6':
            break

if __name__ == "__main__":
    main()