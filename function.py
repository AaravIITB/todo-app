def get_todo(filepath="todos.txt"):
    """ Read the text file and 
    return the list of to-do items """#DocString
    with open(filepath, 'r') as file_local:
        todo_local = file_local.readlines()
    return todo_local

def write_todo(todos_local,filepath="todos.txt"):
    """ Write the to-do items list
    in text files."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)