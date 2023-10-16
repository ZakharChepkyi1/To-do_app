import functions
import time

now = time.strftime("%b %d,%Y %H:%M:%S")
print('It is', now)

while True:
    user_action = input('do you want to add,show,edit,complete or exit:')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todo()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todo()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index + 1}-{item}'
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            number = number - 1

            todos = functions.get_todo()

            new_todos = input("Enter the new Todo:")
            todos[number] = new_todos + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("Your command is invalid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[8:])

            todos = functions.get_todo()
            index = number - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f'Todo {todos_to_remove} was removed from the list'
            print(message)
        except IndexError:
            print('OUT of range')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid')

print('Bye')
