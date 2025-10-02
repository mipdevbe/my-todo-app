import os

FILEPATH = 'files/todos.txt'

def check_todos_exists(filepath=FILEPATH):
    sub_path = os.path.split(filepath)[0]
    file_path = os.path.join(os.getcwd(), sub_path)

    if not os.path.exists(file_path):
        os.mkdir(file_path)

    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass  # pass means do nothing

def load_todos(filepath=FILEPATH):
    """Read a text file and return the new list of
    to-do items.
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()

    for index, todo in enumerate(todos):
        todos[index] = todo.replace('\n', '')
    return todos


def write_todos(todos, filepath=FILEPATH):
    """Write a list of to-do items to a text file."""
    with open(filepath, 'w') as file:
        for todo in todos:
            file.writelines(todo + "\n")

if __name__ == "__main__":
    print("Hello")
    print(load_todos())