# 📝 To-Do App (Python Console Application)

## 📖 Project Overview
The **To-Do App** is a simple Python console-based application that allows users to manage their daily tasks efficiently.  
Users can:
- Add tasks with deadlines  
- View all pending tasks  
- Remove specific tasks  
- Mark tasks as completed  
- View the list of completed tasks  

This project demonstrates basic Python concepts such as:
- Lists and global variables  
- User input validation  
- Functions and modular code design  
- Loops and conditional statements  

---

## ⚙️ Features
✅ Add new tasks with a deadline  
✅ Display all current tasks  
✅ Remove tasks by their number  
✅ Mark tasks as completed  
✅ Display completed tasks separately  
✅ Input validation for better user experience  

---

## 🧠 How It Works
The app uses **four global lists** to manage tasks and deadlines:
- `tasks[]` → stores task names  
- `date[]` → stores deadlines  
- `completeTasksName[]` → stores completed task names  
- `completeTasksDate[]` → stores completed task deadlines  

When you add or complete a task, the corresponding data is stored or moved between these lists.

---

## 🚀 Setup Instructions

### 1️⃣ Prerequisites
Make sure you have **Python 3.x** installed on your computer.  
You can check by running:
```bash
python --version
```

If Python is not installed, download it here:  
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

### 2️⃣ Download the Project
Clone or download this repository to your local machine:
```bash
git clone https://github.com/your-username/toDoApp.git
```
Or simply copy the `toDoApp.py` file to a folder of your choice.

---

### 3️⃣ Run the Application
Navigate to the folder where `toDoApp.py` is located, then run:
```bash
python toDoApp.py
```

---

## 🧭 Usage Guide

Once the program runs, you’ll see the main menu:
```
======= Group 1 To-Do App =======

[1] Add Task
[2] Show Tasks
[3] Remove Task
[4] Mark Task as Complete
[5] Show Completed Tasks
[6] Exit
Enter choice :
=================================
```

Enter the number corresponding to your desired action.  
The app will guide you through each process (e.g., entering task details or selecting a task to remove).

---

## 💡 Example Usage
```
Enter choice : 1
Enter task : Finish report
Enter deadline : Oct 15
Task and deadline added!

Enter choice : 2
1.) Finish report - Oct 15
```

---

## 👨‍💻 Authors
Developed by **Group 1** as a Python programming exercise.
Members: 
```
    Aganinta, Kyle Azriel
    Ganotisi, Bea Margaret
    Ipil, Shikkari Jerard
    Tuyay, John Benedict
```
