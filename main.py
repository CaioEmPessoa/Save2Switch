from views import main_view
from src.modify_data import ModifyData

from src import ftp_connect
from src import new_save
from views import new_save_view
from src import config
from views import config_view

from customtkinter import set_appearance_mode

class Main():
    def __init__(self):
        super().__init__()
        
        self.modify_data = ModifyData(self)
        self.data = self.modify_data.read_data()

        self.theme = self.data["theme"]
        self.switch_theme()
        
        self.connect_switch = ftp_connect.connectFTP(self)

        self.add_save = new_save.NewSave()
        self.main_view = main_view.Root()
        self.main_view.CreateWindow(self)
        self.main_view.mainloop()

    def switch_theme(self):
        # If the theme is dark it switches it to light and vice-versa
        if self.theme == "Light":
            theme_data = {"theme": "Light"}
            self.theme = "Dark"

        elif self.theme == "Dark":
            theme_data = {"theme": "Dark"}
            self.theme = "Light"

        self.modify_data.write_data(theme_data)
        set_appearance_mode(self.theme)

    def call_window(self, window):
        match window:
            case "restart":
                self.main_view.destroy()
                copysave = Main()

            case "close":
                self.main_view.destroy()
             
            case "new_save":
                self.add_save.create_newsave_window(self, new_save_view)

            case "edit":
                self.add_save.create_edit_window(self, new_save_view)

            case "config":
                self.configs = config.Config()
                self.configs.create_config_window(self, config_view)

if __name__ == "__main__":
    copysave = Main()
