label start:
    $ gf = Flags() # Global flags on their own namespace.
    $ areas = {} # We add all area instances here as area.id = area
    $ locations = {} # Same for locations
    python:
        blocked = Area("blocked", "#f0f8ff")
        Area("lobby", blue, bg="content/gfx/locations/hotel1/lobby.jpg", teleport=[[10, 5, "hsf"]])
        Area("dinning_room", red, bg="content/gfx/locations/hotel1/dinning_room.jpg")
        Area("kitchen", red,  bg="content/gfx/locations/hotel1/kitchen.jpg", teleport=[[10, 7, "bm"]])
        Area("library", green, bg="content/gfx/locations/hotel1/library.jpg")
        Area("sport_area", green, bg="content/gfx/locations/hotel1/sport_area.jpg")
        Area("sport_bar", red, bg="content/gfx/locations/hotel1/sport_bar.jpg")
        Area("art_room", green, bg="content/gfx/locations/hotel1/art_room.jpg")
        Area("lobby_second", blue, bg="content/gfx/locations/hotel2/lobby_second.jpg", teleport=[[10, 5, "hff"]])
        Area("corridor", "#00ffff", bg="content/gfx/locations/hotel2/corridor.jpg")
        Area("room", black, bg="content/gfx/locations/hotel2/room.jpg")
        Area("basement_entrance", blue, bg="content/gfx/locations/hotel_b/basement.jpg", teleport=[[10, 7, "hff"]])
        Area("mine", green, bg="content/gfx/locations/hotel_b/mine.jpg")
        
    python:
        pattern = ((10, 5, areas["lobby"]),
                        (10, 6, areas["dinning_room"]),
                        (10, 7, areas["kitchen"]),
                        (11, 6, areas["library"]),
                        (9, 7, areas["sport_bar"]),
                        (8, 7, areas["sport_area"]),
                        (12, 6, areas["art_room"]))
        hotel1 = Location("hff", "Hotel", "Первый этаж", (20, 10), (10, 5), pattern)
        pattern = ((10, 5, areas["lobby_second"]),
                        (10, 6, areas["corridor"]),
                        (9, 6, areas["corridor"]),
                        (8, 6, areas["corridor"]),
                        (7, 6, areas["corridor"]),
                        (6, 6, areas["corridor"]),
                        (5, 6, areas["corridor"]),
                        (11, 6, areas["corridor"]),
                        (12, 6, areas["corridor"]),
                        (13, 6, areas["corridor"]),
                        (14, 6, areas["corridor"]),
                        (15, 6, areas["corridor"]),
                        (9, 7, areas["room"]),
                        (7, 7, areas["room"]),
                        (5, 7, areas["room"]),
                        (11, 7, areas["room"]),
                        (13, 7, areas["room"]),
                        (15, 7, areas["room"]))
        hotel2 = Location("hsf", "Hotel", "Второй этаж", (20, 10), (10, 5), pattern)
        pattern = ((10, 7, areas["basement_entrance"]),
                        (10, 8, areas["mine"]))
        bas = Location("bm", "Hotel", "Подвал", (20, 10), (10, 7), pattern)
        
    $ loc = hotel1 # Global variable representing current location, this prolly should be a property of mc
    "Начинаем игру!"
    
    show screen walk
    scene expression loc.pt.bg
    jump lobby



# default place = None
# init -1 python hide: # Функция возвращающая в нужную локацию.
    # store.place = None
    # def label_callback(name, abnormal):
        # store.lines = store.place <> name
        # store.place = name
    # config.label_callback = label_callback
# init python: # Функция отвечающая за смену времени.
    # def Change_Time():
        # if store.Time == "Утро":
            # store.Time = "День"
        # elif store.Time == "День":
            # store.Time = "Вечер"
        # elif Time == "Вечер":
            # store.Time = "Ночь"
        # else:
            # store.Time = "Утро"
        # renpy.jump(store.place)
