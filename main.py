from tkinter import *
import qrcode
import qrcode.image.svg

def qrcode_png(data, filename):
	qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=2)
	qr.add_data(data)
	qr.make(fit=True)

	img = qr.make_image(fill_color="black", back_color="white")
	img.save(f"{filename}.png")

def qrcode_svg(data, filename):
	factory = qrcode.image.svg.SvgPathImage
	svg_img = qrcode.make(data, image_factory=factory)
	svg_img.save(f"{filename}.svg")

def create():
	if data.get() == "" or filename.get() == "" or option.get() == OPTIONS[0]:
		return
	filetype = option.get()
	if filetype == 'png':
		qrcode_png(data.get(), filename.get())
	else:
		qrcode_svg(data.get(), filename.get())

root = Tk()
root.geometry("300x200")
root.title("QR Code App")

OPTIONS = ['select', 'png', 'svg']

option = StringVar()
option.set(OPTIONS[0])

filetype_label = Label(root, text = "Choose filetype:")
filetype_label.grid(row = 0, column = 0)

option_menu = OptionMenu(root, option, *OPTIONS)
option_menu.grid(row = 0, column = 1, pady = 10)

data_label = Label(root, text = "Your data:")
data_label.grid(row = 1, column = 0)

data = Entry(root)
data.grid(row = 1, column = 1, pady = 10, ipadx = 15, ipady = 3)

filename_label = Label(root, text = "Name of File:")
filename_label.grid(row = 2, column = 0)

filename = Entry(root)
filename.grid(row = 2, column = 1, ipadx = 15, ipady = 3)

create = Button(root, text = "Create QR Code", command = create)
create.grid(columnspan = 2, pady = 12)

root.mainloop()