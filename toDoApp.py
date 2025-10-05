# toDoApp.py

tasks=[]
date=[]
completeTasks=[]

def addtask(task, deadline) :
    tasks.append(task)
    date.append(deadline)
    print("\nTask and deadline added!\n")

def showTasks( ):
    if len(tasks)==0 :
      print("\nNo tasks yet.\n")
    else:
     for i in range (len(tasks)):
      print("\n",i+1,".) ",tasks[i], " - ",date[i],"\n")

def showCompletedTasks( ):
    if len(completeTasks)==0 :
      print("\nNo completed tasks yet.\n")
    else:
     for i in range (len(completeTasks)):
      print("Completed Tasks:\n")
      print("\n",i+1,".) ",completeTasks[i], " - ",date[i], "\n")

def removetask(tasknumber):
    if 0 <= tasknumber < len(tasks):
        del tasks[tasknumber]
        print("\nTask removed!\n")
    else:
       print("\nTasks does not exist\n")

def addCompleteTask(task, deadline):
    completeTasks.append((task, deadline))



def main():
    print("======= Group 1 To-Do App =======")

    while True:
        print("[1] Add Task")
        print("[2] Show Tasks")
        print("[3] Remove Task")
        print("[4] Show Completed Tasks")
        print("[5] Exit")
        ch = input("Enter choice : ")
        print("=================================")
        if ch=="1":
            t = input("Enter task : ")
            d = input("Enter deadline : ")
            addtask(t, d)
        elif ch=="2":
            showTasks()
        elif ch=="3":
            showTasks()
            n=int(input("enter task no to remove: "))
            addCompleteTask(tasks[n-1], date[n-1])
            removetask(n-1)

            print("Task marked as complete and added to the Completed Tasks list.")
        elif ch == "4":
           showCompletedTasks() 
        elif ch=="5":
            break
        else:
            print("wrong choice!!")

    print("Exiting application...")
    print("=================================")
main()
