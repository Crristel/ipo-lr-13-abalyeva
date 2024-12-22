from image import ImageHandler, ImageProcessor  
Menu = True
current_image_path = "image_2.jpg"  
handler = None  


def menu_image():
    print(f"Меню".center(35, "~"))
    print(f"1 - Изменение размера")
    print(f"2 - Сохранить в формате PNG")
    print(f"3 - Применить фильтр blure")
    print(f"4 - Добавить текст")
    print(f"5 - Выйти")


while Menu:
    menu_image()
    input_num = input("Введите номер: ")

    if not input_num.isdigit():
        print("Введите корректное значение!")
        continue

    input_num = int(input_num)

    try:
        if handler is None:  
            handler = ImageHandler(current_image_path)
            handler.load_image()

        if handler.image is None:  
            print("Не удалось загрузить изображение. Завершение программы.")
            Menu = False
            continue

        processor = ImageProcessor(handler.get_image())   

        if input_num == 1:
            handler.resize_image()
            processor.get_image().show()
            print("Размер изменён.")

        elif input_num == 2:
            handler.save_png()
            
        elif input_num == 3:
            processor.blur_filter()
            processor.get_image().show()

        elif input_num == 4:
            processor.add_text()
            processor.get_image().show()
        elif input_num == 5:
            Menu = False
            

        else:
            print("Некорректный ввод!")

    except FileNotFoundError:
        print("Файл изображения не найден!")
        Menu = False
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        Menu = False

