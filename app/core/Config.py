class Config:
    path_to_current_notebook: str = "app/resources/note.csv"
    path_to_config: str = "app/core/config.ini"

    def set_path_to_resources(self, new_path: str):
        self.path_to_current_notebook = new_path

    def set_path_to_config(self, new_path):
        self.path_to_config = new_path

    def get_path_to_resources(self):
        return self.path_to_current_notebook

    def get_path_to_config(self):
        return self.path_to_config

    def read_config(self):
        pass