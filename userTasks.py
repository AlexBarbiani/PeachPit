# this module houses classes/functions related to user-created tasks

#import datetime
import uuid
import json
import os
import userCharacter as char

#Initializing

class UserTask:
    def __init__(self, ID:uuid, name:str, notes:str | None = None, tags:set | None = None, due_date = None):
        self.ID = ID
        self.name = name
        self.notes = notes
        self.tags = tags
        self.due_date = due_date

    def to_dict(self):
        return {
            "ID": str(self.ID),
            "name": self.name,
            "notes": self.notes,
            "tags": self.tags,
            "due_date": self.due_date,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            ID=uuid.UUID(
                data["ID"]
            ),  # badly formed hexadecimal UUID string - figure out how to ignore this because i don't care
            name=data["name"],
            notes=data.get("notes"),
            tags=data.get("tags"),
            due_date=data.get("due_date"),
        )

    def __str__(self):
        return f" Task ID: {self.ID} \n Task Name: {self.name} \n Task Notes: {self.notes} \n Task Tags: {self.tags} \n Task Due Date: {self.due_date} \n"


# JSON file interaction
task_filename = "tasks.json"
completed_tasks_filename ="completed_tasks.json"

def initialize_task_list():
    global task_list
    task_list = load_user_tasks()
    if task_list is None:
        default_tasks = UserTask(
                "74a5b43d-0ae3-4ddc-af20-9b7c5c46e792",
                "Pick up Nintendo Switch from repair shop",
                "No more Joy-con drift!",
        )
        save_user_tasks(default_tasks)
        default_tasks = UserTask("41fd9a7b-b5fe-4144-8f2a-8343b1541d7c",
                "Buy groceries",
                "Buy lettuce, almonds, cranberries, cucumbers, and a vinaigrette for the salad.",
        )
        save_user_tasks(default_tasks)
        
        default_tasks = UserTask("cded018c-26e3-45f3-8579-6182c551e63c",
                "Win Worlds",
                "Faker! What was that?!",
        )
        save_user_tasks(default_tasks)
        task_list = load_user_tasks()


def load_user_tasks(filename=task_filename):
    if not os.path.exists(filename):
        return None
    with open(filename, "r") as file:
        tasks_data = json.load(file)
        return [UserTask.from_dict(task_data) for task_data in tasks_data]
    file.close()


def save_user_tasks(tasks, filename=task_filename):
    with open(filename, "w") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)
    file.close()


def save_completed_user_tasks(task, filename=completed_tasks_filename):
    try:
        try:
            with open(filename, "r") as file:
                completed_tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            completed_tasks = []

        completed_tasks.append(task.to_dict())

        with open(filename, "w") as file:
            json.dump(completed_tasks, file, indent=4)
        file.close()

    except Exception as e:
        print(f"An error occurred while saving completed tasks: {e}")
    file.close()

def print_user_tasks():
    task_list = load_user_tasks()
    for tasks in task_list:
        print (tasks)

def query_add_user_tasks():
    incoming_name = input("Please input the name of your new task. If you don't want to create a task, press Enter.").strip()
    if incoming_name != "":
        add_user_tasks(incoming_name)
    else:
        print("Cancelled task creation.")

def add_user_tasks(incoming_name, filename=task_filename):

    task_id = uuid.uuid1()
    new_user_task = UserTask(ID=task_id, name=incoming_name)
    task_list.append(new_user_task)
    save_user_tasks(task_list, filename)
    print(f"New task {incoming_name} has been created!")
    print_user_tasks()

def query_edit_user_tasks():
    incoming_ID = input("Please input the ID of the task you wish to edit; I recommend copy/pasting. If you don't want to edit a task, press Enter.").strip()
    if incoming_ID != "":
        edit_user_tasks(incoming_ID)
    else:
        print("Cancelled task editing.")

def edit_user_tasks(incoming_ID): # current job 
    try:
        task_to_edit = None
        for task in task_list:
            if str(task.ID) == incoming_ID:
                task_to_edit = task
                break
        
        if task_to_edit:
            incoming_name = input(
            "Please input the task's new name. If you do not want to make any changes, press Enter:"
            )
            if incoming_name:
                task_to_edit.name = incoming_name
            
            incoming_notes = input(
            "Please input the task's new notes. If you do not want to make any changes, press Enter:"
                    )
            if incoming_notes:
                task_to_edit.notes = incoming_notes

            incoming_tags = input(
            "Please input the task's new tags, with each tag separated by a single space. If you do not want to make any changes, press Enter:"
                    )
            if incoming_tags:
                task_to_edit.tags = list(set(incoming_tags.split()))
        
            save_user_tasks(task_list)
            print_user_tasks()
        
        else:
            print(f"I couldn't find a task with the ID {incoming_ID}. Are you sure it's correct?")
            query_edit_user_tasks()
    
    except Exception as e:
        print(f"An error occurred: {e}")   

# the difference between completion and deletion is that completion awards exp and archives the task, but deletion simply removes it

def query_complete_user_tasks():
    incoming_ID = input("Please input the ID of the task you wish to complete; I recommend copy/pasting. If you don't want to complete a task, press Enter.").strip()
    if incoming_ID != "":
        complete_user_tasks(incoming_ID)
    else:
        print("Cancelled task completion.")


def complete_user_tasks(incoming_ID):
    exp = 8
    try:
        task_to_complete = None
        for task in task_list:
            if str(task.ID) == incoming_ID:
                task_to_complete = task
                break
        
        if task_to_complete:
            save_completed_user_tasks(task_to_complete)
            task_list.remove(task_to_complete)
            save_user_tasks(task_list)
            char.UserCharacter.add_exp(char.character, exp)
            print(f"Task with the ID {incoming_ID} has been completed. You gained {exp} exp!")

        else:
            print(f"I couldn't find a task with the ID {incoming_ID}. Are you sure it's correct?")
            query_complete_user_tasks()
    except Exception as e:
        print(f"An error occurred: {e}")

    print_user_tasks

def query_delete_user_tasks():
    incoming_ID = input("Please input the ID of the task you wish to delete; I recommend copy/pasting. If you don't want to delete a task, press Enter.").strip()
    if incoming_ID != "":
        delete_user_tasks(incoming_ID)
    else:
        print("Cancelled task deletion.")


def delete_user_tasks(incoming_ID):
    try:
        task_to_delete = None
        for task in task_list:
            if str(task.ID) == incoming_ID:
                task_to_delete = task
                break
        
        if task_to_delete:
            task_list.remove(task_to_delete)
            save_user_tasks(task_list) 
            print(f"Task with the ID {incoming_ID} has been deleted.")
        else:
            print(f"I couldn't find a task with the ID {incoming_ID}. Are you sure it's correct?")
            query_delete_user_tasks()
    except Exception as e:
        print(f"An error occurred: {e}")

    print_user_tasks

#This is used only for the initialization to show a user what they can do with their tasks

def custom_user_task(task_id, task_name, task_notes):
    new_user_task = UserTask(ID=task_id, name=task_name, notes=task_notes)
    return new_user_task
