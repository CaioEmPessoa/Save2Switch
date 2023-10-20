import json
import os

class ModifyData():
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.data = {}

    def read_data(self):
        if not os.path.exists("saves_data.json"):
            theme_data = {"theme": "Dark"}
            self.write_data(theme_data)

            return self.read_data()

        with open("saves_data.json", "r") as read_file:
            self.data = json.load(read_file)
            self.theme = self.data["theme"]
        
        try:
            self.names_list = [self.data[key]['name'] for key in self.data]
            self.icon_paths = [self.data[key]['icon_path'] for key in self.data]
            self.pc_paths = [self.data[key]['pc_path'] for key in self.data]
            self.switch_paths = [self.data[key]['switch_path'] for key in self.data]
        except:
            return self.data

        self.list_number = len(self.names_list)

        data_read = {
            "names":self.names_list,
            "icons":self.icons_paths,
            "pc_paths":self.pc_paths,
            "switch_paths":self.switch_paths,
            "list_number":self.list_number,
            "theme": self.theme
        }
        
        return data_read

    def write_data(self, data):
        self.data.update(data)
        with open("saves_data.json", "w") as write_file:
            json.dump(self.data, write_file, indent=4)

    def clear_data(self, init):
        for item in os.listdir("img"):
            if item != "unknown.png":
                os.remove("img/" + item)
        os.remove("saves_data.json")
                
        init.call_window("restart")