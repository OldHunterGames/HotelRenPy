label test5:
    scene expression Solid(loc.pt.color)
    if not gf.flag("test5"):
        $ gf.set_flag("test5")
        "I am a room on the second floor!"
    
    jump walk
