label demo_fencing:
    scene bg_black
    play ambience audio.fencing loop # ?
    voice voice_demo_fencing_dionysus_1
    dionysus "Crap. Crap. Crap."
    nike "You know, running away from Athena like that isn't going to help you win." # VA: Matter-of-fact.
    voice voice_demo_fencing_dionysus_2
    dionysus "Oh shut up, Nike."
    hephaestus "Listen to her Dionysus." # VA: Worried, steady.
    hephaestus "Before you make the same mistake I did." # VA: Serious warning.
    nike "Obviously, fencing and pint-sized steampunk nerds don't mix." # VA: Playful jab.
    hephaestus "Shut up, Nike." # VA: Flat, gruff.
    voice voice_demo_fencing_dionysus_3
    dionysus "Oh fuck."
    voice voice_demo_fencing_dionysus_4
    dionysus "Fuck! Fuck! Fuck!"
    athena "One..." # VA: Calm count, controlled and confident.
    voice voice_demo_fencing_dionysus_5
    dionysus "OH NO!"
    athena "Two..." # VA: Same calm count, tightening pressure.
    voice voice_demo_fencing_dionysus_6
    dionysus "BY THE FATES, HAVE MERCY!"
    athena "Three..." # VA: Crisp finish to the count, ready to strike.
    stop ambience fadeout 0.2
    play sound audio.fencing2 # ?
    show cg_athena_dionysus_fencing with fade
    voice voice_demo_fencing_dionysus_7
    dionysus "Ugh. You win again, Athena."
    nike "Amazing work, as always." # VA: Warm praise.
    hephaestus "Flawless Victory!" # VA: Like Shao Khan from Mortal Kombat.
    athena "Enough with the video game references!" # VA: Playful annoyance. Athena is trying to restore order.
    athena "Time for a water break." # VA: Coach-like and practical.
    show bg_fencing with fade
    show sprite_athena_fencing_neutral at Position(xalign=0.5) with dissolve
    show sprite_dionysus_fencing_neutral at Position(xalign=0.7) with dissolve
    show sprite_nike_neutral at Position(xalign=0.3) with dissolve
    show sprite_hephaestus_neutral at Position(xalign=0.9) with dissolve
    athena "So guys, what are our plans tonight?" # VA: Casual, friendly reset after training.
    show sprite_nike_excited at Position(xalign=0.3)
    nike "HESTIA'S HOMEBREW!" # VA: Excited exclaim.
    show sprite_dionysus_fencing_tired at Position(xalign=0.7)
    voice voice_demo_fencing_dionysus_8
    dionysus "...We've been there like a billion times already, Nike."
    show sprite_nike_annoyed at Position(xalign=0.3)
    nike "Well, where else could we go then?" # VA: Annoyed pushback.
    nike "Wait, don't tell me it's the Hanging Gardens, Dionysus?" # VA: Annoyed pushback.
    show sprite_hephaestus_curious at Position(xalign=0.9)
    hephaestus "Why not? I've never been." # VA: Curious, casual.
    show sprite_nike_sick at Position(xalign=0.3)
    nike "They make seafood." # VA: Grossed out. 
    hephaestus "So? I thought you'd like that, Nike." # VA: Oblivious, teasing.
    hephaestus "Being buddy-buddy with Professor Poseidon and all." # VA: Joking, still oblivious.
    show sprite_nike_angry at Position(xalign=0.3)
    nike "We're NOT buddies." # VA: Sharp defensive denial. 
    show sprite_nike_embarrassed at Position(xalign=0.3)
    nike "He's just my professor in Marine Biology, that's all." # VA: Embarrassed, flustered, downplaying.
    show sprite_dionysus_fencing_happy at Position(xalign=0.7)
    voice voice_demo_fencing_dionysus_9
    dionysus "And your track & field coach too."
    voice voice_demo_fencing_dionysus_10
    dionysus "And the first person you turn to when you need homework help."
    voice voice_demo_fencing_dionysus_11
    dionysus "And the guy you dote on and make sappy poems about in your spare time."
    voice voice_demo_fencing_dionysus_12
    dionysus "And sometimes he even catches you making lovey-dovey faces at him in class when you think no one is looking."
    show sprite_nike_red at Position(xalign=0.3)
    show sprite_hephaestus_happy at Position(xalign=0.7)
    show sprite_athena_fencing_happy at Position(xalign=0.5)
    play sound audio.hephaestus_snort
    voice voice_demo_fencing_dionysus_13
    dionysus "If I wasn't such a self-induced dullard from all my drunken wine escapades..."
    voice voice_demo_fencing_dionysus_14
    dionysus "I'd suspect you might even have a crush on him, Nike."
    show sprite_nike_angry at Position(xalign=0.3)
    nike "Shut Up." # VA: Angry, full stop.
    athena "I take it that means we're going to the Hanging Gardens then?" # VA: Teasing, pretending to be oblivious.
    athena "We might even get a glimpse of Professor Poseidon there, who knows?" # VA: Teasing, good-natured.
    nike "Shut." # VA: Clipped warning.
    nike "Up." # VA: Hard stop.
    hephaestus "I know the prospect of that just brightens Nike's day, Athena." # VA: Teasing, good-natured.
    play sound audio.athena_snort
    play ambience audio.athena_phone loop # ?
    show sprite_athena_fencing_annoyed at Position(xalign=0.5)
    athena "Gods, who could that be now?" # VA: Annoyed, frustrated. 
    voice voice_demo_fencing_dionysus_15
    dionysus "I wonder what the chances of that are, Hephaestus?"
    voice voice_demo_fencing_dionysus_16
    dionysus "20%%? 30%%? 50%%?"
    hephaestus "Honestly, I'm surprised Nike hasn't arranged a dinner date with Poseidon already." # VA: Deadpan joke.
    hephaestus "Given how relentless her pursuit of him is." # VA: Dry follow-up.
    show sprite_nike_tired at Position(xalign=0.3)
    nike "...Shut up, Hephaestus." # VA: Tired mumble, no fight left. Defeated. 
    show sprite_athena_fencing_phone at Position(xalign=0.5)
    athena "Sorry guys, I have to take this." # VA: Apologetic, polite. Athena doesn't want to be away from her friends, but she has to take the call. 
    show sprite_dionysus_fencing_surprised at Position(xalign=0.7)
    voice voice_demo_fencing_dionysus_17
    dionysus "EVERYONE QUIET DOWN! ATHENA IS ABOUT TO MAKE A VERY IMPORTANT PHONE CALL!"
    show sprite_hephaestus_neutral at Position(xalign=0.9)
    show sprite_nike_neutral at Position(xalign=0.3)
    show sprite_dionysus_fencing_neutral at Position(xalign=0.7)
    stop ambience fadeout 0.2
    play sound audio.phone_click # ?
    show sprite_athena_fencing_call_eyes_open at Position(xalign=0.5)
    athena "Hello?" # VA: Warm and professional.
    zeus "Is this my wondrous daughter I'm speaking to?" # VA: Warm, proud, fatherly, slightly eccentric. 
    pause 1.0
    athena "...Yes, it is." # VA: Polite, but slightly annoyed. Athena doesn't like being called wondrous, even by Zeus. 
    athena "I wished he didn't call me wondrous." # VA: Internal monologue, annoyed, frustrated. This is the only place where Athena gets to vent her frustrations from the outside world. 
    athena "All the praise from everyone else around me was tiresome enough." # VA: Internal monologue, annoyed, frustrated. End of monologue.
    pause 1.0
    show sprite_athena_fencing_call_eyes_closed at Position(xalign=0.5)
    athena "Is there something you wanted to talk to me about, father?" # VA: Polite, but she really wishes she was with her friends. 
    zeus "Yes! I did!" # VA: Excited.
    zeus "How's your schedule looking for this afternoon?" # VA: Curious, fatherly.
    show sprite_athena_fencing_call_eyes_open at Position(xalign=0.5)
    athena "Well, I have to help Hermes go over some notes before his final exam in Latin..." # VA: Neutral, beginning of long-winded explanation.
    pause 1.0
    show sprite_dionysus_fencing_happy at Position(xalign=0.7)
    voice voice_demo_fencing_dionysus_18
    dionysus "...You'd think he'd pick Greek instead, but Latin is the domain of hipster gods, I guess."
    show sprite_nike_angry at Position(xalign=0.3)
    nike "Shush!" # VA: Quick cutoff.
    pause 1.0
    athena "Then I was thinking about heading to the great Alexandrian library to do some research for my final project..." # VA: Continutation of long-winded explanation. 
    athena "Then I have to take a class on the history of the underworld with Persephone..." # VA: Athena doesn't seem to realise (or care) that this is a whole lot for one person to do.
    athena "But since she's on leave right now with custodian Hades, I have to teach the other students in the class for her..." # VA: Continued long-winded explanation, matter-of-fact.
    zeus "Forget all that!" # VA: Abrupt cutoff.
    zeus "Are you free right now?" # VA: Not so sublty asking Athena to drop everything and come to his office.
    pause 1.0
    athena "Umm...I guess I am." # VA: Neutral, suddenly overwhelmed.
    zeus "Great! Come down to my office then, would you?" # VA: Upbeat, decisive.
    zeus "Love you, daughter!" # VA: About to hang up, but still excited.
    athena "Wait, what's this all about?" # VA: Confused, concerned.
    pause 1.0
    zeus "..." # VA: Listening beat.
    zeus "..." # VA: Measured pause.
    athena "...I see." # VA: # Understanding, but disappointed.
    athena "But I did promise Hermes we'd go over his notes together." # VA: Brief pushback.
    zeus "Very well, but please make sure to come to my office after that, all right?" # VA: Relents, but still excited.
    athena "Alright." # VA; Short, clipped. 
    zeus "Love you, my wonderful daughter!" # VA: Zeus loves getting the last word in, even if it means repeating himself.
    athena "...Love you too, father." # Going through the motions, but isn't really feeling it. 
    play sound audio.phone_hangup # ?
    pause 2.0
    show sprite_athena_fencing_annoyed at Position(xalign=0.5)
    athena "Ugh." # Frustrated, annoyed.
    athena "Just my luck for being the Rector's daughter." # Exhausted, exasperated.
    show sprite_nike_worried at Position(xalign=0.3)
    nike "What's wrong, Athena?" # VA: Concerned, gentle.
    athena "It's..." # VA: Athena finds it hard to get the words out. 
    show sprite_dionysus_fencing_neutral at Position(xalign=0.7)
    voice voice_demo_fencing_dionysus_19
    dionysus "Come on." 
    voice voice_demo_fencing_dionysus_20
    dionysus "Spit it out already."
    hephaestus "Yeah, Athena." # VA: Concerned, supportive.
    hephaestus "Tell us." # VA: Gentle push.
    pause 2.0
    athena "...It's Medusa." # VA: Hesitant, nervous but finally gets it out.
    scene bg_black
    return