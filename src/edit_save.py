class Root(ctk.CTk):
    def EditWindow(self, main, save):
        save_data = main.data["saves"][save]
        main.call_window("new_save")
        main.add_save.name_entry.insert(save_data["name"])