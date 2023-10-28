class Config():
    def create_config_window(self, main, config_view):
        self.main = main

        self.config_view = config_view.NewSaveView(self)
        self.config_view.grab_set()