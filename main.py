'''When to Use Which?
• Snake Case: Use for variables, functions, and module names 
(preferred in Python).
• Pascal Case Use for class names'''

import userTasks as task
import userCharacter as char

test_character = char.UserCharacter()

test_task = input("Hello! Please enter your task name:")
task.create_user_task(test_task)

print(test_character)
print(task.new_task)
task.edit_user_task()