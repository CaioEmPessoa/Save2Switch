import customtkinter as ctk 
from tkinter import messagebox
from PIL import Image

class Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

class GamesFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

    def create_save_frames(self, main):
        saves_data = main.modify_data.data["saves"]
        
        pos = 0
        for save in saves_data:

            game_name = saves_data[save]["name"]
            icon_path = saves_data[save]["icon_path"]

            my_frame = Frame(master=self, border_width=3, border_color="gray", width=550)
            
            border_label = ctk.CTkLabel(master=my_frame, text="")
            border_label.grid(row=0, column=0)

            game_name_label = ctk.CTkLabel(master=my_frame, font=('', 30), text=game_name, 
                                        justify="center", width=500)
            game_name_label.grid(row=pos+1, column=0, columnspan=3, padx=24)

            question_where_label = ctk.CTkLabel(master=my_frame, font=('', 20), 
                                text="Copy save to?", justify="center", text_color="grey")
            question_where_label.grid(row=pos+2, column=1)

            if icon_path != "":
                my_image = ctk.CTkImage(light_image=Image.open(icon_path), size=(130, 130))
                img_label = ctk.CTkLabel(master=my_frame, image=my_image, text="", corner_radius=100)
                img_label.grid(row=pos+3, column=1, pady=20)

            switch_button = ctk.CTkButton(master=my_frame, text="switch", width=120, height=50,
                                          command=lambda game=game_name: main.connect_switch.save2switch(game),
                                          font=('', 25), fg_color=("#1f6aa5", "#2a2b2a"), 
                                          border_color="#1f6aa5", border_width=2, corner_radius=15)
            switch_button.grid(row=pos+3, column=0, pady=15)

            pc_button = ctk.CTkButton(master=my_frame, text="pc", width=120, height=50, 
                                      command=lambda game=game_name: main.connect_switch.save2pc(game),
                                      font=('', 25), fg_color=("#1f6aa5", "#2a2b2a"), 
                                      border_color="#1f6aa5", border_width=2, corner_radius=15)
            pc_button.grid(row=pos+3, column=2, pady=15)

            my_frame.grid(row=pos, column=0, columnspan=2, rowspan=3, pady=20)
            
            pos += 4

class Root(ctk.CTk):
    def CreateWindow(self, main):

        # WINDOW CONFIG <----------------------------<
        self.title('Save2Switch')
        self.minsize(430, 300)
        self.grid_rowconfigure((1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        w = 600 
        h = 750 
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        #  >-------------------------------------> END
        
        self.welcome = ctk.CTkLabel(master=self, text="Choose or add a new save game", 
                               font=('Segoe UI', 20), text_color="#807e7e", width=500, pady=15)
        self.welcome.grid(row=0, column=0, columnspan=4)

        self.games_frame = GamesFrame(master=self, fg_color="transparent",
                                width=550, height=600, corner_radius=0)
        self.games_frame.grid(row=1, column=0, padx=10,
                           columnspan=4, sticky="nsew")


        # BUTTONS <------------------------------------------------------------<
        add_button = ctk.CTkButton(master=self, text=" + ", width=70, 
                                   command=lambda: main.call_window("new_save"))
        add_button.grid(row=99, column=0, 
                        padx=10, pady=10, sticky="E",)

        edit_button = ctk.CTkButton(master=self, text="Edit", width=70,
                                    command=lambda: main.call_window("restart"))
        edit_button.grid(row=99, column=1, pady=10)

        theme_buttom = ctk.CTkButton(master=self, text="Theme", width=70, command=main.switch_theme)
        theme_buttom.grid(row=99, column=2, padx=10, pady=10, sticky="W")
        
        config_icon = ctk.CTkImage(light_image=Image.open("img/config_light.png"), dark_image=Image.open("img/config_dark.png"), size=(30, 30))

        config_button = ctk.CTkButton(master=self, text="", width=30, 
                                      image=config_icon, fg_color="transparent",
                                      command=lambda: main.call_window("config"))
        config_button.grid(row=99, column=3, padx=10, pady=10, sticky="W")
        # >----------------------------------------------------------------> END

        if main.data["switch_ip"] == "0.0.0.0":
            add_button.configure(fg_color="red", state="disabled")
            self.welcome.configure(text="Please configure your switch IP.")
            #self.tutorial(main)

        try:
            self.games_frame.create_save_frames(main)
        except:
            print("no saves")

    def tutorial(self, main):
        #tutorials like this don't work??
        tour = messagebox.askyesno(title="Tutorial", message="It seems this is your first time here, do you want a tutorial?")
        if tour:
            messagebox.showinfo(title="+ Button", message="The '+' button is where you add new game saves, it is red now because you first need to configure some things.")
            messagebox.showinfo(title="Edit Button", message="The 'edit' button lets you edit or delete your already made saves, if you changed your save foulder, or want to change the icon of the game, you can make this changes here.")
            messagebox.showinfo(title="Theme Button", message="The 'theme' button lets you change the theme of the app from light to dark and the other way around.")
            messagebox.showinfo(title="Config Button", message="The config button should be the first button to press, here is where you config your switch ip, port, username and such... We will open the tab of it now.")
            main.call_window("config")
            messagebox.showinfo(title="Configurating...", message="First you can open a server on your switch, there you can check your IP and Port.")
            messagebox.showinfo(title="Configurating...", message="Then you can put a custom username and password to connect to your switch, but I DO NOT RECOMMEND doing that, it is probably the default one, so change only IF YOU KNOW WHAT YOU ARE DOING.")
            main.call_window("restart")
            messagebox.showinfo(title="End", message="Ok, I think that's it for the tutorial! The part of adding a app and actually copying saves is much simpler and you can do it by intuition, but if you have any trouble doing so. But if you have >any< trouble with the app, I recommend reporting it to my github, thanks!")
            main.call_window("restart")
        else:
            return