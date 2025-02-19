import userTasks
import userCharacter

testCharacter = userCharacter.userCharacter()

userTaskName = input("Hello! Please enter your task name:")
userTasks.createUserTask(userTaskName)

print(testCharacter)
print(userTasks.newTask)