from tkinter import filedialog
from PIL import Image
import shutil
import os

class NewSave():
    def create_newsave_window(self, main, new_save_view):
        self.main = main

        self.new_view = new_save_view.NewSaveView(self)
        self.new_view.grab_set()

    def copy_img(self, path):
        if path != "":
            try:
                Image.open(path)
                shutil.copy(path, "img")
                new_path = f"{os.getcwd()}/img/{os.path.basename(path)}"
                return new_path

            except:
                return ""

    def send(self):
        self.name = self.new_view.configs_frame.name_entry.get()
        self.switch_path = self.new_view.configs_frame.switch_path_entry.get()
        self.switch_foulder = self.new_view.configs_frame.switch_foulder_entry.get()
        self.pc_path = self.new_view.configs_frame.pc_path_entry.get()
        self.icon_path = self.new_view.configs_frame.image_path_entry.get()

        if self.pc_path == "" or self.name == "" or self.switch_path == "" or self.switch_foulder=="":
            self.new_view.configs_frame.warning.configure(fg_color="#b60000", text="FILL IN ALL THE * ENTRIES")
            return

        current_save_dic = {
            "saves":{
                self.name: {
                    "name": f"{self.name}",
                    "switch_path": f"{self.switch_path}",
                    "switch_foulder": f"{self.switch_foulder}",
                    "pc_path": f"{self.pc_path}",
                    "icon_path": f"{self.copy_img(self.icon_path)}"
                }
            }
        }
        
        self.main.modify_data.write_data(current_save_dic)

        self.main.call_window("restart")

    def search_foulder_window(self, entry):
        entry.delete(0, "end")
        path = filedialog.askdirectory()
        entry.insert(0, path)

    def search_file_window(self, entry):
        entry.delete(0, "end")
        path = filedialog.askopenfilename()
        entry.insert(0, path)