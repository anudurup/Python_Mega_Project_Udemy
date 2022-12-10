while True:
    user_action = input("Type add,show, edit or exit: ").strip()
    if user_action.startswith('add'):
        todo = input("Enter a todo: ") + "\n"
        # with helps with not needing to open and close the file.
        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)
        with open('todo.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        with open('todo.txt', 'r') as file:
            todos = file.readlines()
        new_todos = [item.strip('\n') for item in todos]

        for i,item in enumerate(new_todos):
            row = f'{i+1} - {item}'
            print(row)

    elif user_action.startswith('edit'):
        number = int(input("Number of the todo to edit: "))
        number -= 1
        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo")
        todos[number] = new_todo + "\n"
        with open('todo.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('complete'):
        number = int(input("Number of the todo to edit: "))
        number -= 1
        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        todos.pop(number)
        with open('todo.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('exit'):
        break
print('Bye!')