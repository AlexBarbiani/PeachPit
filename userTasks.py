#import datetime
import uuid
import re

class UserTask:
    def __init__(self, ID, name, notes = None, tags = None, due_date = None):
        self.ID = ID
        self.name = name
        self.notes = notes
        self.tags = tags
        self.due_date = due_date
    
    def __str__(self):
        return f" Task ID: {self.ID} \n Task Name: {self.name} \n Task Notes: {self.notes} \n Task Tags: {self.tags} \n Task Due Date: {self.due_date} \n"
    

def create_user_task(user_task_name):
    global new_task
    taskID = uuid.uuid1()
    new_task = UserTask(ID = taskID, name = user_task_name)
    return new_task

def edit_user_task():
    incoming_name = input("Please input the task's new name. If you do not want to make any changes, press Enter:")
    if incoming_name != "":
       new_task.name = incoming_name

    incoming_notes = input("Please input the task's new notes. If you do not want to make any changes, press Enter:")
    if incoming_notes != "":
        new_task.notes = incoming_notes

    initial_tags = input("Please input the task's new tags, with each tag separated by a single space. If you do not want to make any changes, press Enter:")
    incoming_tags = re.split("\s", initial_tags)
    incoming_tags = set(incoming_tags)
    if incoming_notes != "":
        new_task.tags = incoming_tags
        
    print(new_task)

def delete_user_task(new_task):
    del new_task