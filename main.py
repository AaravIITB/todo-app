#from function import get_todo,write_todo
#importing elements from another file. Condition both the file main and function are in the same directory.
import function
import time

now = time.strftime("%b %d,%Y %H:%M:%S")
print("It is "+now)
while True:
    action=input("type add, show, edit, complete or exit:")
    action =action.strip()

    if action.startswith("add"):
        todo=action[4:]+'\n'
        #Using With context manager the file is automatically closed
        todos= function.get_todo()

        todos.append(todo)

        function.write_todo(todos)

    elif action.startswith("show"):
        todos= function.get_todo()

        for index,item in enumerate(todos):
            item=item.strip('\n')
            print(index+1,"-",item)
        #2nd method
        # new_todos = []
        # for item in todos:
        #     new_item=item.strip('\n')
        #     new_todos.append(new_item)
        # for index,item in enumerate(new_todos):
        #     print(index+1,"-",item)
        #3rd method
        # new_todos=[item.strip('\n') for item in todos]
        # for index, item in enumerate(new_todos):
        #     print(index+1,"-",item)
    elif action.startswith("edit"):
        try:
            todos= function.get_todo()

            number =int((action[5:]))

            todo=input("Enter the task:")+'\n'
            todos[number-1]=todo

            function.write_todo(todos)

        except ValueError:
            print("Your command is not valid.")
            continue
    elif action.startswith("complete"):
        try:
            todos= function.get_todo()

            number = int(action[9:])
            todo_to_remove=todos[number-1]
            todos.pop(number-1)

            function.write_todo(todos)

            print(f"{todo_to_remove.strip('\n')} is removed from the list")

        except IndexError:
            print("Invalid input")
            continue
    elif action.startswith("exit"):
        break
    else:
        print("Invalid input")
print("Bye")