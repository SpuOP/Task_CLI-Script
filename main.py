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
    print("Saving to file...")
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

parser = argparse.ArgumentParser()
parser.add_argument("task", type=str, nargs="?", help="Task to Add")
args = parser.parse_args()

print("args.task =", args.task)

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

if args.task:
    print("Inside args.task block")
    tasks = load_tasks()
    print("Loaded tasks:", tasks)

    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = tasks[-1]["id"] + 1

    tasks.append({"id": new_id, "task": args.task, "done": False})
    save_task(tasks)

    print(f"Task added: {args.task} added with ID of {new_id}")