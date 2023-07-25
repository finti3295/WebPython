FILEPATH = "todos.txt"


def get_todos(fpath=FILEPATH):
    with open(fpath, "r") as file1:
        todos1 = file1.readlines()
    return todos1


def write_todos(todos1, fpath=FILEPATH):
    with open(fpath, "w") as file1:
        file1.writelines(todos1)


def count(phrase):
    return phrase.count('.')
