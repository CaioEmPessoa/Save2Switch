import main_view
from new_save import new_save
from new_save import new_save_view
from modify_data import ModifyData

from customtkinter import set_appearance_mode
import shutil

class CopySave():
    def __init__(self):
        super().__init__()

        # ⬇ didn't like that list_number ⬇ #
        self.list_number = 0

        self.modify_data = ModifyData(self)
        self.modify_data.read_data()

        self.theme = self.modify_data.data_pure["theme"]
        print(self.list_number)

        self.switch_theme()

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
                copysave = CopySave()

            case "close":
                self.main_view.destroy()
            
            case "new_save":
                self.add_save = new_save.NewSave()
                self.add_save.create_newsave_window(self, new_save_view)

    def copy_save(src, dst):
        shutil.copy(src, dst)

if __name__ == "__main__":
    copysave = CopySave()