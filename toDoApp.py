# toDoApp.py

tasks=[]
date=[]

def addtask(task, deadline) :
    tasks.append(task)
    date.append(deadline)
    print("task and deadline added!")

def showTasks( ):
    if len(tasks)==0 :
      print("No tasks yet.")
    else:
     for i in range (len(tasks)):
      print(i+1,".) ",tasks[i], " - ",date[i])

def removetask(tasknumber):
    if 0 <= tasknumber < len(tasks):
        del tasks[tasknumber]
        print("Task removed!")
    else:
       print("Tasks does not exist")


def main():
    print("======= Group 1 To-Do App =======")

    while True:
        print("[1] Add Task")
        print("[2] Show Tasks")
        print("[3] Remove Task")
        print("[4] Exit")
        ch = input("enter choice : ")
        print("=================================")
        if ch=="1":
            t = input("enter task : ")
            addtask(t)
        elif ch=="2":
            showTasks()
        elif ch=="3":
            n=int(input("enter task no to remove: "))
            removetask(n-1)   
        elif ch=="4":
            break
        else:
            print("wrong choice!!")

    print("Exiting application...")
    print("=================================")
main()
