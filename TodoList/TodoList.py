from termcolor import colored

# Reading the tasks
def read_tasks():
    try:
        with open("tasks.txt", 'r') as f:
            tasks = f.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []
# Adding new tasks
def write_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + '\n')

# Displaying/viewing the tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nThe tasks are:\n")
        for idx, task in enumerate(tasks, start=1):
            print(colored(f"{idx}.{task}", 'blue'))
# Adding new tasks
def add_task(tasks, new_task):
    tasks.append(new_task)
    write_tasks(tasks)
    print("Task added successfully!")
# Completing the particular tasks
def complete_tasks(tasks, task_index):
    try:
        task_index = int(task_index)
        if 1 <= task_index <= len(tasks):
            del tasks[task_index - 1]
            write_tasks(tasks)
            print("Task completed successfully!")
        else:
            print("Invalid index!")
    except ValueError:
        print("Invalid index!")
# Displaying the choice menu
def display_menu():
    print("\nTodo List\n")
    print("1.View task")
    print("2.Add task")
    print("3.Complete task")
    print("4.Exit")
# Main function
def main():
    tasks = read_tasks()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == '3':
            task_index = input("Enter the task index to be marked completed: ")
            complete_tasks(tasks, task_index)
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()