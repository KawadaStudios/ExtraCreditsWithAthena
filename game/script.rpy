# Init configs
init python:
    renpy.music.register_channel("ambience", mixer="music", loop=True)
define config.window = 'hide'

# ---START---
label start:
    call demo
    return
