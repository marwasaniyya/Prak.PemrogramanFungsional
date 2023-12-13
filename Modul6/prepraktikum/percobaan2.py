from PIL import Image, ImageEnhance

# TODO 1: Buka gambar dengan pillow
img_path = 'C:/Users/LEGION/OneDrive/Documents/SEMESTER 5/PEM. FUNGSIONAL/PRAKTIKUM/Modul6/prepraktikum/9fbe8649-dc90-40b9-955a-aae8d68f2be9.jpeg'
image = Image.open(img_path)

# TODO 2: Ubah tingkat kecerahan (brightness) dan kontras (contrast)
enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(1.5)

enhancer = ImageEnhance.Contrast(brightened_image)
final_image = enhancer.enhance(1.2)

# TODO 3: Simpan gambar hasil edit
final_image.save("hasil_edit.jpeg")

# TODO 4: Tampilkan
final_image.show()