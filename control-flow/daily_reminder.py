## Develop a script named daily_reminder.py. 
## This script will ask the user for a single task, its priority level, 
## and if it is time-sensitive. 
## The program will then provide a customized reminder for that task,
## demonstrating control flow and loops without relying on data structures to store multiple tasks.

user_task = str(input("Enter your task: "))
user_priority = str(input("Priority (high/medium/low: )"))
user_timebound = str(input("Is it time-bound? (yes/no): "))

match user_priority:
    case "high":
        if user_timebound == "yes":
          print(f"Reminder: {user_task} is a high priority task that requires immediate attention today!")
    case "low":
       if user_timebound =="no":
          print(f"{user_task} is a low priority task. Consider completing it when you free time.")
    case _:
      print("print,no task given.")