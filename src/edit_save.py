from tkinter import filedialog
import customtkinter as ctk
from PIL import Image
import shutil
import os

class NewSave():
    def create_newsave_window(self, main, new_save_view):
        self.main = main

        self.new_view = new_save_view.NewSaveView(self)
        self.new_view.grab_set()

    def create_edit_window(self, main, new_save_view):
        self.editing = True
        self.create_newsave_window(main, new_save_view)
        self.new_view.edit_itens(self, main)

    def delete_save(self):
        self.name = self.new_view.name_entry.get()
        tmp_data = self.main.data
        del tmp_data["saves"][self.name]
        self.main.modify_data.write_data(tmp_data)
        self.main.call_window("restart")

    def insert_save(self, game):
        game_info = self.main.data["saves"][game]
        self.new_view.switch_path_entry.delete(0, "end")
        self.new_view.switch_path_entry.insert(0, game_info["switch_path"])
        self.new_view.switch_foulder_entry.delete(0, "end")
        self.new_view.switch_foulder_entry.insert(0, game_info["switch_foulder"])
        self.new_view.pc_path_entry.delete(0, "end")
        self.new_view.pc_path_entry.insert(0, game_info["pc_path"])
        self.new_view.image_path_entry.delete(0, "end")
        self.new_view.image_path_entry.insert(0, game_info["icon_path"])

    def copy_img(self, path):
        if path != "" or path != "None":
            try:
                Image.open(path)
                shutil.copy(path, "img")
                new_path = f"{os.getcwd()}/img/{os.path.basename(path)}"
                return new_path

            except:
                return ""

    def send(self):
        self.name = self.new_view.name_entry.get()
        self.switch_path = self.new_view.switch_path_entry.get()
        self.switch_foulder = self.new_view.switch_foulder_entry.get()
        self.pc_path = self.new_view.pc_path_entry.get()
        self.icon_path = self.new_view.image_path_entry.get()

        if self.pc_path == "" or self.name == "" or self.switch_path == "" or self.switch_foulder=="":
            self.new_view.warning.configure(fg_color="#b60000", text_color="white", text="FILL IN ALL THE * ENTRIES")
            return

        saves_list = [name for name in self.main.data["saves"]]
        
        if self.name in saves_list and not self.editing:
            self.new_view.warning.configure(fg_color="#b60000", text_color="white", text="Please choose a different name.\nTo edit an app, go to the edit window.")
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