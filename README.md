# Task Tracker

## About
Task Tracker is a CLI app used to assist your productivity by tracking your tasks.

## Instructions

```bash
git clone https://github.com/exathan11/task-cli.git
cd task-cli
```

### Try it locally

Requires: `uv`

```bash
uv run task-cli
```

### Install as a CLI command

```bash
uv tool install .
task-cli
```

## Usage

```bash
task-cli add "Buy milk"
// Task added successfully (task ID: 1)

task-cli update 1 "Buy milk and eggs"
// Task updated successfully (task ID: 1)

task-cli delete 1

task-cli mark-in-progress 1
task-cli mark-done 1

task-cli list
task-cli list done
task-cli list todo
task-cli list in-progress
```