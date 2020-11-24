"""
    Page depends on tkinter
"""
from tkinter import Frame


class Page(Frame):
    """
        Page is a subclass of a tkinter frame.
        Its purpose is to be able to create a
        frame where widgets easily can be removed
    """

    def __init__(self, **kw):
        super().__init__(**kw)

    def clear(self):
        """
            Loop through the frame's widgets
            and destroy them
        """
        for w in self.winfo_children():
            w.destroy()
