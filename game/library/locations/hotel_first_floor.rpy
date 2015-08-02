label test1:
    scene expression Solid(loc.pt.color) # Should be a background in the future.
    if not gf.flag("test1"):
        $ gf.set_flag("test1")
        "Label 1 reporting in!"
        "You can put backgrounds or show other screens from here or bind them to Areas for convinience!"
    
    jump walk
   
label test2:
    scene expression Solid(loc.pt.color)
    if not gf.flag("test2"):
        $ gf.set_flag("test2")
        "Just entered label 2!"

    jump walk  
   
label test3:
    scene expression Solid(loc.pt.color)
    if not gf.flag("test3"):
        $ gf.set_flag("test3")
        "Just entered label 3!"
   
    jump walk
   
label test4:
    scene expression Solid(loc.pt.color)
    if not gf.flag("test4"):
        $ gf.set_flag("test4")
        "I am the (secret?) room to the right that you can barely see on the map!"
   
    jump walk
