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
        self.icon_path = self.new_view.self.image_path_entry.get()

        if self.pc_path == "" or self.name == "" or self.switch_path == "":
            self.new_view.wanring.configure(fg_color="#b60000", text="FILL IN ALL THE * ENTRIES")

        else:
            current_app_dic = {
                self.name: {
                    "name": f"{self.name}",
                    "pc_path": f"\"{self.pc_path}\"",
                    "switch_path": f"{self.switch_path}",
                    "icon_path": f"{self.icon_path}"
                }
            }
            
            self.main.write_data(current_app_dic)

            self.main.call_window("restart")

    def search_window(self, entry):
            entry.delete(0, "end")
            path = filedialog.askopenfilename()
            entry.insert(0, path)

    def site_app(self):

        # Caso seja um site
        if self.site_check.get() == 1:
            self.path_label.configure(text="Insira o link para o site")
            self.path_window_button.configure(state="disabled")

            self.browser_label.grid(row=5, column=0, padx=10, columnspan=2, sticky="W")
            self.browser_entry.grid(row=6, column=0, pady=10, padx=10, sticky="W")


        # Não é um site
        if self.site_check.get() == 0:
            self.path_label.configure(text="Insira o caminho do app:")
            self.path_window_button.configure(state="normal")

            self.browser_entry.grid_forget()
            self.browser_label.grid_forget()
