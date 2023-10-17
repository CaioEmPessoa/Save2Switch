import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import shutil

class NewSaveView(ctk.CTkToplevel):
    def __init__(self, newsave_src):
        super().__init__()

        # Buttons, Labels and Entrys
        # LABELS
        self.name_label = ctk.CTkLabel(master=self, justify="left", text="Choose the name of the game:")
        self.name_label.grid(row=0, column=0, padx=10, columnspan=3, sticky="W")

        self.pc_path_label = ctk.CTkLabel(master=self, text="Select the path to the PC save foulder:")
        self.pc_path_label.grid(row=3, column=0, padx=10, columnspan=2, sticky="W")

        self.switch_path_label = ctk.CTkLabel(master=self, text="Select the path to the Switch save foulder:")
        self.switch_path_label.grid(row=7, column=0, padx=10, columnspan=2, sticky="W")
        # END Labels

        # ENTRY
        self.name_entry = ctk.CTkEntry(master=self, width=200)
        self.name_entry.grid(row=1, column=0, 
                        pady=10, padx=10, sticky="W", columnspan=3)

        self.pc_path_entry = ctk.CTkEntry(master=self)
        self.pc_path_entry.grid(row=4, column=0, 
                        pady=10, padx=10, sticky="W")

        self.switch_path_entry = ctk.CTkEntry(master=self)
        self.switch_path_entry.grid(row=8, column=0, pady=10, padx=10, sticky="W")
        # END Entry

        # Buttons
        self.pc_window_button = ctk.CTkButton(master=self, text="Janela", width=10, 
                                    command=lambda: newsave_src.search_window("pc"))
        self.pc_window_button.grid(row=4, column=1, sticky="W")

        self.switch_window_button = ctk.CTkButton(master=self, text="Janela", width=10, 
                                    command=lambda: newsave_src.search_window("switch"))
        self.switch_window_button.grid(row=8, column=1, sticky="W")

        self.send_button = ctk.CTkButton(master=self, command=lambda: newsave_src.send(), text="Concluir")
        self.send_button.grid(row=9, pady=15, columnspan=2)
        # END Buttons