# # Экран который по идее должен отображать текущее время и содержать кнопку промотки времени.
# screen gui:
    # frame: # Кнопка промотки времени.
        # xalign 0.15
        # yalign 0.15
        # has vbox
        # hbox:
            # textbutton ("Время")  action Function(Change_Time)
    # frame: # Текущее время.
        # xalign 0.85
        # yalign 0.15
        # has vbox
        # hbox:
            # text "Время:[Time]"
# label start: # Начинаем игру, задаем положение времени на Утро и отправляем игрока на 1 этаж.
    # $ Time = "Утро"
    # jump first
# label first: # Сразу вызываем экран отображающий время (который в текущем положении прекрывает все остальное и херит игру).
    # show screen gui
    # if lines: # Игра проверяет находится ли игрок в той же локации что и до этого (ущербно, я знаю)
        # "Ты стоишь в холле первого этажа." # Если нет тогда она показывает текст захода на локацию и переключает переменную. Если игрок делает действие или проматывает время в пределах 1 локации это сообщение не появляется. 
    # menu: # По комнатам нечего и говорить тут все вообще элементарно.
        # "Подняться на второй этаж":
            # jump second
        # "Пройти на кухню":
            # jump kitchen
        # "Направиться в столовую":
            # jump dinning
        # "Пройти в библиотеку":
            # jump library
        # "Заглянуть в спортивную зону":
            # jump sport_area
        # "Заскочить в творческую комнату":
            # jump art_room
        # "Спуститься в подвал":
            # jump down
# label second: # Экран времени вызывается при входе на каждую локацию.
    # show screen gui
    # if lines:
        # "Ты стоишь на лестничной площадке второго этажа."
    # menu: # Я сделал всего одну комнату потому что если одна будет работать то с остальными проблем не будет, а пока не хочу загружать пространство мусором. Ну, еще большим количеством мусора.
        # "Идти в свой номер":
            # jump room
        # "Спуститься на первый этаж":
            # jump first
# label down:
    # show screen gui
    # if lines:
        # "Ты стоишь в сыром и промозглом подвале."
    # menu:
        # "Углубиться в шахту":
            # jump mine
        # "Подняться на первый этаж":
            # jump first
# label room:
    # show screen gui
    # if lines:
        # "Ты стоишь в своей комнате"
    # menu:
        # "Спать в своей кровати": # Действия пока не делают ничего кроме промотки времени.
            # $ Change_Time()
        # "Выйти из своего номера":
            # jump second
# label kitchen:
    # show screen gui
    # if lines:
        # "Ты стоишь в запотевшой от жара кухне."
    # menu:
        # "Перекусить":
            # $ Change_Time()
        # "Вернуться в холл":
            # jump first
# label dinning:
    # show screen gui
    # if lines:
        # "Ты стоишь в богато убранной столовой."
    # menu:
        # "Поесть":
            # $ Change_Time()
        # "Вернуться в холл":
            # jump first
# label library:
    # show screen gui
    # if lines:
        # "Ты стоишь в маленькой, заваленной книгами библиотеке."
    # menu:
        # "Почитать что-то":
            # $ Change_Time()
        # "Вернуться в холл":
            # jump first
# label sport_area:
    # show screen gui
    # if lines:
        # "Ты стоишь в просторном и гулком спортзале."
    # menu:
        # "Поупражняться":
            # $ Change_Time()
        # "Вернуться в холл":
            # jump first
# label mine:
    # show screen gui
    # if lines:
        # "Ты сутулишься в узкой шахте."
    # menu:
        # "Раскапывать месторождение":
            # $ Change_Time()
        # "выити из шахты":
            # jump down
# label art_room:
    # show screen gui
    # if lines:
        # "Ты стоишь в залитой светом комнате с мольбертами."
    # menu:
        # "Рисовать":
            # $ Change_Time()
        # "Вернуться в холл":
            # jump first
