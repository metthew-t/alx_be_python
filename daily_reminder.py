task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = inpu("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task. focus on completing it soon. ")
    case "medium":
        is time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
        else:
            print(f"Note: '{task}'is a medium priority task. schedule time for it this week.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but has deadline today. ")
        else:
            print("Note: '{task}' is a low priority task. consider completing it when you have free time. ")
    case_:
        print(f"Invalid priority level. please use high, medium, or low. ")

