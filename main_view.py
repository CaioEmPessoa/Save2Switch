import customtkinter as ctk 
from PIL import Image
import os

class Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

class GamesFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        for s in range(0, 20, 4):
            my_frame = Frame(master=self, border_width=3, border_color="gray", width=550)
            
            border_label = ctk.CTkLabel(master=my_frame, text="")
            border_label.grid(row=0, column=0)

            game_name_label = ctk.CTkLabel(master=my_frame, font=('', 30), text="Disco Elysium", 
                                        justify="center", width=500)
            game_name_label.grid(row=s+1, column=0, columnspan=3, padx=24)

            question_where_label = ctk.CTkLabel(master=my_frame, font=('', 20), 
                                text="Copy save to?", justify="center", text_color="grey")
            question_where_label.grid(row=s+2, column=1)

            my_image = ctk.CTkImage(light_image=Image.open("img/disco.jpg"), size=(130, 130))
            img_label = ctk.CTkLabel(master=my_frame, image=my_image, text="")
            img_label.grid(row=s+3, column=1, pady=20)

            switch_button = ctk.CTkButton(master=my_frame, text="switch", width=120, height=50, font=('', 25),
                                        fg_color=("#1f6aa5", "#2a2b2a"), border_color="#1f6aa5", border_width=2, corner_radius=15)
            switch_button.grid(row=s+3, column=0, pady=15)

            pc_button = ctk.CTkButton(master=my_frame, text="pc", width=120, height=50, font=('', 25),
                                    fg_color=("#1f6aa5", "#2a2b2a"), border_color="#1f6aa5", border_width=2, corner_radius=15)
            pc_button.grid(row=s+3, column=2, pady=15)

            my_frame.grid(row=s, column=0, columnspan=2, rowspan=3, pady=20)

class Root(ctk.CTk):
    def CreateWindow(self, init):

        # WINDOW CONFIG <----------------------------<
        self.title('Save2Switch')
        self.minsize(430, 300)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        #  >-------------------------------------> END
        
        welcome = ctk.CTkLabel(master=self, text="Escolha um ou adicione um novo save de jogo", 
                               font=('Segoe UI', 20), text_color="#807e7e", width=500, pady=15)
        welcome.grid(row=0, column=0, columnspan=3)

        self.games_frame = GamesFrame(master=self, fg_color="transparent",
                                width=550, height=600, corner_radius=0)
        self.games_frame.grid(row=1, column=0, padx=10,
                           columnspan=3, sticky="nsew")


        # BUTTONS <------------------------------------------------------------<
        add_button = ctk.CTkButton(master=self, text=" + ", width=70, 
                                   command=lambda: init.call_new_save_window())
        add_button.grid(row=99, column=0, 
                        padx=10, pady=10, sticky="E",)

        edit_button = ctk.CTkButton(master=self, text="Edit/Reset view for debug", width=70,
                                    command=lambda: init.call_window("restart"))
        edit_button.grid(row=99, column=1, pady=10)

        theme_buttom = ctk.CTkButton(master=self, text="Theme", width=70, command=self.switch_theme)
        theme_buttom.grid(row=99, column=2, padx=10, pady=10, sticky="W")
        # >----------------------------------------------------------------> END

    def switch_theme(self):
        try:
            print(self.tema)
        except:
            self.tema = "Dark"
        
        # If the theme is dark it switches it to light and vice-versa
        if self.tema == "Dark":
            theme_data = {"tema": "Dark"}
            #self.write_data(theme_data)
            self.tema = "Light"

        elif self.tema == "Light":
            theme_data = {"tema": "Light"}
            #self.write_data(theme_data)

            self.tema = "Dark"

        ctk.set_appearance_mode(self.tema)
