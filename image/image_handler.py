from PIL import Image

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None

    def load_image(self):
        try:
            self.image = Image.open(self.image_path)
        except FileNotFoundError:
            print(f"Ошибка: Файл не найден: {self.image_path}")
            self.image = None
        except Exception as e:
            print(f"Ошибка при загрузке изображения: {e}")
            self.image = None

    def save_png(self, filename="output.png"):
        self.image.save(filename, "PNG")
        print(f"Сохранён как {filename}.")


    def resize_image(self, size=(300, 300)):
         if self.image is not None:
             try:
                self.image = self.image.resize(size)
             except Exception as e:
                print(f"Ошибка при изменении размера: {e}")
    def get_image(self):
        return self.image

