import customtkinter as ctk 
from PIL import Image
import os

class MyFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class Root(ctk.CTk):
    def CreateWindow(self, init):
        
        # WELCOME LABEL ------------------------------------<
        welcome = ctk.CTkLabel(master=self, text="Escolha um ou adicione um novo atalho", 
                               font=('Segoe UI', 20), text_color="#807e7e", width=500)
        welcome.grid(row=0, column=0, columnspan=3)
        # -----------------------------------------------> END

        # Calls the app buttons to generate them. ------------------------------<

        self.my_frame = MyFrame(master=self, fg_color="transparent",
                                width=550, height=600, corner_radius=0)
        self.my_frame.grid(row=1, column=0, padx=10,
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
