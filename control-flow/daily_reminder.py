task =input("Enter your task:")
priority =input("Priority (high/medium/low):")
time_bount =input("Is it time-bound? (yes/no):")


match priority:
    case "low":
        if time_bount =='yes':
            print(f"'{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bount =='yes':
            print(f"'{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a medium priority task. Consider completing it when you have free time.")
    case "high":
        if time_bount =='yes':
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a high priority task. Consider completing it when you have free time.")

 
 
