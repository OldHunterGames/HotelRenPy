label lobby:
    if not gf.flag("test1"):
        $ gf.set_flag("test1")
        "Welcome to the Mists Of Rome Hotel!"
        "We are programmed to receive."
        "You can check-out any time you like! "
        extend "But you can never leave!"
    
    jump walk
   
label test2:
    if not gf.flag("test2"):
        $ gf.set_flag("test2")
        "Just entered label 2!"

    jump walk  
   
label test3:
    if not gf.flag("test3"):
        $ gf.set_flag("test3")
        "Just entered a new area, you can get to the second floor from here!"
   
    jump walk
   
label test4:
    if not gf.flag("test4"):
        $ gf.set_flag("test4")
        "I am the (secret?) room to the right that you can barely see on the map!"
   
    jump walk
