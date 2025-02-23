import json
import os
from models_v2 import ToDo

filename = 'todo.json'
if not os.path.isfile(filename):
    with open(filename, 'w') as f:
        json.dump([], f)

if __name__ == '__main__':
    with open(filename, 'r') as f:
        start_json = json.load(f)

    todo_now = ToDo(start_json)
    todo_now.add_todo("Покорми кота", "20.02.2025 вечер")

    todo_now.delete_todo("Покорми кота")

    with open(filename, 'w') as f:
        json.dump(start_json, f)
