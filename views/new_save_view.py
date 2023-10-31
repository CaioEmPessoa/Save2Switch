import customtkinter as ctk

class newSaveConfig(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def create_itens(self, new_save):

        # LABELS
        self.warning = ctk.CTkLabel(master=self, font=('',16), text="")
        self.warning.grid(row=0, column=0, columnspan=3, sticky="W", pady=10, padx=10)

        self.name_label = ctk.CTkLabel(master=self, justify="left", font=('',16), text="The game name to display:")
        self.name_label.grid(row=1, column=0, padx=10, columnspan=3, sticky="W")

        self.switch_path_label = ctk.CTkLabel(master=self, font=('',16), justify="left",
                                              text="The name of the game for JKSV,\nor title ID for EdiZon:")
        self.switch_path_label.grid(row=4, column=0, padx=10, columnspan=2, sticky="W")

        self.pc_path_label = ctk.CTkLabel(master=self, font=('',16), text="The path to the PC foulder/file:")
        self.pc_path_label.grid(row=8, column=0, padx=10, columnspan=2, sticky="W")

        self.image_path_label = ctk.CTkLabel(master=self, font=('',16), text="Optional: Path to the preview image:")
        self.image_path_label.grid(row=10, column=0, padx=10, columnspan=2, sticky="W")

        self.warning = ctk.CTkLabel(master=self, font=('',16), text="")
        self.warning.grid(row=13, column=0, columnspan=2, sticky="EW")
        # END Labels

        # ENTRY
        self.name_entry = ctk.CTkEntry(master=self, width=200)
        self.name_entry.grid(row=2, column=0, pady=10, padx=10, sticky="W", columnspan=3)

        self.pc_path_entry = ctk.CTkEntry(master=self, width=200)
        self.pc_path_entry.grid(row=9, column=0, pady=10, padx=10, sticky="W")
        
        self.switch_path_entry = ctk.CTkEntry(master=self, width=200)
        self.switch_path_entry.grid(row=5, column=0, pady=10, padx=10, sticky="W")

        self.image_path_entry = ctk.CTkEntry(master=self, width=200)
        self.image_path_entry.grid(row=11, column=0, pady=10, padx=10, sticky="W")
        # END Entry

        # Buttons
        self.pc_window_button = ctk.CTkButton(master=self, text="Window", width=10, 
                                    command=lambda: new_save.search_windows(self.pc_path_entry))
        self.pc_window_button.grid(row=9, column=1, sticky="W")

        self.image_window_button = ctk.CTkButton(master=self, text="Window", width=10, 
                                    command=lambda: new_save.search_windows(self.image_path_entry))
        self.image_window_button.grid(row=11, column=1, sticky="W")

        self.checkbox_label = ctk.CTkLabel(master=self, font=('',16), text="Foulder Mode for Window button:")
        self.checkbox_label.grid(row=12, column=0, pady=15, padx=10)

        self.checkbox = ctk.CTkCheckBox(master=self, text="")
        self.checkbox.grid(row=12, column=1, pady=15)

        self.send_button = ctk.CTkButton(master=self, command=lambda: new_save.send(), text="Concluir")
        self.send_button.grid(row=13, pady=15)
        # END Buttons

class NewSaveView(ctk.CTkToplevel):
    def __init__(self, new_save):
        super().__init__()
        self.minsize(370, 100)
        self.maxsize(370, 550)

        # open screen centered
        w = 370
        h = 500
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y-35))

        self.title("Save2Switch new save.")
        configs_frame = newSaveConfig(master=self)
        configs_frame.pack(fill="both", expand=True)
        configs_frame.create_itens(new_save)
