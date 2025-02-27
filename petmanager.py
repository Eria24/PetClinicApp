import tkinter as tk
from tkinter import ttk, messagebox
from pet import Pet


class PetsManager:
    def __init__(self, root, pets, app):
        self.pets = pets
        self.app = app 

        self.page = tk.Toplevel(root)
        self.page.title("Manage pets")
        self.page.geometry("1500x600")

        frame = ttk.Frame(self.page, padding=20)
        frame.pack(fill=tk.BOTH)

        title_label=ttk.Label(frame, text="Pet profiles", font=(10))
        title_label.pack(pady=20)

        self.pet_list = tk.Listbox(frame, height=10)
        self.pet_list.pack(fill=tk.BOTH, pady=5)
        self.load_pet_data()

        add_button=ttk.Button(frame, text="Add a pet", command=self.add_pet)
        add_button.pack(fill=tk.X, pady=5)
        edit_button=ttk.Button(frame, text="Edit a pet", command=self.edit_pet)
        edit_button.pack(fill=tk.X, pady=5)
        delete_button=ttk.Button(frame, text="Delete a pet", command=self.delete_pet)
        delete_button.pack(fill=tk.X, pady=5)
        detail_button=ttk.Button(frame, text="Display pets details", command=self.pet_details)
        detail_button.pack(fill=tk.X, pady=5)
        total_pet_number=ttk.Button(frame, text="Display total number of pets", command=self.total_pets)
        total_pet_number.pack(fill=tk.X, pady=5)
        quit_button=ttk.Button(frame, text="Quit", command=self.page.destroy)
        quit_button.pack(fill=tk.X, pady=5)

    def load_pet_data(self):
        self.pet_list.delete(0, tk.END)
        for pet in self.pets:
            self.pet_list.insert(tk.END, pet.name)

    def add_pet(self):
        def save():
            name = name_var.get()
            animal = animal_var.get()
            age = age_var.get()
            medical_history = medical_var.get()
            instructions = inst_var.get()

            if name:
                self.pets.append(Pet(name, animal, age, medical_history, instructions))
                self.app.save_pets()
                self.load_pet_data()
                add_page.destroy()
            else:
                messagebox.showerror("ERROR!!!", "The name field is required!")

        add_page = tk.Toplevel(self.page)
        add_page.geometry("1500x600")
        add_page.title("Add pet")

        ttk.Label(add_page, text="Name:").grid(row=0, column=0,padx=10, pady=10)
        name_var = tk.StringVar()
        ttk.Entry(add_page, textvariable=name_var).grid(row=0, column=1,padx=10, pady=10)

        ttk.Label(add_page, text="Animal:").grid(row=1, column=0,padx=10, pady=10)
        animal_var = tk.StringVar()
        ttk.Entry(add_page, textvariable=animal_var).grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(add_page, text="Age:").grid(row=2, column=0,padx=10, pady=10)
        age_var = tk.StringVar()
        ttk.Entry(add_page, textvariable=age_var).grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(add_page, text="Medical History:").grid(row=3, column=0, padx=10, pady=10)
        medical_var = tk.StringVar()
        ttk.Entry(add_page, textvariable=medical_var, width=50).grid(row=3, column=1,padx=10, pady=10)

        ttk.Label(add_page, text="Care instruction:").grid(row=4, column=0,padx=10, pady=10)
        inst_var = tk.StringVar()
        ttk.Entry(add_page, textvariable=inst_var).grid(row=4, column=1, padx=10, pady=10)

        ttk.Button(add_page, text="Save", command=save).grid(row=5, column=1, padx=10, pady=10)


    def edit_pet(self):
        select_index = self.pet_list.curselection()
        if select_index:
            pet = self.pets[select_index[0]]

            def save():
                name = name_var.get()
                animal = animal_var.get()
                age = age_var.get()
                medical_history = medical_var.get()
                instructions = inst_var.get()

                if name:
                    pet.name = name
                    pet.animal = animal
                    pet.age = age
                    pet.medical_history = medical_history
                    pet.instructions = instructions
                    self.app.save_pets()
                    self.load_pet_data()
                    edit_page.destroy()
                else:
                    messagebox.showerror("ERROR!!!", "The name field is required!")

            edit_page = tk.Toplevel(self.page)
            edit_page.geometry("1500x600")
            edit_page.title("Edit pet")

            ttk.Label(edit_page, text="Name:").grid(row=0, column=0, padx=10, pady=10)
            name_var = tk.StringVar(value=pet.name)
            ttk.Entry(edit_page, textvariable=name_var).grid(row=0, column=1, padx=10, pady=10)

            ttk.Label(edit_page, text="Animal:").grid(row=1, column=0, padx=10, pady=10)
            animal_var = tk.StringVar(value=pet.animal)
            ttk.Entry(edit_page, textvariable=animal_var).grid(row=1, column=1, padx=10, pady=10)

            ttk.Label(edit_page, text="Age:").grid(row=2, column=0, padx=10, pady=10)
            age_var = tk.StringVar(value=pet.age)
            ttk.Entry(edit_page, textvariable=age_var).grid(row=2, column=1, padx=10, pady=10)

            ttk.Label(edit_page, text="Medical History:").grid(row=3, column=0, padx=10, pady=10)
            medical_var = tk.StringVar(value=pet.medical_history)
            ttk.Entry(edit_page, textvariable=medical_var, width=50).grid(row=3, column=1, padx=10, pady=10)

            ttk.Label(edit_page, text="Care instruction:").grid(row=4, column=0, padx=10, pady=10)
            inst_var = tk.StringVar(value=pet.instructions)
            ttk.Entry(edit_page, textvariable=inst_var).grid(row=4, column=1, padx=10, pady=10)

            ttk.Button(edit_page, text="Save", command=save).grid(row=5, column=1, padx=10, pady=10)
        else:
            messagebox.showerror("ERROR!!!", "Must select a pet to edit!")

    def delete_pet(self):
        select_index = self.pet_list.curselection()
        if select_index:
            del self.pets[select_index[0]]
            self.app.save_pets() 
            self.load_pet_data()
        else:
            messagebox.showerror("ERROR!!!", "Must select a pet to delete!")

    def pet_details(self):
        select_index = self.pet_list.curselection()
        if select_index:
            pet = self.pets[select_index[0]]
            details = (
                f"Name: {pet.name}\n"
                f"Animal: {pet.animal}\n"
                f"Age: {pet.age}\n"
                f"Medical history: {pet.medical_history}\n"
                f"Care instructions: {pet.instructions}"
            )
            messagebox.showinfo("Pet details", details)
        else:
            messagebox.showerror("ERROR!!!", "Must select a pet to view details!")

    def total_pets(self):
        total_pets = len(self.pets)
        messagebox.showinfo("Total number of pets", f"The total number of pets is: {total_pets}")