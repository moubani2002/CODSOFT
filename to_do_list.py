#codsoft task - 1:
#To Do List

tasks = []

def add_tasks():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"'{task}' is added to the list successfully...")

def task_list():
    if not tasks:
        print("There are no task for you at present...")
    else:
        print("Your tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task {index}.{task}")
def delete_task():
    task_list()
    try:
        task_to_be_deleted = int(input("Enter the task number to delete: "))
        if 0<= task_to_be_deleted <len(tasks):
            deleted_task = tasks.pop(task_to_be_deleted)
            print(f"Task has been removed...")
        else:
            print(f"Task was not found...")
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    print("Welcome to your To-Do-List app...")
    while True:
        print("Select a number between 1 to 4, where 1: add task, 2: delete task, 3: task list, 4: Exit")

        choice = input("Input your choice: ")

        if choice == "1":
            add_tasks()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            task_list()
        elif choice == "4":
            break
        
        else:
            print("Invaid choice...")
    
    print("Thank you...")
