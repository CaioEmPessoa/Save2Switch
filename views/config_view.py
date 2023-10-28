import customtkinter as ctk

class NewSaveView(ctk.CTkToplevel):
    def __init__(self, new_save):
        super().__init__()
        self.minsize(230, 260)
        self.grid_rowconfigure((list(range(12))), weight=2)
        self.grid_columnconfigure((list(range(3))), weight=2)

        teste = ctk.CTkLabel(master=self, text="TESTE")
        teste.grid(row=0, column=0)