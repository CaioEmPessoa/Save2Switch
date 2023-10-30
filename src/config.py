class Config():
    def create_config_window(self, main, config_view):
        self.main = main
        self.config_view = config_view.NewSaveView(self)
        self.config_view.grab_set()

    def get_config_info(self):
        self.switch_ip = self.config_view.switch_ip_entry.get()
        self.save_app = self.config_view.save_app_select.get()

        self.ftp_username = self.config_view.ftp_username_entry.get()
        self.ftp_password = self.config_view.ftp_password_entry.get()

        if self.switch_ip == "":
            self.config_view.wanring.configure(fg_color="#b60000", text="Please put your switch IP.")
            return
        if self.ftp_username == "":
            self.ftp_username = "anonymous"

        self.config_data = {
            "switch_ip": self.switch_ip,
            "save_app": self.save_app,
            "username": self.ftp_username,
            "password": self.ftp_password
        }

        self.main.modify_data.write_data(self.config_data)
        self.config_view.destroy()
