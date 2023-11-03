from tkinter import filedialog
import shutil
import os

class NewSave():
    def create_newsave_window(self, main, new_save_view):
        self.main = main

        self.new_view = new_save_view.NewSaveView(self)
        self.new_view.grab_set()

    def send(self):
        self.name = self.new_view.configs_frame.name_entry.get()
        self.switch_path = self.new_view.configs_frame.switch_path_entry.get()
        self.pc_path = self.new_view.configs_frame.pc_path_entry.get()
        self.icon_path = self.new_view.configs_frame.image_path_entry.get()

        if self.pc_path == "" or self.name == "" or self.switch_path == "":
            self.new_view.configs_frame.warning.configure(fg_color="#b60000", text="FILL IN ALL THE * ENTRIES")
            return
        
        if os.path.isfile(self.icon_path):
            working_path = os.getcwd()
            icon_name = os.path.basename(self.icon_path)
            
            shutil.copy(self.icon_path, f"{working_path}/img/{icon_name}")
            self.icon_path = f"{working_path}/img/{icon_name}"

        current_save_dic = {
            "saves":{
                self.name: {
                    "name": f"{self.name}",
                    "switch_path": f"{self.switch_path}",
                    "pc_path": f"{self.pc_path}",
                    "icon_path": f"{self.icon_path}"
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