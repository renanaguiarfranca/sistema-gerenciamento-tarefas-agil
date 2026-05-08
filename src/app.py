from flask import Flask, jsonify, redirect, render_template, request, url_for, abort

from src.a import TaskManager

app = Flask(__name__)
manager = TaskManager()

PRIORITY_ORDER = {'Alta': 1, 'Média': 2, 'Baixa': 3}


def task_to_dict(task):
    return {
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'priority': task.priority,
        'status': task.status,
    }


@app.route('/')
def index():
    tasks = manager.read_tasks()
    return render_template('index.html', tasks=tasks)


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify([task_to_dict(task) for task in manager.read_tasks()])


@app.route('/tasks/priority', methods=['GET'])
def get_tasks_by_priority():
    tasks = manager.list_by_priority()
    return jsonify([task_to_dict(task) for task in tasks])


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.form or request.get_json() or {}
    title = data.get('title', '').strip()
    description = data.get('description', '').strip()
    priority = data.get('priority', 'Média').strip()

    if not title or not description:
        abort(400, 'Título e descrição são obrigatórios.')

    task = manager.create_task(title, description, priority)
    if request.is_json:
        return jsonify(task_to_dict(task)), 201
    return redirect(url_for('index'))


@app.route('/tasks/<int:task_id>', methods=['PUT', 'PATCH'])
def update_task(task_id):
    data = request.get_json() or {}
    status = data.get('status')
    if status is None:
        abort(400, 'Status é obrigatório.')

    updated = manager.update_task(task_id, status=status)
    if not updated:
        abort(404, 'Tarefa não encontrada.')
    return jsonify(task_to_dict(updated))


@app.route('/tasks/<int:task_id>/update', methods=['POST'])
def update_task_form(task_id):
    status = request.form.get('status')
    if not status:
        abort(400, 'Status é obrigatório.')
    updated = manager.update_task(task_id, status=status)
    if not updated:
        abort(404, 'Tarefa não encontrada.')
    return redirect(url_for('index'))


@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task_form(task_id):
    removed = manager.delete_task(task_id)
    if not removed:
        abort(404, 'Tarefa não encontrada.')
    return redirect(url_for('index'))


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    removed = manager.delete_task(task_id)
    if not removed:
        abort(404, 'Tarefa não encontrada.')
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
