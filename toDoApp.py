#toDoApp.py

#global variables
tasks=[]
date=[]
completeTasksName=[]
completeTasksDate=[]

def addTasks(task, deadline): #function to add task
    tasks.append(task)
    date.append(deadline)
    print("\nTask and deadline added!\n")

def showTasks(): #function to show tasks
    if len(tasks)==0 :
        print("\nNo tasks yet.\n")
    else:
        for i in range (len(tasks)):
            print("\n",i+1,".) ",tasks[i], " - ",date[i],"\n")

def showCompletedTasks(): #function to show completed tasks
    if len(completeTasksName)==0 :
        print("\nNo completed tasks yet.\n")
    else:
        print("Completed Tasks:\n")
        for i in range (len(completeTasksName)):
            print("\n",i+1,".) ",completeTasksName[i], " - ",completeTasksDate[i], "\n")

def removeTasks(tasknumber, checker=1): #function to remove task
    if 0 <= tasknumber < len(tasks) and checker==1:
        del tasks[tasknumber]
        del date[tasknumber]
        print("\nTask removed!\n")
    elif 0 <= tasknumber < len(tasks) and checker==0:
        del tasks[tasknumber]
        del date[tasknumber]
    else:
       print("\nTasks does not exist\n")

def addCompleteTask(task, deadline): #function to add completed task
    completeTasksName.append((task))
    completeTasksDate.append((deadline))



def main(): #main function
    print("======= Group 1 To-Do App =======")

    while True: #menu loop
        print("\n[1] Add Task")
        print("[2] Show Tasks")
        print("[3] Remove Task")
        print("[4] Mark Task as Complete")
        print("[5] Show Completed Tasks")
        print("[6] Exit")
        ch = input("Enter choice : ")
        print("=================================")

        # validate menu input
        if not ch.isdigit() or int(ch) not in range(1,7):
            print("Invalid choice! Please enter a number between 1 and 6.")
            continue

        if ch=="1": #add task
            t = input("Enter task : ").strip()
            while t == "":
                print("Task cannot be empty!")
                t = input("Enter task : ").strip()

            d = input("Enter deadline : ").strip()
            while d == "":
                print("Deadline cannot be empty!")
                d = input("Enter deadline : ").strip()

            addTasks(t, d)

        elif ch=="2": #show tasks
            showTasks()

        elif ch=="3": #remove task
            showTasks()
            if len(tasks)==0:
                continue
            try:
                n = int(input("Enter task no to remove: "))
                removeTasks(n-1)
            except ValueError:
                print("Please enter a valid number.")

        elif ch=="4": #mark task as complete
            showTasks()
            if len(tasks)==0:
                continue
            try:
                n=int(input("Enter task no to mark as complete: "))
                if 1 <= n <= len(tasks):
                    addCompleteTask(tasks[n-1], date[n-1])
                    removeTasks(n-1,0)
                    print("Task marked as complete and added to the Completed Tasks list.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif ch == "5": #show completed tasks
            showCompletedTasks() 

        elif ch=="6": #exit
            break

        else:
            print("wrong choice!!")

    print("Exiting application...")
    print("=================================")

# Calling the main function to run the application
main()
