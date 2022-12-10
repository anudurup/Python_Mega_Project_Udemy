def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_local):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)


while True:
    user_action = input("Type add,show, edit or exit: ").strip()
    if user_action.startswith('add'):
        todo = user_action[4:]
        # with helps with not needing to open and close the file.
        todos = get_todos('todo.txt')
        todos.append(todo + "\n")
        write_todos('todo.txt', todos)

    elif user_action.startswith('show'):
        todos = get_todos('todo.txt') 
        new_todos = [item.strip('\n') for item in todos]

        for i, item in enumerate(new_todos):
            row = f'{i + 1} - {item}'
            print(row)

    elif user_action.startswith('edit'):
        number = int(input("Number of the todo to edit: "))
        number -= 1
        todos = get_todos('todo.txt')

        new_todo = user_action[4:]
        todos[number] = new_todo + "\n"
        write_todos('todo.txt', todos)

    elif user_action.startswith('complete'):
        number = int(input("Number of the todo to edit: "))
        number -= 1
        todos = get_todos('todo.txt')

        todos.pop(number)
        write_todos('todo.txt', todos)

    elif user_action.startswith('exit'):
        break
print('Bye!')
