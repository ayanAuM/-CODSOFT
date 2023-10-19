import tkinter as tk
import csv
from datetime import datetime


def load_tasks():
    try:
        with open("tasks.csv", "r", newline="") as file:
            reader = csv.reader(file)
            return [{"task": row[0], "done": row[1] == "True", "timestamp": row[2]} for row in reader]
    except FileNotFoundError:
        return []


def save_tasks():
    with open("tasks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow(
                [task["task"], str(task["done"]), task["timestamp"]])


def add_task():
    task = task_entry.get()
    if task:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tasks.append({"task": task, "done": False, "timestamp": timestamp})
        refresh_lists()
        task_entry.delete(0, tk.END)
        save_tasks()


def remove_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        del tasks[selected_task_index[0]]
        refresh_lists()
        save_tasks()


def toggle_task_done():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        task = tasks[index]
        task["done"] = not task["done"]
        refresh_lists()
        save_tasks()


def refresh_lists():
    tasks_listbox.delete(0, tk.END)
    completed_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, start=1):
        checkbox = "[\u2713]" if task["done"] else "[ ]"
        formatted_task = f"{i}. {checkbox} {task['task']} ({task['timestamp']})"
        if task["done"]:
            completed_listbox.insert(tk.END, formatted_task)
        else:
            tasks_listbox.insert(tk.END, formatted_task)

# Function to add a task when Enter key is pressed


def add_task_on_enter(event):
    add_task()


# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# Set the window dimensions based on a 1920 x 1080 screen
window_width = 1200  # Adjust as needed
window_height = 800  # Adjust as needed

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Configure the main window
app.configure(bg="DarkOrchid")

title_label = tk.Label(app, text="To-Do List",
                       font=("Helvetica", 20), bg="lightgray")
title_label.pack(pady=20)

# Create a frame for tasks and completed tasks
tasks_frame = tk.Frame(app)
tasks_frame.pack(side=tk.LEFT, padx=50, pady=20)
completed_frame = tk.Frame(app)
completed_frame.pack(side=tk.RIGHT, padx=50, pady=20)

# Create title labels for frames
tasks_title_label = tk.Label(
    tasks_frame, text="Pending Tasks", font=("Helvetica", 16))
tasks_title_label.pack()

completed_title_label = tk.Label(
    completed_frame, text="Completed Tasks", font=("Helvetica", 16))
completed_title_label.pack()

# Create scrollbars for listboxes
tasks_scrollbar = tk.Scrollbar(tasks_frame, orient=tk.VERTICAL)
completed_scrollbar = tk.Scrollbar(completed_frame, orient=tk.VERTICAL)

# Create entry field, buttons, and listboxes as before
task_entry = tk.Entry(tasks_frame, width=50)
task_entry.pack(pady=10)

# Bind the 'Enter key event to add the add_task_on_enter function
task_entry.bind("<Return>", add_task_on_enter)

add_button = tk.Button(tasks_frame, text="Add Task", command=add_task)
add_button.pack()

tasks_listbox = tk.Listbox(
    tasks_frame, selectmode=tk.SINGLE, width=60, height=15, bg="white", yscrollcommand=tasks_scrollbar.set)
tasks_listbox.pack()

completed_listbox = tk.Listbox(
    completed_frame, selectmode=tk.SINGLE, width=60, height=20, bg="white", yscrollcommand=completed_scrollbar.set)
completed_listbox.pack()

remove_button = tk.Button(tasks_frame, text="Remove Task", command=remove_task)
remove_button.pack()

done_button = tk.Button(tasks_frame, text="Mark as Done",
                        command=toggle_task_done)
done_button.pack()

message_label = tk.Label(tasks_frame, text="", fg="black")
message_label.pack()

# Configure scrollbars to work with listboxes
tasks_scrollbar.config(command=tasks_listbox.yview)
tasks_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

completed_scrollbar.config(command=tasks_listbox.yview)
completed_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tasks = load_tasks()


def on_closing():
    save_tasks()
    app.destroy()


app.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()
