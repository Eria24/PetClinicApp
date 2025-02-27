import tkinter as tk
from tkinter import ttk, messagebox
from task import Task


class TasksManager:
    def __init__(self, root, tasks, pets, app):
        self.tasks = tasks
        self.pets = pets
        self.app = app 

        self.page = tk.Toplevel(root)
        self.page.title("Manage tasks")
        self.page.geometry("1500x600")

        frame = ttk.Frame(self.page, padding=10)
        frame.pack(fill=tk.BOTH)

        title_label=ttk.Label(frame, text="Tasks", font=(10))
        title_label.pack(pady=20)

        self.task_list = tk.Listbox(frame, height=10)
        self.task_list.pack(fill=tk.BOTH, pady=5)
        self.load_task_data()

        add_button=ttk.Button(frame, text="Add a task", command=self.add_task)
        add_button.pack(fill=tk.X, pady=5)
        edit_button=ttk.Button(frame, text="Edit a task", command=self.edit_task)
        edit_button.pack(fill=tk.X, pady=5)
        delete_button=ttk.Button(frame, text="Delete a task", command=self.delete_task)
        delete_button.pack(fill=tk.X, pady=5)
        mark_as_complete_button=ttk.Button(frame, text="Mark task as completed", command=self.mark_completed)
        mark_as_complete_button.pack(fill=tk.X, pady=5)
        tasks_report_button=ttk.Button(frame, text="Tasks report", command=self.tasks_report)
        tasks_report_button.pack(fill=tk.X, pady=5)
        quit_button=ttk.Button(frame, text="Quit", command=self.page.destroy)
        quit_button.pack(fill=tk.X, pady=5)

    def load_task_data(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, f"{task.pet_name} - {task.type} - {task.date} - {task.time} - {task.status}")

    def add_task(self):
        def save():
            pet_name = pet_var.get()
            task_type = type_var.get()
            date = date_var.get()
            time = time_var.get()
            status = status_var.get()
    
            if pet_name and task_type and date and time:
                self.tasks.append(Task(pet_name, task_type, date, time, status))
                self.app.save_tasks()
                self.load_task_data()
                add_page.destroy()
            else:
                messagebox.showerror("ERROR!!!", "All fields are required!")

        add_page = tk.Toplevel(self.page)
        add_page.geometry("1500x600")
        add_page.title("Add task")

        pet_names = []
        for pet in self.pets:
            pet_names.append(pet.name)
        
        ttk.Label(add_page, text="Pet Name:").grid(row=0, column=0, padx=10, pady=10)
        pet_var = tk.StringVar()
        ttk.Combobox(add_page, textvariable=pet_var, values=pet_names, state="readonly").grid(row=0, column=1, padx=10, pady=10)
    
        ttk.Label(add_page, text="Task Type:").grid(row=1, column=0, padx=10, pady=10)
        type_var = tk.StringVar()
        ttk.Entry(add_page, textvariable=type_var).grid(row=1, column=1, padx=10, pady=10)
    
        ttk.Label(add_page, text="Date:").grid(row=2, column=0, padx=10, pady=10)
        date_var = tk.StringVar()
        ttk.Entry(add_page, textvariable=date_var).grid(row=2, column=1, padx=10, pady=10)
    
        ttk.Label(add_page, text="Time:").grid(row=3, column=0, padx=10, pady=10)
        time_var = tk.StringVar()
        ttk.Entry(add_page, textvariable=time_var).grid(row=3, column=1, padx=10, pady=10)
    
        ttk.Label(add_page, text="Status:").grid(row=4, column=0, padx=10, pady=10)
        status_var = tk.StringVar(value="Pending")
        ttk.Combobox(add_page, textvariable=status_var, values=["Pending", "Completed"], state="readonly").grid(row=4, column=1, padx=5, pady=5)

        ttk.Button(add_page, text="Save", command=save).grid(row=5, column=1, padx=10, pady=10)

    def edit_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]

            def save():
                task.pet_name = pet_var.get()
                task.type = type_var.get()
                task.date = date_var.get()
                task.time = time_var.get()
                task.status = status_var.get()
    
                if task.pet_name and task.type and task.date and task.time:
                    self.app.save_tasks()
                    self.load_task_data()
                    edit_page.destroy()
                else:
                    messagebox.showerror("ERROR!!!", "All fields are required!")

            edit_page = tk.Toplevel(self.page)
            edit_page.geometry("1500x600")
            edit_page.title("Edit task")

            pet_names = []
            for pet in self.pets:
                pet_names.append(pet.name)

            ttk.Label(edit_page, text="Pet name:").grid(row=0, column=0, padx=10, pady=10)
            pet_var = tk.StringVar(value=task.pet_name)
            ttk.Combobox(edit_page, textvariable=pet_var, values=pet_names, state="readonly").grid(row=0, column=1, padx=10, pady=10)
    
            ttk.Label(edit_page, text="Task type:").grid(row=1, column=0, padx=10, pady=10)
            type_var = tk.StringVar(value=task.type)
            ttk.Entry(edit_page, textvariable=type_var).grid(row=1, column=1, padx=10, pady=10)
    
            ttk.Label(edit_page, text="Date:").grid(row=2, column=0, padx=10, pady=10)
            date_var = tk.StringVar(value=task.date)
            ttk.Entry(edit_page, textvariable=date_var).grid(row=2, column=1, padx=10, pady=10)
    
            ttk.Label(edit_page, text="Time:").grid(row=3, column=0, padx=10, pady=10)
            time_var = tk.StringVar(value=task.time)
            ttk.Entry(edit_page, textvariable=time_var).grid(row=3, column=1, padx=10, pady=10)
    
            ttk.Label(edit_page, text="Status:").grid(row=4, column=0, padx=10, pady=10)
            status_var = tk.StringVar(value=task.status)
            ttk.Combobox(edit_page, textvariable=status_var, values=["Pending", "Completed"], state="readonly").grid(row=4, column=1, padx=10, pady=10)
    
            ttk.Button(edit_page, text="Save", command=save).grid(row=5, column=0, padx=10, pady=10)

        else:
            messagebox.showerror("ERROR!!!", "Must select a task to edit!")

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.app.save_tasks() 
            self.load_task_data()
        else:
            messagebox.showerror("ERROR!!!", "Must select a task to delete!")

    def mark_completed(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.tasks[selected_index[0]].status = "Completed"
            self.app.save_tasks() 
            self.load_task_data()
        else:
            messagebox.showerror("ERROR!!!", "Must select a task to mark as completed!")
   
    def tasks_report(self):
        total_tasks = len(self.tasks)
        completed_tasks = 0
        for task in self.tasks:
            if task.status == "Completed":
                completed_tasks += 1
        pending_tasks = total_tasks - completed_tasks
        report= (
            f"Total tasks: {total_tasks}\n"
            f"Completed tasks: {completed_tasks}\n"
            f"Pending tasks: {pending_tasks}"
        )
        messagebox.showinfo("Tasks report:", report)