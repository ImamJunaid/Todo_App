FILEPATH = "todos_items.txt"


def get_todos(filepath = "todos.txt"):
    """ Read the text file and return the list
    of to-do items
    """
    with open(filepath, 'r') as file_local:
        """ Write the to-do items list and return in file"""
        todos_local = file_local.readlines()

    return todos_local

def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath,'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())