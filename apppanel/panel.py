import customtkinter as ctk

# Simple class for making top level windows, nothing more

class Panel(ctk.CTkToplevel):
    def __init__(self, width, height, title) -> None:
        super().__init__()
        self.geometry = "{width}x{height}"
        self.title(title)
        