print("To-Do List: ")
enter_task = ""
view_task = ""
task_complete = ""
quit = ""
task = ""
task_1 = []
list = ["""
Add task
View task
Mark completed
Quit"""]
print("What do you want to do? ")
print(*list, sep=",")
command = input("> ")
command.upper()
while command == "e":
    if task == 'done':
        print('These are all your tasks.')
        break
    else:
        task_1 = [item for item in input("Enter your tasks: ").split()]
        print(*task_1, sep="\n")



