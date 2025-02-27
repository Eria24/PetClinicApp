class Pet:
    def __init__(self, name, animal, age, medical_history, instructions):
        self.name = name
        self.animal = animal
        self.age = age
        self.medical_history = medical_history
        self.instructions = instructions
        
    def turn_string(self):
        return f"{self.name}|{self.animal}|{self.age}|{self.medical_history}|{self.instructions}"
    
    @staticmethod
    def convert_string(data):
        name, animal, age, medical_history, instructions = data.strip().split('|')
        return Pet(name, animal, age, medical_history, instructions)