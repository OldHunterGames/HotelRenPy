label lobby_second:
    if not gf.flag("lobby_second"):
        $ gf.set_flag("lobby_second")
        "Лестничная площадка второго этажа."
    
    jump walk
    
label corridor:
    
    jump walk
    
label room:
    if not gf.flag("room"):
        $ gf.set_flag("room")
        "Комната, в будущем нужно сделать личную комнату игрока."
    
    jump walk
