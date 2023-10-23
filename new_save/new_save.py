import shutil
from PIL import Image
from tkinter import filedialog

class NewSave():
    def create_newsave_window(self, main, new_save_view):
        self.main = main

        self.new_view = new_save_view.NewSaveView(self)
        self.new_view.grab_set()

    def send(self):
        self.name = self.new_view.name_entry.get()
        self.pc_path = self.new_view.pc_path_entry.get()
        self.switch_path = self.new_view.switch_path_entry.get()
        self.icon_path = self.new_view.image_path_entry.get()

        if self.pc_path == "" or self.name == "" or self.switch_path == "":
            self.new_view.wanring.configure(fg_color="#b60000", text="FILL IN ALL THE * ENTRIES")

        else:
            current_save_dic = {
                "saves":{
                    self.name: {
                        "name": f"{self.name}",
                        "pc_path": f"{self.pc_path}",
                        "switch_path": f"{self.switch_path}",
                        "icon_path": f"{self.icon_path}"
                    }
                }
            }
            
            self.main.modify_data.write_data(current_save_dic)

            self.main.call_window("restart")

    def search_windows(self, entry):
        check = self.new_view.checkbox.get()

        if not check:
            self.search_file_window(entry)
        if check:
            self.search_foulder_window(entry)

    def search_foulder_window(self, entry):
        entry.delete(0, "end")
        path = filedialog.askdirectory()
        entry.insert(0, path)

    def search_file_window(self, entry):
        entry.delete(0, "end")
        path = filedialog.askopenfilename()
        entry.insert(0, path)