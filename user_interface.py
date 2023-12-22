import PySimpleGUI as sg
from exif import ExifTag

sg.theme('BluePurple')


# Define the layout
layout = [
	[sg.Image(filename='logo.png', size=(800, 600))],
	[sg.Text('Click browse and select the file you want to remove or extract Exif data', font=("Any 12"))],
	[sg.FileBrowse(target='-FILE-', file_types=(("Image Files", "*.png *.jpg *.jpeg"),)), 
	sg.InputText(key='-FILE-')], #sg.InputText(size=(32, 1))],
	[sg.Button("Remove Data", button_color=('white', 'green')),sg.Button("Extract Data", button_color=('white', 'blue')),
	sg.Cancel(button_color=('white', 'red'))],
]

# Create the window
window = sg.Window('Exif Data Remover', layout, element_justification='center', font=("Times New Roman", 16), size=(1100, 900))

# Create an instance of ExifTag
#exif = ExifTag('')

while True:
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == 'Cancel':
		break
	elif event == 'Remove Data':
		file_path = values['-FILE-']
		exif = ExifTag(file_path) #instance of ExifTag
		if file_path:
			result = exif.remove_data()
			if result is True:
				sg.popup('Data removed successfully!', title='Success', background_color='cyan', text_color='white', auto_close=True, auto_close_duration=5)
			else:
				sg.popup_error(f'Error: {result}', title='Error', background_color='red', text_color='white')
	elif event == 'Extract Data':
		file_path = values['-FILE-']
		if file_path:
			exif = ExifTag(file_path) #instance of ExifTag
			data = exif.extract_data()
			if data:
				exif.save(data)
				sg.popup(f'Extracted data successfully', title='Extraction Success', background_color='black', text_color='white')
			else:
				sg.popup_error('Error extracting data. No Exif data found.', title='Extraction Error', background_color='red', text_color='white')

window.close()

