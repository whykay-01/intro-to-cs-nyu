import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.km_label = tkinter.Label(self.top_frame, text="Enter distance in km: ")
        self.km_entry = tkinter.Entry(self.top_frame, width=10)

        self.km_label.pack(side="left")
        self.km_entry.pack(side="left")

        self.result_label1 = tkinter.Label(self.middle_frame, text="Converted to miles: ")
        self.result = tkinter.StringVar()
        self.result_label2 = tkinter.Label(self.middle_frame, textvariable=self.result)

        self.result_label1.pack(side="left")
        self.result_label2.pack(side="left")

        self.button = tkinter.Button(self.bottom_frame, text="Convert", command=self.convert)
        self.button.pack()

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        km = float(self.km_entry.get())
        miles = km * 0.6214
        # miles = int(miles * 100)/100
        miles = round(miles, 2)
        # tkinter.messagebox.showinfo("Result", str(km) + " km is equal to " + str(miles) + " miles")
        self.result.set(str(miles))

my_gui = MyGUI()