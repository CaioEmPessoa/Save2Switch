import ftplib

class connectFTP():
    def __init__(self, main):
        super().__init__()

        self.main = main
        
    def connect(self):
        if self.main.data["switch_ip"] != "0.0.0.0":
            try:
                HOSTNAME = self.main.data["switch_ip"]
                PORT = int(self.main.data["switch_port"])
                USERNAME = self.main.data["username"]
                PASSWORD = self.main.data["password"]

                self.switch_connect = ftplib.FTP()
                self.switch_connect.connect(HOSTNAME, PORT)
                self.switch_connect.login(USERNAME, PASSWORD)
                print(self.switch_connect.getwelcome())

            except:
                self.main.main_view.welcome.configure(text="Error connecting to FTP server.\nCheck your FTP info and if the server is opened.", 
                                                      text_color="Black")

    def save2switch(self, game):
        self.connect()
        game = self.main.data["saves"][game]
        src = game["pc_path"]
        dst = game["switch_path"]

        # Read file in binary mode
        with open(src, "rb") as file:
            # Command for Uploading the file "STOR filename"
            self.switch_connect.storbinary(f"STOR {dst}", file)

    def save2pc(self, game):
        self.connect()
        game = self.main.data["saves"][game]
        src = game["pc_path"]
        dst = game["switch_path"]

        # Read file in binary mode
        with open(src, "rb") as file:
            # Command for Uploading the file "STOR filename"
            self.switch_connect.storbinary(f"STOR {dst}", file)

