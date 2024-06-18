import os

# Define the file where the to-do list will be stored
TODO_FILE = 'todo.txt'

def display_menu():
    print("\nTo-Do List Application")
    print("1. View to-do list")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

def view_todo_list():
    if not os.path.exists(TODO_FILE):
        print("\nNo tasks in the to-do list.")
        return

    with open(TODO_FILE, 'r') as file:
        tasks = file.readlines()

    if not tasks:
        print("\nNo tasks in the to-do list.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task.strip()}")

def add_task():
    task = input("Enter the task: ")
    with open(TODO_FILE, 'a') as file:
        file.write(task + '\n')
    print("Task added.")

def remove_task():
    view_todo_list()
    if not os.path.exists(TODO_FILE):
        return

    try:
        task_num = int(input("\nEnter the task number to remove: "))
        with open(TODO_FILE, 'r') as file:
            tasks = file.readlines()

        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            with open(TODO_FILE, 'w') as file:
                file.writelines(tasks)
            print("Task removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == '1':
            view_todo_list()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
