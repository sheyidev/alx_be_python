## Develop a script named daily_reminder.py. 
## This script will ask the user for a single task, its priority level, 
## and if it is time-sensitive. 
## The program will then provide a customized reminder for that task,
## demonstrating control flow and loops without relying on data structures to store multiple tasks.

task = input(f"Enter your task: ")
priority = input(f"Priority (high/medium/low): ")
time_bound = input(f"Is it time-bound? (yes/no): ")

match priority :
    case "high":
        if time_bound == "yes":
          print("Reminder: {task} is a high priority task that requires immediate attention today!")
    case "low":
       if time_bound =="no":
          print("{task} is a low priority task. Consider completing it when you free time.")
    case "medium":
        print("{task} is a medium priority task.")
    case _:
      print("no task given.")