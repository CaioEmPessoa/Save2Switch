import customtkinter as ctk

class NewSaveView(ctk.CTkToplevel):
    def __init__(self, new_save):
        super().__init__()
        self.minsize(230, 260)
        self.grid_rowconfigure((list(range(12))), weight=2)
        self.grid_columnconfigure((list(range(3))), weight=2)

        # Buttons, Labels and Entrys
        # LABELS
        self.config_label = ctk.CTkLabel(master=self, text="Remember to config your switch address on the config tab\nit is the far right icon on the main page")
        self.config_label.grid(row=0, column=0, columnspan=3, sticky="W", pady=10, padx=10)

        self.name_label = ctk.CTkLabel(master=self, justify="left", text="The name of the game:")
        self.name_label.grid(row=1, column=0, padx=10, columnspan=3, sticky="W")

        self.switch_path_label = ctk.CTkLabel(master=self, text="Whats the game on the JKSV foulder?")
        self.switch_path_label.grid(row=4, column=0, padx=10, columnspan=2, sticky="W")

        self.pc_path_label = ctk.CTkLabel(master=self, text="The path to the PC foulder/file:")
        self.pc_path_label.grid(row=8, column=0, padx=10, columnspan=2, sticky="W")

        self.image_path_label = ctk.CTkLabel(master=self, text="Optional: Path to the preview image:")
        self.image_path_label.grid(row=10, column=0, padx=10, columnspan=2, sticky="W")

        self.wanring = ctk.CTkLabel(master=self, text="")
        self.wanring.grid(row=13, column=0, columnspan=2, sticky="EW")
        # END Labels

        # ENTRY
        self.name_entry = ctk.CTkEntry(master=self, width=200)
        self.name_entry.grid(row=2, column=0, pady=10, padx=10, sticky="W", columnspan=3)

        self.pc_path_entry = ctk.CTkEntry(master=self)
        self.pc_path_entry.grid(row=9, column=0, pady=10, padx=10, sticky="W")
        
        self.switch_path_entry = ctk.CTkEntry(master=self)
        self.switch_path_entry.grid(row=5, column=0, pady=10, padx=10, sticky="W")

        self.image_path_entry = ctk.CTkEntry(master=self)
        self.image_path_entry.grid(row=11, column=0, pady=10, padx=10, sticky="W")
        # END Entry

        # Buttons
        self.pc_window_button = ctk.CTkButton(master=self, text="Window", width=10, 
                                    command=lambda: new_save.search_windows(self.pc_path_entry))
        self.pc_window_button.grid(row=9, column=1, sticky="W")

        self.image_window_button = ctk.CTkButton(master=self, text="Window", width=10, 
                                    command=lambda: new_save.search_windows(self.image_path_entry))
        self.image_window_button.grid(row=11, column=1, sticky="W")

        self.checkbox_label = ctk.CTkLabel(master=self, text="Foulder Mode for Window button:")
        self.checkbox_label.grid(row=12, column=0, pady=15, padx=10)

        self.checkbox = ctk.CTkCheckBox(master=self, text="")
        self.checkbox.grid(row=12, column=1, pady=15)

        self.send_button = ctk.CTkButton(master=self, command=lambda: new_save.send(), text="Concluir")
        self.send_button.grid(row=13, pady=15)
        # END Buttons