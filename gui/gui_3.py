import tkinter
import tkinter.messagebox


class myGUI:
	def __init__(self):
		
		self.main_window = tkinter.Tk()
		
		self.top_frame = tkinter.Frame(self.main_window)
		self.middle_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)
		
		self.main_window.geometry("200x70")
		self.main_window.title("Km to Ml converter")
		
		self.label1 = tkinter.Label(self.top_frame, text = "Enter distance in km: ")
		self.label1.pack(side = "left")

		self.entry = tkinter.Entry(self.top_frame, width = 10)
		self.entry.pack(side = "left")

		self.label2 = tkinter.Label(self.middle_frame, text = "Converted to miles: ")
		self.label2.pack(side = "left")

		self.my_button = tkinter.Button(self.bottom_frame, text='Convert', command = self.show_conversion)
		self.my_button.pack()

##################################################################################################

		self.result = tkinter.StringVar()
		self.label = tkinter.Label(self.middle_frame, textvariable = self.result)
		self.label.pack(side = "left")

##################################################################################################

		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()
		
		tkinter.mainloop()
		
	def show_conversion(self):
		km = int(self.entry.get())
		miles = km * 0.6214
		miles = round(miles, 2)
		self.result.set(str(miles))
		#tkinter.messagebox.showinfo("Result", str(km) + " km equals to " + str(miles) + " miles")


myGUI = myGUI()