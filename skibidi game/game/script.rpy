﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[name]")

# The game starts here.

label start:
    
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    
    $ name = renpy.input("Who are you?", default = "", length = 12)
    $ name = name.strip() or "Sigma"

    mc"You've created a new Ren'Py game."
    mc"Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
