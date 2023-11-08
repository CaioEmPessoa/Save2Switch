import ftplib
import datetime
import shutil
import os

class connectFTP():
    def __init__(self, main):
        super().__init__()

        self.main = main
        self.today = datetime.datetime.now().strftime("%d.%m.%Y")
        self.today_precise = datetime.datetime.now().strftime("%d.%m.%Y - %H;%M;%S")
        
    def connect(self, game_name):
        self.game = self.main.data["saves"][game_name]
        self.pc_path = self.game["pc_path"]
        match self.main.data["save_app"]:
            case "JKSV":
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
                
                print('CWD ', self.switch_path)
                self.switch_connect.cwd(self.switch_path)
                print('CWD ', "OK!")

            except:
                self.main.main_view.welcome.configure(text="Error connecting to FTP server.\nCheck your FTP info and if the server is opened.", 
                                                      text_color="Black")
                raise

    def download_tree(self, src, dst):       
        print("CWD ", src)
        self.switch_connect.cwd(src)

        src_list = [os.path.basename(file) for file in self.switch_connect.nlst()]
        dst_list = os.listdir(dst)
        # try, if path not exist, create the src foulder|^|

        for file in src_list:
            try:
                self.switch_connect.cwd(file)
                self.switch_connect.cwd("..")
                isfile = False
            except:
                isfile = True
            

            if isfile:
                dst_file = os.path.join(dst, file)
                if file in dst_list:
                    os.remove(dst_file)

                print("RETR ", file)
                self.switch_connect.retrbinary("RETR " + file, open(dst_file, 'wb').write)

            elif not isfile:
                print("LOCAL: MKDIR", file)
                self.download_tree(file, os.path.join(dst, file))
                self.switch_connect.cwd("..")
            
            else:
                print("???")

    def upload_tree(self, src):
        for file in os.listdir(src):
            localpath = f"{src}/{file}"
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

                self.upload_tree(localpath)
                
                print("CWD", "..")
                self.switch_connect.cwd("..")

    def save2switch(self, game_name):
        self.connect(game_name)

        print('CWD ', self.switch_path)
        self.switch_connect.cwd(self.switch_path)
        print('CWD ', "OK!")
        
        new_dir_name = "Save2Switch Copy - " + self.today

        try:
            print('MKD ', new_dir_name)
            self.switch_connect.mkd(new_dir_name)
            print('MKD ', "OK!")
        except ftplib.error_perm:
            self.today_precise = datetime.datetime.now().strftime("%d.%m.%Y - %H;%M;%S")
            new_dir_name = "Save2Switch Copy - " + self.today_precise
            print('MKD ', new_dir_name)
            self.switch_connect.mkd(new_dir_name)
            print('MKD ', "OK!")
            pass

        print('CWD ', new_dir_name)
        self.switch_connect.cwd(new_dir_name)

        self.upload_tree(self.pc_path)
        self.switch_connect.quit()

    def save2pc(self, game_name):
        self.connect(game_name)
        src = self.game["switch_foulder"]
        dst = self.game["pc_path"]

        # PC SAVE BACKUP <-----------------------------------------------------
        backhup_foulder = f"{os.getcwd()}\\backups\\{self.game['name']} backup - {self.today}"
        
        try:
            os.mkdir(backhup_foulder)
        except FileExistsError:
            self.today_precise = datetime.datetime.now().strftime("%d.%m.%Y - %H;%M;%S")
            backhup_foulder = f"{os.getcwd()}\\backups\\{self.game['name']} backup - {self.today_precise}"
            os.mkdir(backhup_foulder)

        for file in os.listdir(dst):
            file_path = f"{dst}/{file}"
            if os.path.isfile(file_path):
                shutil.copy(file_path, backhup_foulder)
            elif os.path.isdir(file_path):
                shutil.copytree(file_path, f"{backhup_foulder}\\{file}")

        # >------------------------------------------------------------------------> END BACKUP

        self.download_tree(src, dst)
