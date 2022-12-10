todos = list()
while True:
    user_action = input("Type add,show, edit or exit: ").strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for i,item in enumerate(todos):
                row = f'{i+1} - {item}'
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number -= 1
            new_todo = input("Enter new todo")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to edit: "))
            number -= 1
            todos.pop(number)
        case 'exit':
            break
        case _: # _ is the unknown variable.
            print("Hey, you entered an unknown command.")


print('Bye!')