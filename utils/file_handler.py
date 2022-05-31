import os
import json

from utils.parameters import folder_path

class FileHandler:
    allowed_formats = ['mkv', 'mp4']

    def __init__(self):
        pass

    def get_file_list(self):
        # Alien.mkv -> ['Alien', 'mkv']
        return [item for item in os.listdir(folder_path) if item.split('.')[-1] in self.allowed_formats]

    @staticmethod
    def write_json(json_path, data):
        if os.path.exists(os.path.dirname(json_path)):
            # ha létezik a json kiírásnál a json-t tartalmazó mappa, akkor mehet az írás
            try:
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
            except Exception as e:
                return False, str(e)
        
        return True


    @staticmethod
    def write_image(image_path, image_link):
        if os.path.exists(os.path.dirname(image_path)):
            # ha létezik a json kiírásnál a json-t tartalmazó mappa, akkor mehet az írás
            try:
                with open(image_path, "wb") as f:
                    f.write(image_link.read())
            except Exception as e:
                return False, str(e)
        
        return True


if __name__ == '__main__':
    handler = FileHandler()

    file_list = handler.get_file_list()
    print(file_list)

    #handler.write_json(None, None)
