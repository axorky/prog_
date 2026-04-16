from tkinter import *

def show_recommendation_btn():
    global recommend_btn, change_entry, confirm_btn, mean_entry, feedback_btn, start_over_btn
    budget_entry.delete(0, END)
    purpose_entry.delete(0, END)
    brand_entry.delete(0, END)
    text_area.delete(1.0, END)
    text_area.insert(END, 
    "Добрый день! Сегодня я ваш консультант по выбору смартфона!\n")
    if 'change_entry' in globals():
        change_entry.destroy()
    if 'confirm_btn' in globals():
        confirm_btn.destroy()
    if 'mean_entry' in globals():
        mean_entry.destroy()
    if 'feedback_btn' in globals():
        feedback_btn.destroy()
    if 'start_over_btn' in globals():
        start_over_btn.destroy()
    recommend_btn.pack()

def on_click():
    global recommend_btn
    get_recommendation()
    recommend_btn.pack_forget()

def get_recommendation():
    b_input = budget_entry.get()
    b = 0
    if b_input.isdigit():
        b = int(b_input)
    else:
        b = 20000
    if b <= 0:
        b = 20000

    purp_input = purpose_entry.get()
    purp = 1
    if purp_input == "1":
        purp = 1
    elif purp_input == "2":
        purp = 2
    elif purp_input == "3":
        purp = 3
    elif purp_input == "4":
        purp = 4
    else:
        purp = 1

    brand = brand_entry.get()
    if brand == "":
        brand = "любой"

    level = ""
    if b < 15000:
        level = "бюджетный"
    elif b <= 35000:
        level = "средний"
    else:
        level = "премиум"

    text_area.delete(1.0, END)
    text_area.insert(END, "-"*30 + "\n")
    text_area.insert(END, f"Ваш бюджет: {b} р.\n")
    text_area.insert(END, f"Категория: {level}\n")
    text_area.insert(END, f"Предпочитаемый брэнд: {brand}\n")
    text_area.insert(END, "-"*30 + "\n")

    if brand != "любой":
        text_area.insert(END, f"Учитываем ваш выбор бренда: {brand}\n")
        if "xia" in brand.lower() or "ксиа" in brand.lower() or "сяо" in brand.lower():
            if level == "бюджетный":
                text_area.insert(END, "Рекомендуем: Xiaomi Redmi Pad SE\nЦена: около 10600 р.\nПочему?: Планшет с диагональю 8.7, 64 ГБ память, Частота 90 ГЦ\n")
            elif level == "средний":
                text_area.insert(END, "Рекомендуем: Телефон Xiaomi 14T\nЦена: около 32400 р.\nПочему?: Невероятная камера, Минимальные рамки экрана, 12 Гб ОЗУ\n")
            else:
                text_area.insert(END, "Рекомендуем: Смартфон realme GT7 Pro\nЦена: около 69000 р.\nПочему?: Full HD, 512 ГБ памяти, Высокая производительность\n")
        elif "iph" in brand.lower() or "айф" in brand.lower() or "app" in brand.lower() or "эпл" in brand.lower():
            if level == "бюджетный":
                text_area.insert(END, "Рекомендуем: Apple iPhone 7\nЦена: около 11000 р.\nПочему?: 128 ГБ Память, Отличная камера для своей цены, Чистый звук\n")
            elif level == "средний":
                text_area.insert(END, "Рекомендуем: Apple iPhone 13 mini\nЦена: около 35000 р.\nПочему?: Ёмкость батареи 2438 мА/ч, 256 ГБ памяти, OLED-дисплей\n")
            else:
                text_area.insert(END, "Рекомендуем: Apple iPhone 16\nЦена: около 67000 р.\nПочему?: 50 мп камера, Видеосъёмка 4к, 8 ГБ ОЗУ, До 40 часов работы\n")
        elif "sams" in brand.lower() or "самс" in brand.lower():
            if level == "бюджетный":
                text_area.insert(END, "Рекомендуем: Samsung Galaxy A16\nЦена: около 15000 р.\nПочему?: 6.7 диагональ, Быстрая зарядка, FHD+ Super AMOLED Дисплей\n")
            elif level == "средний":
                text_area.insert(END, "Рекомендуем: Смартфон Samsung Galaxy A56\nЦена: около 35200 р.\nПочему?: Аккумулятор 5000 мА/ч, камера 50+12Мп, Частота 120 ГЦ\n")
            else:
                text_area.insert(END, "Рекомендуем: Samsung Galaxy S25 Ultra\nЦена: около 74900 р.\nПочему?: 12 ГБ ОЗУ, Ультрапрочный, Мощный процессор Snapdragon\n")
        else:
            text_area.insert(END, f"К сожалению - {brand}, не входит в число наших рекомендуемых телефонов, но мы это исправим!\n")
    else:
        text_area.insert(END, "Наше предложение:\n")
        if level == "бюджетный":
            if purp == 4:
                text_area.insert(END, "Рекомендуем: TECNO POVA 7 - Для ваших игр\nЦена: около 15000 р.\nПочему?: Большой экран, 8 ГБ ОЗУ\n")
            elif purp == 3:
                text_area.insert(END, "Рекомендуем: OPPO A5\nЦена: около 10000 р.\nПочему?: 2 Камеры 50 Мп, 256 ГБ\n")
            elif purp == 2:
                text_area.insert(END, "Рекомендуем: REDMI 15\nЦена: около 13000 р.\nПочему?: Надежный, лёгкий, NFC\n")
            else:
                text_area.insert(END, "Рекомендуем: Xiaomi Redmi Note 14\nЦена: около 15000 р.\nПочему?: Отличный телефон в соотношении цена=качество\n")
        elif level == "средний":
            if purp == 4:
                text_area.insert(END, "Рекомендуем: Xiaomi Poco X7 Pro 5G\nЦена: около 25600 р.\nПочему?: Сильный процессор на базе mediatek, 12 ГБ ОЗУ\n")
            elif purp == 3:
                text_area.insert(END, "Рекомендуем: HONOR 200\nЦена: около 32000 р.\nПочему?: Лучшая камера в своем классе, 3 Камеры, 512 ГБ памяти\n")
            elif purp == 2:
                text_area.insert(END, "Рекомендуем: Samsung Galaxy S24 FE\nЦена: около 36000 р.\nПочему?: Частота 120 Гц, 6.7 Диагональ, Время работы до 21 часа\n")
            else:
                text_area.insert(END, "Рекомендуем: HONOR X9d\nЦена: около 32600 р.\nПочему?: Прочный, Стильный, Защита от падений, пыли и влаги\n")
        else:
            if purp == 4:
                text_area.insert(END, "Рекомендуем: Realme GT7\nЦена: около 51300 р.\nПочему?: Частота 120 Гц, 2к Разрешение, 7700 мм2 Система охлаждения\n")
            elif purp == 3:
                text_area.insert(END, "Рекомендуем: Apple iPhone 16\nЦена: около 62900 р.\nПочему?: Лучшая камера 48+12 Мп, Зум до 25х\n")
            elif purp == 2:
                text_area.insert(END, "Рекомендуем: Google Pixel 9\nЦена: около 57500 р.\nПочему?: Чёткий OLED-дисплей, Ёмкость аккумулятора 4700 мА/ч\n")
            else:
                text_area.insert(END, "Рекомендуем: Huawei Mate 70 Pro\nЦена: около 64900 р.\nПочему?: Новый дизайн, встроенный ИИ-пощник, 6.9 диагональ\n")

    text_area.insert(END, "-"*30 + "\n")
    text_area.insert(END, "Хотите изменить ввод? (да/нет):\n")
    global change_entry
    change_entry = Entry(root)
    change_entry.pack()
    global confirm_btn
    confirm_btn = Button(root, text="Подтвердить", command=confirm_change)
    confirm_btn.pack()

