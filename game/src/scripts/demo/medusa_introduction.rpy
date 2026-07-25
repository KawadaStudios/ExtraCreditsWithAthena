label demo_medusa_introduction:
    scene bg_black
    play ambience audio.medusa_alarm_1 loop # ?
    unkown_character "Ugh..." # VA: Groggy, annoyed.
    unkown_character "Not again..." # VA: Groggy, annoyed, exasperated.
    play sound audio.medusa_bed # ?
    stop ambience fadeout 0.2
    play sound audio.medusa_sigh_relief
    unkown_character "There we go..." # VA: Relieved, relaxed.
    pause 3.0
    play ambience audio.medusa_alarm_2 loop # ?
    unkown_character "Ugh!" # VA: Groggy, head pain. 
    play sound audio.medusa_bed # ?
    stop ambience fadeout 0.2
    play sound audio.medusa_sigh_relief_2
    unkown_character "Nice and comfy now..." # VA: Purring, relieved as she settles under the covers for a second time. 
    pause 3.0
    play ambience audio.medusa_alarm_3 loop # ?
    unkown_character "For fuck's sake!" # VA: Angry, furious mood. 
    unkown_character "I swear on the phallus of Apollo this thing gets louder every day!" # VA: Angry, furious mood. Medusa edges close to the point of losing her temper.
    pause 2.0
    play sound audio.medusa_bed # ?
    stop ambience fadeout 0.2
    play sound audio.alarm_slam # ?
    scene cg_medusa_slams_alarm with vpunch
    pause 2.0
    scene bg_black
    unkown_character "Finally." # VA: Relieved, exasperated. Medusa has finally silenced the alarm clock.
    pause 2.0
    play sound audio.medusa_sigh
    unkown_character "Mondays." # VA: Groggy distaste for "Mondays."
    unkown_character "The gut punch of the week." # VA: Strong, scornful emphasis on the word "gut punch."
    unkown_character "And that means..." # VA: Slight, horrible realisation dawning on her.
    pause 2.0
    scene cg_medusa_bed
    medusa "Oh no." # VA: Dread. Something horrible is about to happen.
    medusa "I have to head into divine daycare again." # VA: Dread. She really doesn't want to head there. 

    scene cg_title_kawada_studios_presents
    pause 2.0
    scene cg_medusa_teeth_brush
    play sound audio.medusa_teeth_brush # ?
    pause 2.0
    scene cg_title_collab_potatoes
    pause 2.0
    scene cg_medusa_dressed
    play sound audio.medusa_dressed # ?
    pause 2.0
    scene cg_title_kimia_kore_novel
    pause 2.0
    scene cg_medusa_mirror_neutral
    medusa "Focus Meddy, focus." # VA: Medusa's nickname is Meddy. She uses it to calm herself down.
    scene cg_medusa_mirror_happy
    medusa "You can do this." # VA: She says this to herself, trying to psych herself up for the day ahead.
    medusa "Today you ace your final exam..." # VA: Continued excitable pysching herself up.
    medusa "Get the hell out of Olympus University..." # VA: Continued excitable pysching herself up.
    medusa "And step into the myths for good!" # VA: End of excitable pysching herself up. Medusa is ready to take on the day, and the world. 
    scene cg_medusa_door_day
    play sound audio.medusa_door_explosion # ?
    with vpunch
    scene cg_medusa_door_explosion
    medusa "Cowabunga!" # VA: Triumphant exclamation, even after the door explodes off it's hinges. 
    scene cg_title_extra with flash
    pause 2.0
    play sound audio.medusa_hum_skate loop
    scene cg_hallway_medusa_skate # Medusa skating through the hallway.
    scene cg_hallway_medusa_shade # Frontal shot of Medusa trying desperately to look cool, wearing dark shades.
    pause 2.0
    scene cg_sphinx_door
    medusa "FOUND IT!" # VA: Excited squal of joy. One would even think for a moment that Medusa is happy to be in class.
    stop sound fadeout 0.5
    scene bg_black
    play sound audio.door_open # ?
    pause 1.0
    play ambience audio.class_talking loop
    sphinx "Ahem!" # VA: Resounding firm sound. The Sphinx demands, not wants, obedience from her class.
    sphinx "Now class, is everyone ready for the exam?" # VA: Continued resounding firm sound.
    sphinx "Raise your hand if you are!" # VA: Continued resounding firm sound.
    pause 2.0
    sphinx "Good!" # VA: Pleased tone. Everything seems in order. Sphinx is happy with the class' readiness for the exam.
    sphinx "It seems like everyone is ready, except for..." # VA: She notices something is amiss.
    sphinx "Medusa, what are you doing?" # VA: Sudden shock. 
    sphinx "Why do you have a book in your-" # VA: Sudden fear. 
    play sound audio.book_throw
    medusa "FASCIST BASTARD!" # VA: Loud, defiant exclamation. Medusa is angry, and she is not afraid to show it.
    stop ambience fadeout 0.2
    pause 2.0
    scene cg_classroom_sphinx
    sphinx "MEDUSA!" # VA: Loud scream of anger. 
    sphinx "GET OUT OF MY CLASSROOM!" # VA: Explosive scream of anger.
    pause 1.0
    scene bg_black
    play sound audio.door_close # ?
    pause 1.0
    play sound audio.medusa_hallway_footsteps # ?
    pause 1.0
    play ambience audio.zeus_hum loop # VA: Zeus is humming to himself, heads in the cloud, oblivious to the world around him.
    unkown_character "*Humming to himself*"
    pause 2.0
    play sound audio.zeus_door_open # ?
    stop ambience fadeout 0.2
    scene cg_zeus_door_neutral
    scene cg_zeus_door_frown
    play sound audio.zeus_sigh
    scene cg_medusa_office
    scene bg_black with Dissolve(3.0)
    return