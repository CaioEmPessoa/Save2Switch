import ftplib

class connectFTP():
    def __init__(self, main):
        super().__init__()

    def connect(self, switchip, username, password):
        HOSTNAME = switchip
        USERNAME = username
        PASSWORD = password

        self.switch_connect = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

    def copy_save(self, src, dst):
        # Read file in binary mode
        with open(src, "rb") as file:
            # Command for Uploading the file "STOR filename"
            self.switch_connect.storbinary(f"STOR {dst}", file)