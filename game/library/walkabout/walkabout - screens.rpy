screen walk():
    
    # General Info:
    vbox:
        align (0.5, 0.0)
        text("Player Coords: %d, %d" % (loc.player_tile[0], loc.player_tile[1]))
        text "Location: [loc.name]"
    
    # Action Buttons ---------------------------------------------->
    vbox:
        align(0, 0.5)
        text "Change Location to:"
        if loc.pt.teleport:
            for t in loc.pt.teleport:
                $ temp = locations[t[2]]
                textbutton "[temp.name]":
                    action Return(["change_location", t])
        textbutton "Back":
            action If(loc.last_coords, true=Return(["go_back"]))
                    
    # Directional Buttons  ---------------------------------------------->
    vbox:
        align (0.5, 0.9)
        spacing 10
        hbox:
            xalign 0.5
            textbutton "Up":
                action If(loc.button_state("up"), true=Return(['move', 'up']))
        hbox:
            xalign 0.5
            spacing 5
            textbutton "Left":
                action If(loc.button_state("left"), true=Return(['move', 'left']))
            textbutton "Down":
                action If(loc.button_state("down"), true=Return(['move', 'down']))
            textbutton "Right":
                action If(loc.button_state("right"), true=Return(['move', 'right']))
 
    # Tile Map ---------------------------------------------->
    frame:
        align (1.0, 1.0)
        xysize (200, 200)
        xfill True
        yfill True
        hbox:
            align (0.5, 0.5)
            box_wrap True
            xysize(162, 82)
            for y in xrange(loc.dimensions[1]):
                    for x in xrange(loc.dimensions[0]):
                        frame:
                            if loc.pt == loc.map[x][y]:
                                background "#4b0082"
                            else:
                                background loc.map[x][y].color
                            xysize (8, 8)
                            xfill True
                            yfill True
