import shutil
from PIL import Image
from tkinter import filedialog

class NewSave():
    def create_newsave_window(self, main, new_save_view):


        self.main = main

        self.new_view = new_save_view.NewSaveView(self)
        #self.new_view.grab_set()
        self.new_view.mainloop()


    def send(self):

        self.name = self.new_view.name_entry.get()
        self.pc_path = self.new_view.pc_path_entry.get()
        self.switch_path = self.new_view.switch_path_entry.get()

        if self.pc_path == "" or self.name == "" or self.switch_path == "":
            print("FILL ALL THE FIELDS")
            self.new_view.send_button.configure(fg_color="Red", text="Caminho Vazio")

        else:
            current_app_dic = {
                self.name: {
                    "name": f"{self.name}",
                    "pc_path": f"\"{self.pc_path}\"",
                    "switch_path": f"{self.switch_path}"
                }
            }
            
            #self.main.write_data(current_app_dic)
            
            self.main.call_window("close")
            self.main.call_window("restart")

    def search_window(self, path_icon):
        if path_icon == "pc":
            self.new_view.pc_path_entry.delete(0, "end")
            self.pc_path = filedialog.askopenfilename()
            self.new_view.pc_path_entry.insert(0, self.pc_path)

        elif path_icon == "switch":
            self.new_view.switch_path_entry.delete(0, "end")
            self.switch_path = filedialog.askopenfilename()
            self.new_view.switch_path_entry.insert(0, self.switch_path)

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


s = NewSave()