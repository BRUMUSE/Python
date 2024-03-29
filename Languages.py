import  collections

list = {
    "Ларри Уолл": "Perl",
    "Рэндалл Хайд": "HLA",
    "Андерс Хейлсберг": "Delphi",
    "Ричард Хикки": "Clojure",
    "Гарольд Абельсон": "Лого",
    "Пол Грэм": "Lisp",
    "Оле-Йохан Даль": "Симула",
    "Эдсгер Вибе Дейкстра": "Алгол",
    "Роберту Иерузалимски": "Lua",
    "Кеннет Юджин Айверсон": "APL",
    "Андрей Александреску": "D",
    "Альфред Ахо": "AWK",
    "Кристен Нюгор": "Симула",
    "Маркус Хендрик Овермарс": "",
    "Родриго Баррето де Оливейра": "Boo",
    "Джон Оустерхаут": "Tcl",
    "Роб Пайк": "Go, Limbo, Sawzall, Newsqueak",
    "Джереми Ашкенас": "сoffeeScript",
    "Стивен Ричард Борн": "C",
    "Уолтер Брайт": "D",
    "Джон Бэкус": "Фортран",
    "Гвидо Ван Россум": "Python",
    "Никлаус Вирт": "Паскаль, Модула-2, Оберон",
    "Ксавье Лерой": "OCaml",
    "Томас Курц": "Basic",
    "Алан Кёртис Кэй": "Smalltalk",
    "Джеймс Лайон": "Intercal",
    "Легалов Александр Иванович": "Пифагор",
    "Расмус Лердорф": "PHP",
    "Барбара Лисков": "Клу",
    "Дон Сайм": "F#",
    "Ричард Мэттью Столлман": "GNU",
    "Бьёрн Страуструп": "C++",
    "Дэвид А. Тёрнер": "SASL, KRC, Miranda",
    "Кен Томпсон": "C",
    "Грейс Хоппер": "COBOL",
    "Джон Маккарти": "Лисп",
    "Юкихиро Мацумото": "Ruby",
    "Бертран Мейер": "Эйфель",
    "Робин Милнер": "ML",
    "Чарльз Мур": "Форт",
    "Петер Наур": "Алгол",
    "Сеймур Пейперт": "Logo",
    "Святослав Пестов": "Factor",
    "Деннис Макалистэйр Ритчи": "BCOL, B, C",
    "Конрад Эрнст Отто Цузе": "Планкалкюль",
    "Дон Дудс": "Intercal",
    "Джеймс Гослинг": "Java",
    "Жан Давид Ишбиа": "Ада, LIS",
    "Джон Джордж Кемени": "Basic",
    "Брайан Уилсон Керниган": "AWK",
    "Дональд Эрвин Кнут": "Metafont"
}

while True:
    try:
        print("Выберите действие\nВведите '1' для сортировки словаря\nНажмите '2'для поиска программиста")
        operation  = int(input("Введите число: "))
        if operation == 1 or operation == 2:
            break
        else:
            print("\nКоманды не существует")
    except (TypeError, ValueError):
        print("\nОшибка. Возможные варианты '1' или'2' ")

if operation == 1:

    sorted_list = collections.OrderedDict(sorted(list.items()))
    for key, value in sorted_list.items():
        print(key, ",    Язык программирования: ", value)
else: # Выполнение операции "нахождение языка программирования"
    while True:
        try:
            name = input("\nВведите имя создателя: ")
            print("\nСоздатель языков программирования: ", list[name])
            break
        except (TypeError, KeyError):
                print("Введите Имя и Фамилию полностью.")