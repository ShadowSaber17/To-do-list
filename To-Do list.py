print("To-Do List: ")
enter_task = ""
view_task = ""
task_1 = ""
quit = ""
task = ""
list = ["""
Add task
View task
Quit"""]
intro = print("What do you want to do? ")
print(*list, sep=",")
command = input("> ")
command.upper()
while command == "e":
    if task != 'done':
        task_1 = [item for item in input("Enter your tasks: ").split()]
        print(*task_1, sep="\n")
    break
intro = print("What do you want to do? ")
command = input("> ")
if command == 'q':
    print('Thank you for using our app! ')
elif command == 'v':
    print(*task_1, sep="\n")




