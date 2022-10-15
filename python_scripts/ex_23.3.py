import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("200x200")
        self.main_window.title("NYUAD Address")

        self.button = tkinter.Button(self.main_window, text="NYUAD Address", command = self.show_address)
        self.button.pack(expand=True)

        tkinter.mainloop()

    def show_address(self):
        tkinter.messagebox.showinfo("NYUAD Address", "Exit 11")

my_gui = MyGUI()