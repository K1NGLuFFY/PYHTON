# Simple Task Manager

tasks = []

def add_task():
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    print("Task added.")

def update_task():
    see_tasks()
    idx = int(input("Enter task number to update: ")) - 1
    if 0 <= idx < len(tasks):
        new_title = input("Enter new title: ")
        tasks[idx]["title"] = new_title
        print("Task updated.")
    else:
        print("Invalid task number.")

def see_tasks():
    if not tasks:
        print("No tasks.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['title']}")

def check_task_complete():
    see_tasks()
    idx = int(input("Enter task number to mark complete: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]["completed"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n1. Add Task\n2. Update Task\n3. See Tasks\n4. Check Task Complete\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            update_task()
        elif choice == "3":
            see_tasks()
        elif choice == "4":
            check_task_complete()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()