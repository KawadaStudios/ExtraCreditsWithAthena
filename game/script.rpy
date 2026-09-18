# --- INIT CONFIGS ---

init python:
    renpy.music.register_channel("ambience", mixer="music", loop=True)
    renpy.music.register_channel("group_sfx", mixer="sfx", loop=False, stop_on_mute=True, tight=True)
    renpy.music.register_channel("wait_sfx", mixer="sfx", loop=False, stop_on_mute=True, tight=True)

define config.window = "hide"


# --- HELPER LABELS ---

label group_sfx(sound):

    $ renpy.music.play(sound, channel="sound", loop=False, relative_volume=0.5)
    $ renpy.music.pump()

    while renpy.music.is_playing(channel="sound"):
        $ renpy.pause(0.05, hard=True)

    return

label wait_sfx(sound):

    $ renpy.music.play(sound, channel="sound", loop=False, relative_volume=0.7)
    $ renpy.music.pump()

    while renpy.music.is_playing(channel="sound"):
        $ renpy.pause(0.05, hard=True)

    return

label ambience(sound):

    $ renpy.music.play(
        sound,
        channel="ambience",
        loop=True,
        fadein=1.0,
        relative_volume=0.05
    )

    return


# --- START ---

label start:
    call demo
    return