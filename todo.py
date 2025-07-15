#todo-list

def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("\n📂 Your task list is empty.\n")
                return
            print("\n📝 Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("\n❌ No task file found. Start by adding tasks.\n")

def add_task():
    task = input("➕ Enter a new task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("✅ Task added!\n")

def delete_task():
    show_tasks()
    try:
        index = int(input("❌ Enter task number to delete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= index <= len(tasks):
            deleted = tasks.pop(index - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"🗑️ Deleted: {deleted.strip()}\n")
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")
    except FileNotFoundError:
        print("❌ No tasks to delete.\n")

def menu():
    while True:
        print("\n========= 📋 TO-DO LIST MENU =========")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("👋 Exiting. Have a productive day!")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")

# Start the app
menu()
