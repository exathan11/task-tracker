import argparse, json
from .parser_actions import add_task, update_task, mark_in_progress, mark_done, delete_task, list_tasks
from .TaskModel import Task

def load_tasks() -> dict[str, list[Task]]:
    with open("tasks.json") as f:
        tasks = json.load(f)
    
    return tasks

def load_parsers(tasks: dict[str, list[Task]]) -> None:
    parser = argparse.ArgumentParser(prog="task-cli", description="A CLI task manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_task_parser = subparsers.add_parser("add", help="Add a new task")
    add_task_parser.add_argument("name", help="The task name")
    add_task_parser.set_defaults(func=add_task)

    update_task_parser = subparsers.add_parser("update", help="Update an existing task")
    update_task_parser.add_argument("id", type=int, help="The task id")
    update_task_parser.add_argument("name", help="The task name")
    update_task_parser.set_defaults(func=update_task)

    mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Mark an existing task in progress")
    mark_in_progress_parser.add_argument("id", type=int, help="The task id")
    mark_in_progress_parser.set_defaults(func=mark_in_progress)

    mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
    mark_done_parser.add_argument("id", type=int, help="The task id")
    mark_done_parser.set_defaults(func=mark_done)

    delete_task_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_task_parser.add_argument("id", type=int, help="The task id")
    delete_task_parser.set_defaults(func=delete_task)

    list_tasks_parser = subparsers.add_parser("list", help="List tasks")
    list_tasks_parser.add_argument("command", nargs="?", help="List command", choices=["todo", "done", "in-progress"])
    list_tasks_parser.set_defaults(func=list_tasks)

    args = parser.parse_args()
    try:
        args.func(args, tasks)
    except ValueError as e:
        print(e)

class Person:
    name: str

def main() -> None:
    tasks = load_tasks()
    load_parsers(tasks)



if __name__ == "__main__":
    main()