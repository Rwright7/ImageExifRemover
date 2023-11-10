import os
from PIL import Image
from PIL.ExifTags import (
	GPSTAGS,TAGS
)

class ExifTag:
	def dec_degrees(self, degree, minutes, seconds, direction):
		#Convert decimal degrees for longitude and latitude
		decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)

		#adjust the decimal degrees by multiplying it by -1 to represent the southern or western hemisphere.
		if direction == "S" or direction == "W":
			decimal_degrees *= -1
		return decimal_degrees


	def extract_data(self, image_path:str) -> dict:
		if not os.path.exists(image_path):
			return None

		data = {}
		gps_coords = {}

		image = Image.open(image_path)
		exif_data = image._getexif()

		if not exif_data:
			return None

		for tag, value in exif_data.items():
			tag_name = TAGS.get(tag)
			if tag_name == "GPSInfo":
				for key, val in value.items():
					gps_coords_key = GPSTAGS.get(key)
					if gps_coords_key:
						gps_coords[gps_coords_key] = val
			else:
				data[tag_name] = value
		return {**data, "gps_coords": gps_coords}


	def remove_data(self, image_path: str) -> bool:
		if not os.path.exists(image_path):
			print(f"'{image_path}' does not exists!")
			return False
		try:
			image = Image.open(image_path)
			data = list(image.getdata())
			new_image = Image.new(image.mode, image.size)
			new_image.putdata(data)
			new_image.save('/Users/roshawnw/learnprogramming/makebot/Phototest/newphoto.jpg')
			new_image.close()
			print("Successfully removed exif data!")
			return True
		except Exception as error:
			print(error)
			return False