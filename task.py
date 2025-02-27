class Task:
    def __init__(self, pet_name, type, date, time, status="Pending"):
        self.pet_name = pet_name
        self.type = type
        self.date = date
        self.time = time
        self.status = status
    
    def turn_string(self):
        return f"{self.pet_name}|{self.type}|{self.date}|{self.time}|{self.status}"
    
    @staticmethod
    def convert_string(data):
        pet_name, type, date, time, status = data.strip().split('|')
        return Task(pet_name, type, date, time, status)