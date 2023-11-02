import customtkinter as ctk

class NewSaveView(ctk.CTkToplevel):
    def __init__(self, new_save):
        super().__init__()
        size = 420

        # open screen centered
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws/2) - (size/2)
        y = (hs/2) - (size/2)
        self.geometry('%dx%d+%d+%d' % (size, size, x, y-80))

        self.maxsize(size, size)
        self.minsize(size, size)

        self.grid_columnconfigure(0, weight=2)
        self.grid_rowconfigure((list(range(7))), weight=2)
        self.title("Save2Switch Config")

        self.switch_ip_label = ctk.CTkLabel(master=self, text="What is your switch's ip? (it may change)", font=('',16))
        self.switch_ip_label.grid(row=0, column=0)

        self.switch_ip_entry = ctk.CTkEntry(master=self, width=200, font=('',16))
        self.switch_ip_entry.grid(row=1, column=0)

        self.switch_port_label = ctk.CTkLabel(master=self, text="\nWhat is your switch's port?", font=('',16))
        self.switch_port_label.grid(row=2, column=0)

        self.switch_port_entry = ctk.CTkEntry(master=self, width=200, font=('',16))
        self.switch_port_entry.grid(row=3, column=0)

        self.ftp_app_label = ctk.CTkLabel(master=self, text="\nWhat save app do you use on Switch?", font=('',16))
        self.ftp_app_label.grid(row=4, column=0)

        self.save_app_select = ctk.CTkOptionMenu(master=self, values=["JKSV", "Edizon"], width=200, font=('',16),
                                        fg_color="White", text_color="Black", button_color=("#969da3", "#565a5f"))
        self.save_app_select.grid(row=5, column=0)
        
        self.ftp_username_label = ctk.CTkLabel(master=self, text="\nOptional: FTP username:", font=('',16))
        self.ftp_username_label.grid(row=6, column=0)

        self.ftp_username_entry = ctk.CTkEntry(master=self, width=200, font=('',16))
        self.ftp_username_entry.grid(row=7, column=0)

        self.ftp_password_label = ctk.CTkLabel(master=self, text="\nOptional: FTP password:", font=('',16))
        self.ftp_password_label.grid(row=8, column=0)

        self.ftp_password_entry = ctk.CTkEntry(master=self, width=200, font=('',16))
        self.ftp_password_entry.grid(row=9, column=0)

        self.send_button = ctk.CTkButton(master=self, text="Confirm", font=('',16),
                                    command=new_save.get_config_info)
        self.send_button.grid(row=10, column=0, pady=15)

        self.wanring = ctk.CTkLabel(master=self, text="")
        self.wanring.grid(row=11, column=0, sticky="EW")

        # DEFAULT VALUES
        self.switch_ip_entry.insert(0, new_save.main.data["switch_ip"])
        self.switch_port_entry.insert(0, new_save.main.data["switch_port"])
        self.save_app_select.set(new_save.main.data["save_app"])
        self.ftp_username_entry.insert(0, new_save.main.data["username"])
        self.ftp_password_entry.insert(0, new_save.main.data["password"])