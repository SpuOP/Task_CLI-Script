import argparse
import sys
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_task(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("task", type=str, nargs="?", help="Task to Add")
    parser.add_argument("--list", action="store_true", help="List all tasks")
    parser.add_argument("--complete", type=int, help="Mark task as complete")
    parser.add_argument("--delete", type=int, help="Delete task by ID")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.list:
        tasks = load_tasks()
        for task in tasks:
            status = "x" if task["done"] else " "
            print(f"[{status}] {task['id']}: {task['task']}")
        sys.exit(0)

    elif args.complete:
        tasks = load_tasks()
        for task in tasks:
            if task["id"] == args.complete:
                task["done"] = True
                save_task(tasks)
                print(f"Task with ID {args.complete} marked as complete.")
                break

    elif args.delete:
        tasks = load_tasks()
        new_tasks = []
        for task in tasks:
            if task["id"] != args.delete:
                new_tasks.append(task)
        save_task(new_tasks)
        print(f"Task with ID {args.delete} deleted.")

    elif args.task:
        tasks = load_tasks()
        if len(tasks) == 0:
            new_id = 1
        else:
            new_id = tasks[-1]["id"] + 1

        tasks.append({"id": new_id, "task": args.task, "done": False})
        save_task(tasks)
        print(f"Task added: {args.task} added with ID of {new_id}")

if __name__ == "__main__":
    main()