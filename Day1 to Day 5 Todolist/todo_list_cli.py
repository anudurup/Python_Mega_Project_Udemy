todos = list()
while True:
    user_action = input("Type add,show or exit: ").strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break
        case _: # _ is the unknown variable.
            print("Hey, you entered an unknown command.")


print('Bye!')