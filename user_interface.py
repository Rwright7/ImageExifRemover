import PySimpleGUI as sg
from exif import ExifTag

sg.theme('BluePurple')

layout = [
	[sg.Image(filename='logo.png', size=(800, 600))],
	[sg.Text('Select file you want to remove Exif data', font=("Any 12"))],
	[sg.InputText(key='-FILE-'), sg.InputText(size=(32, 1))],
	[sg.FileBrowse(target='-FILE-', file_types=(("Image Files", "*.png *.jpg *.jpeg"),))],
	[sg.Submit(button_color=('white', 'green')), sg.Cancel(button_color=('white', 'red'))],

]

window = sg.Window('Exif Data Remover', layout, font=("Times New Roman", 16), size=(1200, 1000))

exif = ExifTag()


while True:
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == 'Cancel':
		break
	elif event == 'Submit':
		file_path = values['-FILE-']
		if file_path:
			result = exif.remove_data(file_path)  # Call the imported Exif removal function
			if result is True:
				ssg.popup(message, title='Success', background_color='green', text_color='white', auto_close=True, auto_close_duration=2)
			else:
				sg.popup_error(f'Error: {result}', title='Error', background_color='red', text_color='white')

window.close()





'''
sg.theme('BluePurple')
BG_COLOR = sg.theme_text_color()
TXT_COLOR = sg.theme_background_color()


layout = [
			[sg.Text('Select file you want to remove Exif data')],
			[sg.In(), size==(32,1)]
			[sg.Button('Save'), sg.Button('Exit')]
		 ]

window = sg.Window('Exif data remover', layout)
event, values = window.read()


window.close()
'''





'''
#sg.theme('DarkAmber')   # Add a touch of color

# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
			[sg.Text('Enter something on Row 2'), sg.InputText()],
			[sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)


# Event Loop to process "events" and get the "values" of the inputs
while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
		break
	print('You entered ', values[0])

window.close()




event, values  = sg.Window('Exif remover', [[sg.Text('Select file')],
						[sg.InputText(), sg.FileBrowse()],
						[sg.Submit(), sg.Cancel()]]).read(close=True)

source_filename = values[0]

'''