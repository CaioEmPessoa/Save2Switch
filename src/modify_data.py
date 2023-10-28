from pydantic.utils import deep_update
import json
import os

class ModifyData():
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.data_pure = {}
        self.data = {}

    def read_data(self):
        if not os.path.exists("saves_data.json"):
            default_data = {"theme": "Dark"}
            self.write_data(default_data)
            self.data = default_data

        with open("saves_data.json", "r") as read_file:
            self.data_pure = json.load(read_file)
            self.theme = self.data_pure["theme"]
        
        try:
            self.saves_path = self.data_pure["saves"]
        except:
            print("NADA LOL")
            return

        self.names_list = [self.saves_path[key]['name'] for key in self.saves_path]
        self.icon_paths = [self.saves_path[key]['icon_path'] for key in self.saves_path]
        self.pc_paths = [self.saves_path[key]['pc_path'] for key in self.saves_path]
        self.switch_paths = [self.saves_path[key]['switch_path'] for key in self.saves_path]

        self.main.list_number = len(self.names_list)

        self.data = {
            "names":self.names_list,
            "icons":self.icon_paths,
            "pc_paths":self.pc_paths,
            "switch_paths":self.switch_paths,
            "theme": self.theme
        }

    def write_data(self, data):
        self.data_pure = deep_update(self.data_pure, data)
        with open("saves_data.json", "w") as write_file:
            json.dump(self.data_pure, write_file, indent=4)
        

    def clear_data(self, init):
        for item in os.listdir("img"):
            if item != "unknown.png":
                os.remove("img/" + item)
        os.remove("saves_data.json")
                
        init.call_window("restart")