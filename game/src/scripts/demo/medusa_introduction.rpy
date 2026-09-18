label demo_medusa_introduction:
    scene black_bg
    call ambience(audio.medusa_alarm_1) # ?
    pause 5.0
    voice voice_demo_medusa_introduction_medusa_01
    unknown_character "Ugh... Not again..." # VA: Groggy, annoyed.
    call wait_sfx(audio.medusa_bed) # ?
    pause 5.0
    stop ambience fadeout 0.2
    voice voice_demo_medusa_introduction_medusa_02
    unknown_character "There we go..." # VA: Relieved, relaxed.
    pause 3.0
    call ambience(audio.medusa_alarm_2) # ?
    pause 3.0
    voice voice_demo_medusa_introduction_medusa_03
    unknown_character "Ugh!" # VA: Groggy, head pain. 
    call wait_sfx(audio.medusa_bed) # ?
    stop ambience fadeout 0.2
    pause 3.0
    voice voice_demo_medusa_introduction_medusa_04
    unknown_character "Nice and comfy now..." # VA: Purring, relieved as she settles under the covers for a second time. 
    pause 3.0
    call ambience(audio.medusa_alarm_3) # ?
    pause 3.0
    voice voice_demo_medusa_introduction_medusa_05
    unknown_character "For fuck's sake! I swear on the phallus of Apollo this thing gets louder every day!" # VA: Angry, furious mood. 
    pause 3.0
    stop ambience fadeout 0.2
    play wait_sfx(audio.alarm_slam) # ?
    scene medusa_slams_alarm_cg with vpunch
    pause 2.0
    scene black_bg
    voice voice_demo_medusa_introduction_medusa_06
    unknown_character "Finally." # VA: Relieved, exasperated. Medusa has finally silenced the alarm clock.
    pause 2.0
    play wait_sfx(audio.medusa_sigh) # ?
    pause 2.0
    voice voice_demo_medusa_introduction_medusa_07
    unknown_character "Mondays." # VA: Groggy distaste for "Mondays."
    pause 2.0
    voice voice_demo_medusa_introduction_medusa_08
    unknown_character "And that means..." # VA: Slight, horrible realisation dawning on her.
    voice voice_demo_medusa_introduction_medusa_08b
    unknown_character "Oh no." # VA: Dread. Something horrible is about to happen.
    pause 2.0
    scene medusa_bed_cg
    voice voice_demo_medusa_introduction_medusa_09
    medusa "I have to head into divine daycare again." # VA: Dread. She really doesn't want to head there. 

    scene title_kawada_studios_presents_cg
    pause 2.0
    scene medusa_teeth_brush_cg
    play wait_sfx(audio.medusa_teeth_brush) # ?
    pause 2.0
    scene title_collab_potatoes_cg
    pause 2.0
    scene medusa_dressed_cg
    play sound audio.medusa_dressed # ?
    pause 2.0
    scene title_kimia_kore_novel_cg
    pause 2.0
    scene medusa_mirror_neutral_cg
    voice voice_demo_medusa_introduction_medusa_10
    medusa "Focus Meddy, focus." # VA: Medusa's nickname is Meddy. She uses it to calm herself down.
    scene medusa_mirror_happy_cg
    voice voice_demo_medusa_introduction_medusa_10b
    medusa "You can do this." # VA: She says this to herself, trying to psych herself up for the day ahead.
    voice voice_demo_medusa_introduction_medusa_10c
    medusa "Today you ace your final exam..." # VA: Continued excitable pysching herself up.
    voice voice_demo_medusa_introduction_medusa_10d
    medusa "Get the hell out of Olympus University..." # VA: Continued excitable pysching herself up.
    voice voice_demo_medusa_introduction_medusa_10e
    medusa "And step into the myths for good!" # VA: End of excitable pysching herself up. Medusa is ready to take on the day, and the world. 
    scene medusa_door_day_cg
    play sound audio.medusa_door_explosion # ?
    with vpunch
    scene medusa_door_explosion_cg
    scene title_extra_cg with flash
    pause 2.0
    play sound audio.medusa_hum_skate loop
    scene hallway_medusa_skate_cg # Medusa skating through the hallway.
    scene hallway_medusa_shade_cg # Frontal shot of Medusa trying desperately to look cool, wearing dark shades.
    pause 2.0
    scene sphinx_door_cg
    voice voice_demo_medusa_introduction_medusa_11
    medusa "FOUND IT!" # VA: Excited squal of joy. One would even think for a moment that Medusa is happy to be in class.
    stop sound fadeout 0.5
    scene black_bg
    play sound audio.door_open # ?
    pause 1.0
    play ambience audio.class_talking loop
    voice voice_demo_medusa_introduction_sphinx_01
    sphinx "Ahem!" # VA: Resounding firm sound. The Sphinx demands, not wants, obedience from her class.
    voice voice_demo_medusa_introduction_sphinx_02a
    sphinx "Now class, is everyone ready for the exam?" # VA: Continued resounding firm sound.
    voice voice_demo_medusa_introduction_sphinx_03a
    sphinx "Raise your hand if you are!" # VA: Continued resounding firm sound.
    pause 2.0
    voice voice_demo_medusa_introduction_sphinx_04a
    sphinx "Good!" # VA: Pleased tone. Everything seems in order. Sphinx is happy with the class' readiness for the exam.
    voice voice_demo_medusa_introduction_sphinx_05
    sphinx "It seems like everyone is ready, except for..." # VA: She notices something is amiss.
    voice voice_demo_medusa_introduction_sphinx_06
    sphinx "Medusa, what are you doing?" # VA: Sudden shock. 
    voice voice_demo_medusa_introduction_sphinx_07c
    sphinx "Why do you have a book in your-" # VA: Sudden fear.
    play sound audio.book_throw
    voice voice_demo_medusa_introduction_medusa_12
    medusa "FASCIST BASTARD!" # VA: Loud, defiant exclamation. Medusa is angry, and she is not afraid to show it.
    stop ambience fadeout 0.2
    pause 2.0
    scene classroom_sphinx_cg
    voice voice_demo_medusa_introduction_sphinx_08
    sphinx "MEDUSA!" # VA: Loud scream of anger. 
    voice voice_demo_medusa_introduction_sphinx_09a
    sphinx "GET OUT OF MY CLASSROOM!" # VA: Explosive scream of anger.
    pause 1.0
    scene black_bg
    play sound audio.door_close # ?
    pause 1.0
    play sound audio.medusa_hallway_footsteps # ?
    pause 1.0
    play ambience audio.zeus_hum loop # VA: Zeus is humming to himself, heads in the cloud, oblivious to the world around him.
    unknown_character "*Humming to himself*"
    pause 2.0
    play sound audio.zeus_door_open # ?
    stop ambience fadeout 0.2
    scene zeus_door_neutral_cg
    scene zeus_door_frown_cg
    play sound audio.zeus_sigh
    scene medusa_office_cg
    scene black_bg with Dissolve(3.0)
    return