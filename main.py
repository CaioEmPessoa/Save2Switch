import customtkinter as ctk
from PIL import Image
import os

from main_view import Root
from new_save import new_save
from new_save import new_save_view

class CopySave():
    def __init__(self):
        super().__init__()

    def copy_save(switch_location, pc_location):
        print("test")

    def clear_data(self, init):
        for item in os.listdir("img"):
            if item != "unknown.png":
                os.remove("img/" + item)
        os.remove("apps_data.json")
                
        init.call_window("close")
        init.call_window("restart")

    def edit_saves(self, init):
        if init.changing == 0:
            init.changing = 1
            for button in init.created_buttons:
                button.configure(border_color="red", 
                                 command=lambda app=init.names_list[init.created_buttons.index(button)]: 
                                 init.call_edit_window(app))

        else:
            init.changing = 0
            for button in init.created_buttons:
                button.configure(border_color="#1f6aa5", 
                                 command=lambda app=init.path_list[init.created_buttons.index(button)]: 
                                 self.open_app(init, app))

    def call_new_save_window(self):
        self.add_save = new_save.NewSave()
        self.add_save.create_newsave_window(self, new_save_view)
        self.add_save.grab_set()

    def call_window(self, window):
        match window:
            case "restart":
                # not working dk why
                copysave = CopySave()

            case "close":
                main_view.destroy()

'''
    >>> ALL OF THIS WILL BE CHANGED

    def app_buttons(self, init):
        for item in range(0, init.list_number): # Loop around the list of app names and create apps with their names.
            app_button = ctk.CTkButton(master=self.my_frame, width=70, text=init.names_list[item], compound="top",
                                    command=lambda app=init.path_list[item]: self.open_app(init, app),
                                    text_color="#807e7e", fg_color="transparent", border_color="#1f6aa5", border_width=2.5, hover_color="#184c74")
            app_button.grid(row=init.row, column=init.column, pady=10, padx=5)

            init.created_buttons.append(app_button)

            # coloca imagem do ícone ao lado do nome do app caso esteja salvo alguma imagem no json

            if init.icon_list[item] != "None":
                icon = ctk.CTkImage(light_image=Image.open(init.icon_list[item]),size=(150, 150))
                app_button.configure(image=icon)

            # Change the pos of the buttons
            init.column += 1
            if init.column == 3:
                init.column = 0
                init.row += 3
'''
if __name__ == "__main__":
    copysave = CopySave()

    main_view = Root()
    main_view.CreateWindow(copysave)
    main_view.mainloop()