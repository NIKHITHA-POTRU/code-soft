import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.task_listbox = tk.Listbox(master, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.view_button = tk.Button(master, text="View Tasks", command=self.view_tasks)
        self.view_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def view_tasks(self):
        if self.tasks:
            messagebox.showinfo("Your To-Do List", "\n".join(self.tasks))
        else:
            messagebox.showinfo("Your To-Do List", "Your To-Do List is empty.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.task_listbox.delete(task_index)
            del self.tasks[task_index]
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
