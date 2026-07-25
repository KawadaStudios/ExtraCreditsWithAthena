label Chapter_2_Athena_Room:
    scene bg_black
    play sound audio.athena_door_shut
    scene bg_black with fade
    athena "Ugh." # VA: Exhausted release.
    athena "That was a long day." # VA: Tired summary.
    athena "I don't know I managed to keep up with snake-" # She catches herself mid sentence.
    pause 1.0
    athena "..." # VA: Quiet pause to gather herself.
    athena "I don't know how I managed to keep up with Medusa." # VA: Overwhelmed reflection.
    athena "She was challenging..." # VA: Honest, tired admission.
    athena "And father expects me to do for the rest of the semester?" # VA: Disbelieving pressure.
    athena "...I don't know if I can do it." # VA: Vulnerable doubt.
    athena "..." # VA: Silent beat.
    athena "..." # VA: Silent beat.
    athena "..." # VA: Silent beat.
    athena "Maybe I should move forward in life, instead of ruminating." # VA: Self-coaching resolve.
    athena "Keep moving forward, and don't look back." # VA: Firm mantra.
    show bg_athena_room with fade
    show sprite_athena_robes_angry at Position(xalign=0.3) with dissolve
    athena "So, what can I do to kill Chronos before Chronos kills me?" # VA: Dark humor masking stress.
    menu athena_room:
        "What do you choose?"
        
        "Alone time with a Vibrator":
            $ lovers += 1
            $ rivals += 1
            show sprite_athena_robes_mouth_covered at Position(xalign=0.3)
            athena "Maybe I should just take a break from all of this." # VA: Tentative self-indulgent thought.
            athena "Alone time." # VA: Quietly decisive.
            athena "With my favourite toy." # VA: Intimate, private confession.
            # show sprite_athena_robes_lust at Position(xalign=0.3)
            athena "Maybe I should just take a break from all this." # VA: Reaffirming the choice.
            athena "I " # VA: Cut-off thought, trailing into silence.
            scene bg_black with fade
            play sound audio.athena_calendar_open
            scene cg_athena_calendar with fade
            pause 2.0
            athena "..." # VA: Wordless beat.
            athena "..." # VA: Wordless beat.
            athena "..." # VA: Wordless beat.
            athena "..." # VA: Wordless beat.
            athena "..." # VA: Wordless beat.
            athena "..." # VA: Wordless beat.
    return