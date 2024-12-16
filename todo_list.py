import json
from datetime import datetime

tasks = []

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    print("\n" + "=" * 40)
    description = input("Enter task description: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD or leave blank): ").strip()
    tasks.append({
        "description": description,
        "completed": False,
        "due_date": due_date if due_date else "No due date"
    })
    print(f"\n✅ Task '{description}' added successfully!\n" + "=" * 40)

def display_tasks():
    print("\n" + "=" * 40)
    if not tasks:
        print("📂 No tasks available.\n")
    else:
        print("{:<5} {:<40} {:<12} {:<15}".format("ID", "Description", "Status", "Due Date"))
        print("-" * 75)
        for i, task in enumerate(tasks):
            status = "✅ Complete" if task["completed"] else "❌ Incomplete"
            print(f"{i:<5} {task['description']:<40} {status:<12} {task['due_date']:<15}")
    print("=" * 40 + "\n")

def mark_task_complete():
    display_tasks()
    try:
        task_id = int(input("Enter the task ID to mark as complete: "))
        if 0 <= task_id < len(tasks):
            tasks[task_id]["completed"] = True
            print(f"\n✅ Task '{tasks[task_id]['description']}' marked as complete!\n" + "=" * 40)
        else:
            print("⚠️ Invalid task ID.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

def edit_task():
    display_tasks()
    try:
        task_id = int(input("Enter the task ID to edit: "))
        if 0 <= task_id < len(tasks):
            new_description = input("Enter new task description: ").strip()
            new_due_date = input("Enter new due date (YYYY-MM-DD or leave blank): ").strip()
            tasks[task_id]["description"] = new_description
            tasks[task_id]["due_date"] = new_due_date if new_due_date else "No due date"
            print(f"\n✏️ Task '{new_description}' updated successfully!\n" + "=" * 40)
        else:
            print("⚠️ Invalid task ID.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

def delete_task():
    display_tasks()
    try:
        task_id = int(input("Enter the task ID to delete: "))
        if 0 <= task_id < len(tasks):
            deleted_task = tasks.pop(task_id)
            print(f"\n🗑️ Task '{deleted_task['description']}' deleted successfully!\n" + "=" * 40)
        else:
            print("⚠️ Invalid task ID.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

def main():
    load_tasks()
    while True:
        print("\n" + "=" * 40)
        print("📋 Task Manager".center(40))
        print("=" * 40)
        print("1. ➕ Add Task")
        print("2. 📄 View Tasks")
        print("3. ✅ Mark Task as Complete")
        print("4. ✏️ Edit Task")
        print("5. 🗑️ Delete Task")
        print("6. 💾 Save and Exit")
        print("=" * 40)

        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            edit_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            save_tasks()
            print("\n💾 Tasks saved. Goodbye!")
            break
        else:
            print("\n⚠️ Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
