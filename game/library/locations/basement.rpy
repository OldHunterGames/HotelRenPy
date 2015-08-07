label basement_entrance:
    if not gf.flag("basement_entrance"):
        $ gf.set_flag("basement_entrance")
        "Чистый, хотя и несколько пыльный подвал."
    
    jump walk

label mine:
    if not gf.flag("mine"):
        $ gf.set_flag("mine")
        "Влажная, холодная шахта."
    
    jump walk
