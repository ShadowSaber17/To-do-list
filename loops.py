print("To-Do List: ")
enter_task = ""
view_task = ""
task_complete = ""
quit = ""
task = ""
list = ["""
Add task
View task
Mark completed
Quit"""]
print("What do you want to do? ")
print(*list, sep=",")
command = input("> ")
command.upper()
if command == "q":
    print('Thank You for using our app!')
while command == "e":
    task = input('Enter your tasks: ').split()
    print(task)
    command = input('Enter "q" if you are done else "e" if you want to enter more')
