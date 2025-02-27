class FileHandling:
    @staticmethod
    def get_data(filename, parser):
        with open(filename, 'r') as file:
            return [parser(line) for line in file if line.strip()]

    @staticmethod
    def save_data(filename, data):
        with open(filename, 'w') as file:
            file.writelines([item.turn_string() + '\n' for item in data])