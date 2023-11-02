import ftplib
import datetime
import shutil
import os

class connectFTP():
    def __init__(self, main):
        super().__init__()

        self.main = main
        self.today = datetime.datetime.now().strftime("%d.%m.%Y")
        
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
                print(self.switch_connect.nlst())

            except:
                self.main.main_view.welcome.configure(text="Error connecting to FTP server.\nCheck your FTP info and if the server is opened.", 
                                                      text_color="Black")
                

    def save2switch(self, game_name):
        self.connect()
        game = self.main.data["saves"][game_name]
        src = game["pc_path"]

        match self.main.data["save_app"]:
            case "JKSV":
                dst = f"/JKSV/{game['switch_path']}/"
            case "EdiZon":
                dst = f"/switch/EdiZon/saves/{game['switch_path']}/"

        # change work directory
        self.switch_connect.cwd(dst)
        
        new_dir_name = "Save2Switch Copy - " + self.today
        print(new_dir_name)
        try:
            self.switch_connect.mkd(new_dir_name)
        except:
            pass

        if os.path.isfile(src):
            file_name = os.path.basename(src)
            with open(src, "rb") as file:
                self.switch_connect.storbinary(f"STOR {new_dir_name}/{file_name}", file)
        elif os.path.isdir(src):
            save_files = os.listdir(src)
            for file in save_files:
                file_name = os.path.basename(file)
                print(file_name)
                with open(src, "rb") as file:
                    self.switch_connect.storbinary(f"STOR {new_dir_name}/{file_name}", file)

        
        self.switch_connect.quit()

    def save2pc(self, game_name):
        game = self.main.data["saves"][game_name]
        src = f"{game['switch_path']}/{game['switch_foulder']}"
        dst = game["pc_path"]

        # could be more effective,
        # bring this code to __init_
        backhup_foulder = f"{dst}/../save2pc save_backup - {self.time}"
        os.mkdir(backhup_foulder) 

        match self.main.data["save_app"]:
            case "JKSV":
                src = f"/JKSV/{game['switch_path']}/"
            case "EdiZon":
                src = f"/switch/EdiZon/saves/{game['switch_path']}/"

        self.switch_connect.quit()
