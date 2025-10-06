# toDoApp.py

tasks=[]
date=[]
completeTasksName=[]
completeTasksDate=[]

def addtask(task, deadline) : #function to add task
    tasks.append(task)
    date.append(deadline)
    print("\nTask and deadline added!\n")

def showTasks( ): #function to show tasks
    if len(tasks)==0 :
      print("\nNo tasks yet.\n")
    else:
     for i in range (len(tasks)):
      print("\n",i+1,".) ",tasks[i], " - ",date[i],"\n")

def showCompletedTasks( ): #function to show completed tasks
    if len(completeTasksName)==0 :
      print("\nNo completed tasks yet.\n")
    else:
     print("Completed Tasks:\n")
     for i in range (len(completeTasksName)):
      print("\n",i+1,".) ",completeTasksName[i], " - ",completeTasksDate[i], "\n")

def removetask(tasknumber, checker=1): #function to remove task
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
        if ch=="1": #add task
            t = input("Enter task : ")
            d = input("Enter deadline : ")
            addtask(t, d)
        elif ch=="2": #show tasks
            showTasks()
        elif ch=="3": #remove task
            showTasks()
            if len(tasks)==0:
                continue
            n=int(input("enter task no to remove: "))
            removetask(n-1)
        elif ch=="4": #mark task as complete
            showTasks()
            n=int(input("enter task no to remove: "))
            addCompleteTask(tasks[n-1], date[n-1])
            removetask(n-1,0)

            print("Task marked as complete and added to the Completed Tasks list.")
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
