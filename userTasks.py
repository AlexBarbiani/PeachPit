
import random

class userTask:
    def __init__(task, ID, name, notes = None, tags = None, dueDate = None):
        task.ID = ID
        task.name = name
        task.notes = notes
        task.tags = tags
        task.dueDate = dueDate
    
    def __str__(task):
        return f" Task ID: {task.ID} \n Task Name: {task.name} \n Task Notes: {task.notes} \n Task Tags: {task.tags} \n Task Due Date: {task.dueDate}"

def createUserTask(userTaskName):
    global newTask
    taskID = random.randint(1, 65365)
    'todo - if an id exists, reroll until it does not {possibly implement as a +1 to the database}'
    taskID = str(taskID)
    newTask = userTask(ID = taskID, name = userTaskName)
    return newTask
