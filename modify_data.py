import json
import os

class ModifyData():
    def __init__(self, main):
        super().__init__()
        self.main = main

    def read_data(self):
        with open("saves_data.json", "r") as read_file:
            self.data = json.load(read_file)

            try:
                self.tema = self.data["tema"]
                
            except:
                self.tema = "Light"
                theme_data = {"tema": "Light"}
                self.write_data(theme_data)
                self.main.switch_theme()

        for key in self.data:
            if key != "tema":
                # Access the elements dynamically using the key
                element = self.data[key]

                self.names_list.append(element['name'])
                self.path_list.append(element['path'])
                self.icon_list.append(element['icon'])

        self.list_number = len(self.names_list)
        self.switch_theme()

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