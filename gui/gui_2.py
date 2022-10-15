import tkinter

class myGUI:
	def __init__(self):
		self.main_window = tkinter.Tk()

		self.top_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

		self.label1 = tkinter.Label(self.top_frame, text = "Winken")
		self.label2 = tkinter.Label(self.top_frame, text = "Blinken")
		self.label3 = tkinter.Label(self.top_frame, text = "Nod")

		self.label1.pack()
		self.label2.pack()
		self.label3.pack()

		self.top_frame.pack()

		self.label4 = tkinter.Label(self.bottom_frame, text = "Winken")
		self.label5 = tkinter.Label(self.bottom_frame, text = "Blinken")
		self.label6 = tkinter.Label(self.bottom_frame, text = "Nod")

		self.label4.pack(side = "left")
		self.label5.pack(side = "left")
		self.label6.pack(side = "left")

		self.bottom_frame.pack()

		tkinter.mainloop()

myGUI = myGUI()