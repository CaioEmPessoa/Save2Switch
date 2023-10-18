import customtkinter as ctk 
from PIL import Image
import os

class Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class GamesFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


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

            my_image = ctk.CTkImage(light_image=Image.open("disco.jpg"), size=(130, 130))
            img_label = ctk.CTkLabel(master=my_frame, image=my_image, text="")
            img_label.grid(row=s+3, column=1, pady=20)

            switch_button = ctk.CTkButton(master=my_frame, text="switch", width=120, height=50, font=('', 25),
                                        fg_color="transparent", border_color="#1f6aa5", border_width=2, corner_radius=15)
            switch_button.grid(row=s+3, column=0, pady=15)

            pc_button = ctk.CTkButton(master=my_frame, text="pc", width=120, height=50, font=('', 25),
                                    fg_color="transparent", border_color="#1f6aa5", border_width=2, corner_radius=15)
            pc_button.grid(row=s+3, column=2, pady=15)

            my_frame.grid(row=s, column=0, columnspan=2, rowspan=3, pady=20)

class Root(ctk.CTk):
    def CreateWindow(self, init):
        
        # WELCOME LABEL ------------------------------------<
        welcome = ctk.CTkLabel(master=self, text="Escolha um ou adicione um novo save de jogo", 
                               font=('Segoe UI', 20), text_color="#807e7e", width=500, pady=15)
        welcome.grid(row=0, column=0, columnspan=3)
        # -----------------------------------------------> END

        # Calls the app buttons to generate them. ------------------------------<

        self.games_frame = GamesFrame(master=self, fg_color="transparent",
                                width=550, height=600, corner_radius=0)
        self.games_frame.grid(row=1, column=0, padx=10,
                           columnspan=3, sticky="nsew")


        # Generate the last button, an "add more" one.
        add_button = ctk.CTkButton(master=self, text=" + ", width=70, 
                                   command=lambda: init.call_new_save_window())
        add_button.grid(row=99, column=0, 
                        padx=10, pady=10, sticky="E",)

        edit_button = ctk.CTkButton(master=self, text="Editar", width=70,
                                    command=lambda: init.call_window("restart"))
        edit_button.grid(row=99, column=1, pady=10)

        theme_buttom = ctk.CTkButton(master=self, text="Tema", width=70,)
        theme_buttom.grid(row=99, column=2, 
                          padx=10, pady=10, sticky="W")

        # >---------------------------------------------------------------- END
