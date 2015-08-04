label start:
    $ gf = Flags() # Global flags on their own namespace.
    $ areas = {} # We add all area instances here as area.id = area
    $ locations = {} # Same for locations
    python:
        blocked = Area("blocked", "#f0f8ff")
        Area("lobby", blue, bg="content/gfx/locations/hotel1/lobby.jpg")
        test2 = Area("test2", "#00ffff")
        test3 = Area("test3", "#00ffff", teleport=[[0, 0, "hsf"]])
        test4 = Area("test4", "#faebd7")
        test5 = Area("test5", "#00ffff", teleport=[[3, 5, "hff"]])
        
    python:
        pattern = ((3, 3, areas["lobby"]),
                        (3, 4, test2),
                        (3, 5, test3),
                        (4, 4, test4))
        hotel1 = Location("hff", "Hotel", "First Floor", (20, 10), (3, 3), pattern)
        pattern = [[0, 0, test5]]
        hotel2 = Location("hsf", "Hotel", "Second Floor", (20, 10), (0, 0), pattern)
        
    $ loc = hotel1 # Global variable representing current location, this prolly should be a property of mc
    "Starting the game!"
    
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
