label demo_fencing_2:
    scene bg_black
    play sound audio.athena_sigh
    athena "Please stop calling her all those foul names." # Defensive. Even though she doesn't know Medusa, she doesn't like it when others call her names.
    scene bg_fencing
    show sprite_athena_fencing_neutral at Position(xalign=0.5)
    show sprite_dionysus_fencing_angry at Position(xalign=0.7)
    show sprite_nike_angry at Position(xalign=0.3)
    show sprite_hephaestus_angry at Position(xalign=0.9)
    pause 1.0
    voice voice_demo_fencing_2_dionysus_1
    dionysus "Foul language?"
    voice voice_demo_fencing_2_dionysus_2
    dionysus "What about her foul behaviour?"
    show sprite_athena_fencing_annoyed at Position(xalign=0.5)
    pause 1.0
    athena "She just needs a little bit of help, that's all." # VA: Defensive but gentle. Athena is trying to de-escalate.
    show sprite_nike_smug at Position(xalign=0.3)
    play sound audio.nike_snort
    nike "Yes, as if giving her every advantage to pass through Medieval Greek wasn't enough on your father's part." # VA: Snide, snorting.
    hephaestus "Dictionaries, cheat sheets, having other students do her assignments and essays." # VA: Matter-of-fact pile-on.
    voice voice_demo_fencing_2_dionysus_3
    dionysus "Now since our Rector can't solve the problem, he's decided to shift the burden onto his daughter."
    show sprite_athena_fencing_sad at Position(xalign=0.5)
    pause 2.0
    athena "You're just in a bad mood." # Athena's voice lacks any real conviction.
    voice voice_demo_fencing_2_dionysus_4
    dionysus "I'm in a bad mood?"
    voice voice_demo_fencing_2_dionysus_5
    dionysus "What about your father having to deal with that headache for eight years on his own?"
    pause 1.0
    athena "..." # VA: Silent beat. Athena bites back a response.
    voice voice_demo_fencing_2_dionysus_6
    dionysus "He always looks so stressed when he's finished dealing with Snakehead!"
    voice voice_demo_fencing_2_dionysus_7
    dionysus "And then a few months ago, Zeus was almost in tears when he caught her scribbling on the walls of the library with a marker!"
    show sprite_athena_fencing_neutral at Position(xalign=0.5)
    athena "Enough." # VA: Flatly. This is the end of the conversation. Athena is tired of hearing the others pile on about Medusa's misdeeds. 
    athena "I'll see you next week for our next lesson." # VA: Flatly. She wants to get out of this conversation as quickly as possible.
    scene bg_black with fade
    pause 2.0
    play sound audio.athena_fencing_footsteps # ?
    play sound audio.fencing_door_open_close # ?
    pause 1.0
    play sound audio.athena_sigh
    show cg_athena_changing_room
    athena "Am I really just cleaning up my father's mistakes?" # VA: Beginning of Athena's internal monolgue. Ruminating, reflective.
    pause 2.0
    athena "No matter how hard I tried to run away from it..." # VA: Continued internal monologue. She can't escape the reality of her situation.
    athena "Dionysus's words echoed in my mind." # VA: Continued internal monologue. Or escape Dionysus's backbiting words.
    pause 2.0
    athena "Snakehead." # VA: Exasperated. Even the nickname seems to wear Athena down. 
    scene bg_black with Dissolve(3.0)
    return