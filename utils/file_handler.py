import os
import json

from parameters import folder_path

class FileHandler:
    allowed_formats = ['mkv', 'mp4']

    def __init__(self):
        pass

    def get_file_list(self):
        # Alien.mkv -> ['Alien', 'mkv']
        return [item for item in os.listdir(folder_path) if item.split('.')[-1] in self.allowed_formats]

    

if __name__ == '__main__':
    handler = FileHandler()

    file_list = handler.get_file_list()
    print(file_list)