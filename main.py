import tkinter as tk
from tkinter import ttk
from files import FileHandling
from pet import Pet
from petmanager import PetsManager
from task import Task
from taskmanager import TasksManager


class PetClinicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pet Clinic")
        root.geometry("1500x600")
    
        self.pets = FileHandling.get_data('pets.txt', Pet.convert_string)
        self.tasks = FileHandling.get_data('tasks.txt', Task.convert_string)
    
        self.main_page()

    def main_page(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill=tk.BOTH)

        title_label=ttk.Label(frame, text="Pet clinic", font=(20))
        title_label.pack(pady=10)
        pets_button=ttk.Button(frame, text="Manage pets", command=self.manage_pets)
        pets_button.pack(fill=tk.X, pady=5)
        tasks_button=ttk.Button(frame, text="Manage tasks", command=self.manage_tasks)
        tasks_button.pack(fill=tk.X, pady=5)
        quit_button = ttk.Button(frame, text="Quit", command=self.root.quit)
        quit_button.pack(fill=tk.X, pady=5)

    def manage_pets(self):
        PetsManager(self.root, self.pets, self)

    def manage_tasks(self):
        TasksManager(self.root, self.tasks, self.pets, self)

    def save_pets(self):
        FileHandling.save_data('pets.txt', self.pets)

    def save_tasks(self):
        FileHandling.save_data('tasks.txt', self.tasks)


if __name__ == "__main__":
 root = tk.Tk()
 app = PetClinicApp(root)
 root.mainloop()