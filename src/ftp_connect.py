import ftplib
import datetime
import shutil
import os

class connectFTP():
    def __init__(self, main):
        super().__init__()

        self.main = main
        self.today = datetime.datetime.now().strftime("%d.%m.%Y")
        
    def connect(self, game_name):
        self.game = self.main.data["saves"][game_name]
        self.pc_path = self.game["pc_path"]
        match self.main.data["save_app"]:
            case "JKSV":
                "Save2Switch Copy - " + self.today
                self.switch_path = f"/JKSV/{self.game['switch_path']}/"
            case "EdiZon":
                self.switch_path = f"/switch/EdiZon/saves/{self.game['switch_path']}/"

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
                raise

    def save2switch(self, game_name):
        self.connect(game_name)
        src = self.pc_path

        print('CWD ', self.switch_path)
        self.switch_connect.cwd(self.switch_path)
        print('CWD ', "OK!")
        
        new_dir_name = "Save2Switch Copy - " + self.today

        try:
            print('MKD ', new_dir_name)
            self.switch_connect.mkd(new_dir_name)
            print('MKD ', "OK!")
        except ftplib.error_perm:
            print('MKD ', "OK!")
            pass

        print('CWD ', new_dir_name)
        self.switch_connect.cwd(new_dir_name)

        for file in os.listdir(src):
            localpath = f"{src}/{file}"
            print(self.switch_connect.nlst())
            if os.path.isfile(localpath):
                print("STOR", localpath, file)
                self.switch_connect.storbinary('STOR ' + file, open(localpath,'rb'))
            elif os.path.isdir(localpath):
                print("MKD", file)
                try:
                    self.switch_connect.mkd(file)

                # ignore "directory already exists"
                except:
                    pass
                
                print("CWD", file)
                self.switch_connect.cwd(file)

                self.copy_tree(localpath)
                
                print("CWD", "..")
                self.switch_connect.cwd("..")
                
        self.switch_connect.quit()

    def save2pc(self, game_name):
        game = self.main.data["saves"][game_name]
        src = f"{game['switch_path']}\\{game['switch_foulder']}"
        dst = game["pc_path"]
        backhup_foulder = f"{os.getcwd()}\\backups\\{game['name']} backup - {self.today}"
        
        try:
            os.mkdir(backhup_foulder)
        except FileExistsError:
            pass

        for file in os.listdir(dst):
            shutil.copy(f"{dst}\\{file}", backhup_foulder)

        save_files = self.switch_connect.nlst()