def confirm_change():
    change = change_entry.get().lower()
    change_entry.destroy()
    confirm_btn.destroy()
    if change == "да" or change == "yes":
        show_recommendation_btn()
    else:
        text_area.insert(END, "Вас всё устроило в нашем обслуживании?:\n")
        global mean_entry
        mean_entry = Entry(root)
        mean_entry.pack()
        global feedback_btn
        feedback_btn = Button(root, text="Отправить отзыв", command=send_feedback)
        feedback_btn.pack()

def send_feedback():
    global start_over_btn
    mean = mean_entry.get().lower()
    mean_entry.destroy()
    feedback_btn.destroy()
    if mean == "да" or mean == "yes":
        text_area.insert(END, "-"*30 + "\nСпасибо за использование нашего консультанта!\n")
    else:
        text_area.insert(END, "-"*30 + "\nМы учтём ваше мнение, спасибо за отзыв!\n")
    start_over_btn = Button(root, text="Начать заново", command=show_recommendation_btn)
    start_over_btn.pack()

root = Tk()
root.title("Консультант по смартфонам")

Label(root, text="Добрый день! Сегодня я ваш консультант по выбору смартфона!").pack()
Label(root, text="-"*30).pack()

Label(root, text="Введите ваш бюджет в рублях:").pack()
budget_entry = Entry(root)
budget_entry.pack()

Label(root, text="Для чего нужен телефон?").pack()
Label(root, text="1 - Для постоянного использования").pack()
Label(root, text="2 - Для работы и учебы").pack()
Label(root, text="3 - Для фото и видео").pack()
Label(root, text="4 - Для игр").pack()
Label(root, text="Введите номер (1-4):").pack()
purpose_entry = Entry(root)
purpose_entry.pack()

Label(root, text="Какой бренд вы бы хотели у своего телефона? (Ничего не пишите, если ничего не предпочитаете):").pack()
brand_entry = Entry(root)
brand_entry.pack()

text_area = Text(root, height=20, width=80)
text_area.pack()

global recommend_btn
recommend_btn = Button(root, text="Получить рекомендацию", command=on_click)
recommend_btn.pack()

root.mainloop()

