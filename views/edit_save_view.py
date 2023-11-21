import customtkinter as ctk
from os import getcwd

class NewSaveView(ctk.CTkToplevel):
    def __init__(self, new_save):
        super().__init__()

        self.minsize(280,420)
        self.maxsize(500,600)

        # open screen centered
        w = 370
        h = 500
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y-35))

        self.grid_rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], weight=1)
        self.grid_columnconfigure([0, 1, 2], weight=1)

        self.title("Save2Switch new save.")
        self.after(200, lambda: self.wm_iconbitmap(f'{getcwd()}/img/Save2Switch.ico'))
        # can only do the above to make icons on toplevels work

        self.create_itens(new_save)

    def create_itens(self, new_save):
        self.name_label = ctk.CTkLabel(master=self, justify="left", font=('',16), text="The game name to display:")
        self.name_label.grid(row=1, column=0, padx=10, columnspan=3)

        self.name_entry = ctk.CTkEntry(master=self, width=220, font=('',16))
        self.name_entry.grid(row=2, column=0, pady=10, padx=10, columnspan=3)

        self.switch_path_label = ctk.CTkLabel(master=self, font=('',16), justify="left",
                                              text="The name of the game for JKSV,\nor title ID for EdiZon:")
        self.switch_path_label.grid(row=3, column=0, padx=10, columnspan=3)

        self.switch_path_entry = ctk.CTkEntry(master=self, width=220, font=('',16))
        self.switch_path_entry.grid(row=4, column=0, pady=10, padx=10, columnspan=3)

        self.switch_foulder_label = ctk.CTkLabel(master=self, font=('',16), justify="left",
                                                  text="The foulder you'll extract the save:")
        self.switch_foulder_label.grid(row=5, column=0, padx=10, columnspan=3)

        self.switch_foulder_entry = ctk.CTkEntry(master=self, width=220, font=('',16))
        self.switch_foulder_entry.grid(row=6, column=0, pady=10, padx=10, columnspan=3)

        self.pc_path_label = ctk.CTkLabel(master=self, font=('',16), text="The path to the PC save:")
        self.pc_path_label.grid(row=7, column=0, padx=10, columnspan=3)

        self.pc_path_entry = ctk.CTkEntry(master=self, width=150, font=('',16))
        self.pc_path_entry.grid(row=8, column=0, pady=10, padx=10, sticky="E", columnspan=2)

        self.pc_window_button = ctk.CTkButton(master=self, text="Window", width=30, 
                                    command=lambda: new_save.search_foulder_window(self.pc_path_entry))
        self.pc_window_button.grid(row=8, column=2, sticky="W")

        self.image_path_label = ctk.CTkLabel(master=self, font=('',16), text="Optional: Path to the preview image:")
        self.image_path_label.grid(row=9, column=0, padx=10, columnspan=3)

        self.image_path_entry = ctk.CTkEntry(master=self, width=150, font=('',16))
        self.image_path_entry.grid(row=10, column=0, pady=10, padx=10, sticky="E", columnspan=2)

        self.image_window_button = ctk.CTkButton(master=self, text="Window", width=30, 
                                    command=lambda: new_save.search_file_window(self.image_path_entry))
        self.image_window_button.grid(row=10, column=2, sticky="W")

        self.send_button = ctk.CTkButton(master=self, command=lambda: new_save.send(), text="Concluir")
        self.send_button.grid(row=11, pady=15, columnspan=3)

        self.warning = ctk.CTkLabel(master=self, font=('',16), text="")
        self.warning.grid(row=12, column=0, columnspan=4, sticky="EW")

    def edit_itens(self, new_save, main):
        self.title("Save2Switch Editing save...")
        self.saves_list = [save for save in main.data["saves"]]
        self.name_entry.destroy()
        self.name_entry = ctk.CTkOptionMenu(master=self, values=self.saves_list, width=220, font=('',16), command=new_save.insert_save,
                                fg_color=("White", "#343638"), text_color=("Black", "White"), button_color=("#969da3", "#565a5f"))
        self.name_entry.grid(row=2, column=0, columnspan=3)

        self.image_path_label.configure(text="Path to the preview image:\n(empty to remove)")

        self.send_button.grid_forget()
        self.send_button.configure(width=100)
        self.send_button.grid(row=11, column=0, pady=15, columnspan=1)
        
        self.delete_button = ctk.CTkButton(master=self, fg_color="red", text="delete", width=100,
                                           command=new_save.delete_save)
        self.delete_button.grid(row=11, column=2, pady=15, columnspan=1)

        new_save.insert_save(self.saves_list[0])