from tkinter import Frame


class Page(Frame):

    def __init__(self, **kw):
        super().__init__(**kw)

    def clear(self):
        for w in self.winfo_children():
            w.destroy()