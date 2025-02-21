
import random

class userTask:
    def __init__(self, ID, name, notes = None, tags = None, dueDate = None):
        self.ID = ID
        self.name = name
        self.notes = notes
        self.tags = tags
        self.dueDate = dueDate
    
    def __str__(self):
        return f" Task ID: {self.ID} \n Task Name: {self.name} \n Task Notes: {self.notes} \n Task Tags: {self.tags} \n Task Due Date: {self.dueDate}"

def createUserTask(userTaskName):
    global newTask
    taskID = random.randint(1, 65365)
    'todo - if an id exists, reroll until it does not {possibly implement as a +1 to the database}'
    taskID = str(taskID)
    newTask = userTask(ID = taskID, name = userTaskName)
    return newTask
