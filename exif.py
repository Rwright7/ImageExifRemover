import csv
from PIL import Image
from pathlib import Path
from PIL.ExifTags import (
	GPSTAGS,TAGS
)

class ExifTag:
	def __init__(self, image_path: Path):
		try:
			self.image_path = image_path
			image = Image.open(image_path)
		except FileNotFoundError:
			raise ValueError(f"File not found: {image_path}")
		except Exception as error:
			raise ValueError(f"Error opening file: {error}")

	@staticmethod
	def dec_degrees(degree: float, minutes: float, seconds: float, direction: str) -> float:
		decimal_degrees = degree + (minutes / 60) + (seconds / 3600)

		if direction == "S" or direction == "W":
			decimal_degrees *= -1
		return decimal_degrees

	def extract_data(self) -> dict:
		data = {}
		gps_coords = {}

		image = Image.open(self.image_path)
		exif_data = image._getexif()

		if not exif_data:
			return {}

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

	def remove_data(self) -> tuple:
		try:
			image = Image.open(self.image_path)
			data = list(image.getdata())
			new_image_path = self.image_path.parent / "newphoto.jpg"
			new_image = Image.new(image.mode, image.size)
			new_image.putdata(data)
			new_image.save(new_image_path)
			new_image.close()
			return True
		except Exception as error:
			return False

	def save(self, data):
		csv_file = "exif_data.csv"
		with open(csv_file, "w", newline="") as file:
			csv_writer = csv.writer(file)
			for item in data.items():
				csv_writer.writerow(item)
