label walk:
    while 1:
        $ result = ui.interact()
       
        if result[0] == "go_back":
            $ loc.player_tile = loc.last_coords*1
            $ loc.last_coords = None
            if renpy.has_label(loc.pt.label):
                jump expression loc.pt.label
            else:
                "No such Label: ([loc.pt.label]) exists (yet :0)"
                jump walk
           
        if result[0] == "move":
            $ loc.last_coords = loc.player_tile*1
            if result[1] == "up":
                $ loc.player_tile[1] -= 1
            elif result[1] == "down":
                $ loc.player_tile[1] += 1
            elif result[1] == "left":
                $ loc.player_tile[0] -= 1
            elif result[1] == "right":
                $ loc.player_tile[0] += 1
            if renpy.has_label(loc.pt.label):
                if loc.pt.bg:
                    scene expression loc.pt.bg # Should be a background in the future.
                    with dissolve
                else:
                    scene expression Solid(loc.pt.color)
                jump expression loc.pt.label
            else:
                scene black
                "No such Label: ([loc.pt.label]) exists (yet :0)"
                jump walk
                
        if result[0] == "change_location":
            $ loc.last_coords = None
            $ temp = result[1]
            $ loc = locations[temp[2]]
            $ loc.last_coords = None
            $ loc.player_tile = [temp[0], temp[1]]
            if renpy.has_label(loc.pt.label):
                if loc.pt.bg:
                    scene expression loc.pt.bg # Should be a background in the future.
                    with dissolve
                else:
                    scene expression Solid(loc.pt.color)
                jump expression loc.pt.label
            else:
                scene black
                "No such Label: ([loc.pt.label]) exists (yet :0)"
                jump walk
