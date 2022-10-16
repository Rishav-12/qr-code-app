import PySimpleGUI as sg
import qrcode
import qrcode.image.svg

sg.theme('BluePurple')

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
	data = values['-DATA-']
	filename = values['-FILENAME-']
	filetype = values['-FILETYPE-']
	print(data, filename, filetype)
	if data == "" or filename == "" or filetype not in options:
		return

	if filetype == 'png':
		qrcode_png(data, filename)
	else:
		qrcode_svg(data, filename)

options = ['svg', 'png']

layout = [[sg.Text('Choose filetype:'), sg.Combo(options, default_value='select', key='-FILETYPE-', size=(10, 1))],
	[sg.Text('Your data:'), sg.Input(key='-DATA-')],
	[sg.Text('Name of file'), sg.Input(key='-FILENAME-')],
	[sg.Button('Create QR Code')]]

window = sg.Window('QR Code App', layout)

while True:
	event, values = window.read()
	if event in (None, 'Exit'):
		break
	if event == 'Create QR Code':
		create()

window.close()
