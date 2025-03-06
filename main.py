import userTasks as task
import userCharacter as char
import randomQuote as quote

"""When to Use Which?
• Snake Case: Use for variables, functions, and module names
(preferred in Python).
• Pascal Case Use for class names"""

'''  try:
    except Exception as e:
        print(f"An error occurred: {e}")'''

def show_command_menu():
 print("\nWelcome to Peach Pit! Please enter the number of the function you want to perform:\n"
        "\n1) Show command menu."
        "\n2) Show character."
        "\n3) Show task list."
        "\n4) Add new task."
        "\n5) Edit a task."
        "\n6) Complete a task."
        "\n7) Delete a task."
        "\n8) Show pomodoro timer (being worked on)."
        "\n9) Share some wisdom."
        "\n0) Exit program.")
    

def main():
    quote.quote_picker()
    char.initialize_character()
    task.initialize_task_list()
    show_command_menu()
    while True:
        try:
            incoming_command = int(input("Command? (to show the command menu again, enter 1): "))
            if incoming_command == 1:
                show_command_menu()
            elif incoming_command == 2:
                char.print_user_character()
            elif incoming_command == 3:
                task.print_user_tasks()
            elif incoming_command == 4:
                task.query_add_user_tasks()
            elif incoming_command == 5:
                task.query_edit_user_tasks()
            elif incoming_command == 6:
                task.query_complete_user_tasks()
            elif incoming_command == 7:
                task.query_delete_user_tasks()
            elif incoming_command == 8:
                print("This one's still in the pipeline. Stay tuned!")
            elif incoming_command == 9:
                quote.quote_picker()
            elif incoming_command == 0:
                print("Thanks for playing!")
                break
            else:
                print("Sorry, I didn't understand that! Make sure you put in a valid number.")
        except Exception as e:
            print("Sorry, I didn't understand that! Make sure you put in a valid number. \n"
                  f"(The exact error was '{e}' if you're interested.)")
            continue
        
    

if __name__ == "__main__":
    main()
