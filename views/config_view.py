import customtkinter as ctk

class NewSaveView(ctk.CTkToplevel):
    def __init__(self, new_save):
        super().__init__()
        self.minsize(230, 260)
        self.grid_rowconfigure((list(range(12))), weight=2)
        self.grid_columnconfigure((list(range(3))), weight=2)

        switch_ip_label = ctk.CTkLabel(master=self, text="What is your switch's ip?")
        switch_ip_label.grid(row=0, column=0)

        switch_ip_entry = ctk.CTkEntry(master=self)
        switch_ip_entry.grid(row=1, column=0)

        ftp_app = ctk.CTkComboBox(master=self, values=["JKSV", "Edizon"])
        ftp_app.grid(row=2, column=0)