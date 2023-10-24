
def connect(self, switchip, username, password):
    HOSTNAME = switchip
    USERNAME = username
    PASSWORD = password

    self.switch_connect = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

def copy(self, file_path):
    file_path = "gfg.txt"
    
    # Read file in binary mode
    with open(file_path, "rb") as file:
        # Command for Uploading the file "STOR filename"
        self.switch_connect.storbinary(f"STOR {file_path}", file)