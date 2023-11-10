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

window = sg.Window('Exif Data Remover', layout, element_justification='center', font=("Times New Roman", 16), size=(1200, 1000))

exif = ExifTag()


while True:
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == 'Cancel':
		break
	elif event == 'Submit':
		file_path = values['-FILE-']
		if file_path:
			result = exif.remove_data(file_path) 
			if result is True:
				ssg.popup(message, title='Success', background_color='green', text_color='white', auto_close=True, auto_close_duration=2)
			else:
				sg.popup_error(f'Error: {result}', title='Error', background_color='red', text_color='white')

window.close()
