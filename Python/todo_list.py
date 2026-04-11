import json
import os

TASKS_FILE = 'daily_todo.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f)

def main():
    tasks = load_tasks()
    while True:
        print("\n===== Daily To-Do List =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Done")
        print("4. Remove Task")
        print("5. Exit")
        choice = input("Choice: ")
        
        if choice == '1':
            n=int(input("How many task you add: "))
            for i in range(n):
             task = input("Task: ")
             tasks.append({"task": task, "done": False})
             save_tasks(tasks)
             print(f"{task} Added!")
        elif choice == '2':
            if not tasks:
                print("No tasks.")
            for i, t in enumerate(tasks, 1):
                status = "Done" if t["done"] else "Not Done"
                print(f"{i}. {t['task']} - {status}")
        elif choice == '3':
            try:
                num = int(input("Task number: ")) - 1
                if 0 <= num < len(tasks):
                    tasks[num]["done"] = True
                    save_tasks(tasks)
                    print("Marked done!")
                else:
                    print("Invalid number.")
            except:
                print("Invalid input.")
        elif choice == '4':
            try:
                n=int(input("How many task you can remove: "))
                for i in range(n):
                 num = int(input("Task number: ")) - 1
                 if 0 <= num < len(tasks):
                    del tasks[num]
                    save_tasks(tasks)
                    print("Removed!")
                 else:
                    print("Invalid number.")
            except:
                print("Invalid input.")
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()