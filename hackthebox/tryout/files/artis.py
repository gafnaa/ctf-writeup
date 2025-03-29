from PIL import Image
from PIL.ExifTags import TAGS
from PIL import PngImagePlugin

# Buat gambar kosong
img = Image.new("RGB", (100, 100), color=(255, 150, 0))

'''
# Tambahkan metadata EXIF
exif_data = PngImagePlugin.PngInfo()
exif_data.add_text("Artist", "{{7*7}}")
'''
# Simpan gambar dengan metadata
img.save("nigaa.jpg")
