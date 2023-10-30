from pydantic.utils import deep_update
import json
import os

class ModifyData():
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.data = {}

    def read_data(self):
        if not os.path.exists("saves_data.json"):
            default_data = {"theme": "Dark",
                            "switch_ip": "0.0.0.0",
                            "save_app": "JKSV",
                            "username": "anonymous",
                            "password": ""}
            self.write_data(default_data)
            self.data = default_data

        with open("saves_data.json", "r") as read_file:
            self.data = json.load(read_file)

        return self.data

    def write_data(self, data):
        self.data = deep_update(self.data, data)
        with open("saves_data.json", "w") as write_file:
            json.dump(self.data, write_file, indent=4)
        

    def clear_data(self, init):
        for item in os.listdir("img"):
            if item != "unknown.png":
                os.remove("img/" + item)
        os.remove("saves_data.json")
                
        init.call_window("restart")