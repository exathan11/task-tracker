import argparse, json
from datetime import datetime
from typing import Any
from .TaskModel import Task


DATETIME_FORMATTER = "%d/%m/%Y - %H:%M"

def add_task(args: argparse.Namespace, tasks: Any) -> None:
    if not args.name:
        raise ValueError("task name cannot be empty")
    
    task_id = len(tasks["tasks"]) + 1
    new_task = Task(name=args.name, id=task_id)
    tasks['tasks'].append(new_task.to_dict())
    print(f"Task added successfully (task ID: {task_id})")
    save_to_file(tasks)


def update_task(args: argparse.Namespace, tasks: Any) -> None:
    task_found = False
    if not args.name:
        raise ValueError("task name cannot be empty")
    for task in tasks['tasks']:
        if args.id == task['id']:
            task_found = True
            task['name'] = args.name
            task['updatedAt'] = datetime.now().strftime(DATETIME_FORMATTER)
            break
    
    if task_found:
        print(f"Task updated successfully (task ID: {args.id})")
        save_to_file(tasks)
    else:
        raise ValueError(f"No task was found with id {args.id}")


def mark_in_progress(args: argparse.Namespace, tasks: Any) -> None:
    task_found = False
    for task in tasks['tasks']:
        if task['id'] == args.id:
            if task['status'] == 'in-progress':
                raise ValueError(f"Task with id {args.id} is already marked in progress")
            
            task_found = True
            task['status'] = 'in-progress'
            task['updatedAt'] = datetime.now().strftime(DATETIME_FORMATTER)
            break

    if task_found:
        save_to_file(tasks)
    else:
        raise ValueError(f"No task was found with id {args.id}")


def mark_done(args: argparse.Namespace, tasks: Any) -> None:
    task_found = False
    for task in tasks['tasks']:
        if task['id'] == args.id:
            if task['status'] == 'done':
                raise ValueError(f"Task with id {args.id} is already marked done")

            task_found = True
            task['status'] = 'done'
            task['updatedAt'] = datetime.now().strftime(DATETIME_FORMATTER)
            break

    if task_found:
        save_to_file(tasks)
    else:
        raise ValueError(f"No task was found with id {args.id}")


def delete_task(args: argparse.Namespace, tasks: Any) -> None:
    task_found = False
    tasks_list = tasks['tasks']
    if not tasks_list:
        raise ValueError("there are no tasks to delete")
    for i in range(len(tasks_list)):
         if tasks_list[i]['id'] == args.id:
             task_found = True
             del tasks_list[i]
             break
    
    if task_found:
        save_to_file(tasks)
    else:
        raise ValueError(f"No task was found with id {args.id}")



def list_tasks(args: argparse.Namespace, tasks: Any) -> None:
    if args.command in ['todo', 'in-progress', 'done']:
        for task in tasks['tasks']:
            if task['status'] == args.command:
                print(f"{task['id']}. {task['name']}")
    else:
        for task in tasks['tasks']:
            print(f"{task['id']}. {task['name']}")
            

def save_to_file(tasks: dict[str, list[dict]]):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)
