import userTasks as task
import userCharacter as char

testCharacter = char.userCharacter()

userTaskName = input("Hello! Please enter your task name:")
task.createUserTask(userTaskName)

print(testCharacter)
print(task.newTask)