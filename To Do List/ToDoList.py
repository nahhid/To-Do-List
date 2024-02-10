import tkinter as tk
from tkinter import messagebox, filedialog

# Function to add a task
def insertTask():
    task = insertField.get()
    if task != "":
        tasksList.insert(tk.END, task)
        insertField.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Function to remove a task
def removeTask():
    try:
        selected_task_index = tasksList.curselection()[0]
        tasksList.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

# Function to save tasks to a file
def saveTasksToFile():
    tasks = tasksList.get(0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(task + "\n")

# Create the main window
window = tk.Tk()
window.title("To-Do List")
window.geometry("300x300")
window.configure(background="grey")

# Label and entry field
enterTask = tk.Label(window, text="Please enter your task", bg="green")
insertField = tk.Entry(window)

# Submit button
Submit = tk.Button(window, text="Submit", fg="black", bg="light green", command=insertTask)

# Remove button
Remove = tk.Button(window, text="Remove", fg="black", bg="orange", command=removeTask)

# Save button
Save = tk.Button(window, text="Save to File", fg="black", bg="light blue", command=saveTasksToFile)

# Listbox to display tasks
tasksList = tk.Listbox(window, selectmode=tk.SINGLE, height=10, width=25)

# Pack widgets
enterTask.pack()
insertField.pack()
Submit.pack()
Remove.pack()
Save.pack()
tasksList.pack()

# Run the Tkinter event loop
window.mainloop()
