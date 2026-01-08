import tkinter as tk
from windows.main_window import MainWindow

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    MainWindow(root)
    root.deiconify()   
    root.mainloop()
