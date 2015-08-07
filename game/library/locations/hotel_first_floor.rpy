label lobby:
    if not gf.flag("lobby"):
        $ gf.set_flag("lobby")
        "Добро пожаловать в гостиницу \"В Туманах\"!"
        "То стоишь в вестибюле гостиницы."
        "Выити из нее нельзя."
        extend "Из игры, всмысле."
        "По карте - красным отмечены комнаты где можно удовлетворить потребность в пище."
        "Зеленым - психологические потребности."
        "Черным - потребность в сне."
        "Синим отмечены переходы между этажами и локациями."
        "Комнаты которые нихрена не делают, отмечены бирюзовым."
        "На мое скромное мнения в будещем вместо цветов стоит использовать один цвет и ряд пиктограм, а карту сделать больше."
    
    jump walk
   
label dinning_room:
    if not gf.flag("dinning_room"):
        $ gf.set_flag("dinning_room")
        "Обеденный зал. Здесь нужна функция \"Накрыть на стол\"."

    jump walk  
   
label kitchen:
    if not gf.flag("kitchen"):
        $ gf.set_flag("kitchen")
        "Кухня, в будущем тут можно будет быстро перекусить или приготовить обед для всех."
        "Тут возникает проблема с цветовыми обозначениями на карте - в этой комнате можно как поесть, так и удовлетворить требование, так и перейти на новую локацию."
   
    jump walk
   
label library:
    if not gf.flag("library"):
        $ gf.set_flag("library")
        "Маленькая библиотека, заваленная книгами."
   
    jump walk

label sport_area:
    if not gf.flag("sport_area"):
        $ gf.set_flag("sport_area")
        "Небольшой тренажерный зал."
        
    jump walk
    
label sport_bar:
    if not gf.flag("sport_bar"):
        $ gf.set_flag("sport_bar")
        "Дымный и темный бар."
        
    jump walk
    
label art_room:
    if not gf.flag("art_room"):
        $ gf.set_flag("art_room")
        "Просторная комната увешенная мольбертами."
        
    jump walk
