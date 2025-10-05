# toDoApp.py

tasks=[]
date=[]

def addtask(task, deadline) :
    tasks.append(task)
    date.append(deadline)
    print("task and deadline added!")

def showTasks( ):
    if len(tasks)==0 :
      print("no tasks yet")
    else:
     for i in range (len(tasks)):
      print(i+1,".) ",tasks[i], " - ",date[i])

def removetask(tasknumber):
    tasks.pop(tasknumber) 
    date.pop(tasknumber)
    print("task removed!!")


while True:
    print("1 Add Task")
    print("2.Show Tasks")
    print("3.Remove Task")
    print("4- Exit")
    ch = input("enter choice : ")
    if ch=="1":
        t = input("enter task : ")
        d = input("enter deadline : ")
        addtask(t,d)
    elif ch=="2":
        showTasks()
    elif ch=="3":
        print("Tasks:")
        showTasks()
        n=int(input("enter task no to remove: "))
        n+=1
        removetask(n)   
    elif ch=="4":
        break
    else:
        print("wrong choice!!")