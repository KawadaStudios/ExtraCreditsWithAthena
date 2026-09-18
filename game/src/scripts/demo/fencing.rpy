label demo_fencing:
    scene black_bg
    call ambience(audio.fencing) # ?
    voice voice_demo_fencing_dionysus_01
    dionysus "Crap. Crap. Crap."
    voice voice_demo_fencing_nike_01
    nike "Running away from Athena like that isn't going to help you win, you know." # VA: Matter-of-fact.
    voice voice_demo_fencing_dionysus_02
    dionysus "Oh shut up, Nike."
    voice voice_demo_fencing_hephaestus_01
    hephaestus "Listen to her Dionysus." # VA: Worried, steady.
    voice voice_demo_fencing_hephaestus_02
    hephaestus "Before you make the same mistake I did." # VA: Serious warning.
    voice voice_demo_fencing_nike_02
    nike "Obviously, fencing and pint-sized steampunk nerds don't mix." # VA: Playful jab.
    voice voice_demo_fencing_hephaestus_03
    hephaestus "Shut up, Nike." # VA: Flat, gruff.
    voice voice_demo_fencing_dionysus_03
    dionysus "Oh fuck."
    voice voice_demo_fencing_dionysus_04
    dionysus "Fuck! Fuck! Fuck!"
    athena "One..." # VA: Calm count, controlled and confident.
    voice voice_demo_fencing_dionysus_05
    dionysus "OH NO!"
    athena "Two..." # VA: Same calm count, tightening pressure.
    voice voice_demo_fencing_dionysus_06
    dionysus "BY THE FATES, HAVE MERCY!"
    athena "Three..." # VA: Crisp finish to the count, ready to strike.
    stop ambience fadeout 0.2
    play sound audio.fencing2 # ?
    show athena_dionysus_fencing_cg with fade
    voice voice_demo_fencing_dionysus_07
    dionysus "Ugh. You win again, Athena."
    voice voice_demo_fencing_nike_03
    nike "Amazing work, as always." # VA: Warm praise.
    voice voice_demo_fencing_hephaestus_04
    hephaestus "Flawless Victory!" # VA: Like Shao Khan from Mortal Kombat.
    athena "Enough with the video game references!" # VA: Playful annoyance. Athena is trying to restore order.
    athena "Time for a water break." # VA: Coach-like and practical.
    show fencing_bg with fade
    show athena_fencing_neutral at Position(xalign=0.5) with dissolve
    show dionysus_fencing_neutral at Position(xalign=0.7) with dissolve
    show nike_neutral at Position(xalign=0.3) with dissolve
    show hephaestus_neutral at Position(xalign=0.9) with dissolve
    athena "So guys, what are our plans tonight?" # VA: Casual, friendly reset after training.
    show nike_excited at Position(xalign=0.3)
    voice voice_demo_fencing_nike_04
    nike "HESTIA'S HOMEBREW!" # VA: Excited exclaim.
    show dionysus_fencing_tired at Position(xalign=0.7)
    voice voice_demo_fencing_dionysus_08
    dionysus "...We've been there like a billion times already, Nike."
    show nike_annoyed at Position(xalign=0.3)
    voice voice_demo_fencing_nike_05
    nike "Well, where else could we go then?" # VA: Annoyed pushback.
    voice voice_demo_fencing_nike_06
    nike "Wait, don't tell me it's the Hanging Gardens, Dionysus?" # VA: Annoyed pushback.
    show hephaestus_curious at Position(xalign=0.9)
    voice voice_demo_fencing_hephaestus_05
    hephaestus "Why not? I've never been." # VA: Curious, casual.
    show nike_sick at Position(xalign=0.3)
    voice voice_demo_fencing_nike_07
    nike "They make seafood." # VA: Grossed out. 
    voice voice_demo_fencing_hephaestus_06
    hephaestus "So? I thought you'd like that, Nike." # VA: Oblivious, teasing.
    voice voice_demo_fencing_hephaestus_07
    hephaestus "Being close with Professor Poseidon and all." # VA: Joking, still oblivious.
    show nike_angry at Position(xalign=0.3)
    voice voice_demo_fencing_nike_08
    nike "We're NOT close." # VA: Sharp defensive denial. 
    show nike_embarrassed at Position(xalign=0.3)
    voice voice_demo_fencing_nike_09
    nike "He's just my professor in Marine Biology, that's all." # VA: Embarrassed, flustered, downplaying.
    show dionysus_fencing_happy at Position(xalign=0.7)
    voice voice_demo_fencing_dionysus_09
    dionysus "And your track & field coach too."
    voice voice_demo_fencing_dionysus_10
    dionysus "And the first person you turn to when you need homework help."
    voice voice_demo_fencing_dionysus_11
    dionysus "And the guy you dote on and make sappy poems about in your spare time."
    voice voice_demo_fencing_dionysus_12
    dionysus "And sometimes he even catches you making lovey-dovey faces at him in class when you think no one is looking."
    show nike_red at Position(xalign=0.3)
    show hephaestus_happy at Position(xalign=0.7)
    show athena_fencing_happy at Position(xalign=0.5)
    play sound audio.hephaestus_snort
    voice voice_demo_fencing_dionysus_13
    dionysus "If I wasn't such a self-induced dullard from all my drunken wine escapades..."
    voice voice_demo_fencing_dionysus_14
    dionysus "I'd suspect you might even have a crush on him, Nike."
    show nike_angry at Position(xalign=0.3)
    voice voice_demo_fencing_nike_10
    nike "Shut Up." # VA: Angry, full stop.
    athena "I take it that means we're going to the Hanging Gardens then?" # VA: Teasing, pretending to be oblivious.
    athena "We might even get a glimpse of Professor Poseidon there, who knows?" # VA: Teasing, good-natured.
    voice voice_demo_fencing_nike_11
    nike "Shut." # VA: Clipped warning.
    voice voice_demo_fencing_nike_12
    nike "Up." # VA: Hard stop.
    voice voice_demo_fencing_hephaestus_08
    hephaestus "I know the prospect of that just brightens Nike's day, Athena." # VA: Teasing, good-natured.
    play sound audio.athena_snort
    play ambience audio.athena_phone loop # ?
    show athena_fencing_annoyed at Position(xalign=0.5)
    athena "Gods, who could that be now?" # VA: Annoyed, frustrated. 
    voice voice_demo_fencing_dionysus_15
    dionysus "I wonder what the chances of that, Hephaestus?"
    voice voice_demo_fencing_dionysus_16
    dionysus "20%%? 30%%? 50%%?"
    voice voice_demo_fencing_hephaestus_09
    hephaestus "Honestly, I'm surprised Nike hasn't arranged a dinner date with Poseidon already." # VA: Deadpan joke.
    voice voice_demo_fencing_hephaestus_10
    hephaestus "Given how relentless her pursuit of him is." # VA: Dry follow-up.
    show nike_tired at Position(xalign=0.3)
    voice voice_demo_fencing_nike_13
    nike "...Shut up, Hephaestus." # VA: Tired mumble, no fight left. Defeated. 
    show athena_fencing_phone at Position(xalign=0.5)
    athena "Sorry guys, I have to take this." # VA: Apologetic, polite. Athena doesn't want to be away from her friends, but she has to take the call. 
    show dionysus_fencing_surprised at Position(xalign=0.7)
    voice voice_demo_fencing_dionysus_17
    dionysus "EVERYONE QUIET DOWN! ATHENA IS ABOUT TO MAKE A VERY IMPORTANT PHONE CALL!"
    show hephaestus_neutral at Position(xalign=0.9)
    show nike_neutral at Position(xalign=0.3)
    show dionysus_fencing_neutral at Position(xalign=0.7)
    stop ambience fadeout 0.2
    play sound audio.phone_click # ?
    show athena_fencing_call_eyes_open at Position(xalign=0.5)
    athena "Hello?" # VA: Warm and professional.
    voice voice_demo_fencing_zeus_01
    zeus "Is this my wondrous daughter I'm speaking to?" # VA: Warm, proud, fatherly, slightly eccentric. 
    pause 1.0
    athena "...Yes, it is." # VA: Polite, but slightly annoyed. Athena doesn't like being called wondrous, even by Zeus. 
    athena "I wished he didn't call me wondrous." # VA: Internal monologue, annoyed, frustrated. This is the only place where Athena gets to vent her frustrations from the outside world. 
    athena "All the praise from everyone else around me was tiresome enough." # VA: Internal monologue, annoyed, frustrated. End of monologue.
    pause 1.0
    show athena_fencing_call_eyes_closed at Position(xalign=0.5)
    athena "Is there something you wanted to talk to me about, Father?" # VA: Polite, but she really wishes she was with her friends. 
    voice voice_demo_fencing_zeus_02
    zeus "Yes! I did!" # VA: Excited.
    voice voice_demo_fencing_zeus_03
    zeus "How's your schedule looking for this afternoon?" # VA: Curious, fatherly.
    show athena_fencing_call_eyes_open at Position(xalign=0.5)
    athena "Well, I have to help Hermes go over some notes before his final exam in Latin..." # VA: Neutral, beginning of long-winded explanation.
    pause 1.0
    show dionysus_fencing_happy at Position(xalign=0.7)
    voice voice_demo_fencing_dionysus_18
    dionysus "...You'd think he'd pick Greek instead, but Latin is the domain of hipster gods, I guess."
    show nike_angry at Position(xalign=0.3)
    voice voice_demo_fencing_nike_14
    nike "Shush!" # VA: Quick cutoff.
    pause 1.0
    athena "Then I was thinking about heading to the great Alexandrian library to do some research for my final project..." # VA: Continutation of long-winded explanation. 
    athena "Then I have to take a class on the history of the underworld with Persephone..." # VA: Athena doesn't seem to realise (or care) that this is a whole lot for one person to do.
    athena "But since she's on leave right now with custodian Hades, I have to teach the other students in the class for her..." # VA: Continued long-winded explanation, matter-of-fact.
    voice voice_demo_fencing_zeus_04
    zeus "Forget all that!" # VA: Abrupt cutoff.
    voice voice_demo_fencing_zeus_05
    zeus "Are you free right now?" # VA: Not so sublty asking Athena to drop everything and come to his office.
    pause 1.0
    athena "Umm...I guess I am." # VA: Neutral, suddenly overwhelmed.
    voice voice_demo_fencing_zeus_06
    zeus "Great! Come down to my office, would you?" # VA: Upbeat, decisive.
    voice voice_demo_fencing_zeus_07
    zeus "Love you, daughter!" # VA: About to hang up, but still excited.
    athena "Wait, what's this all about?" # VA: Confused, concerned.
    pause 1.0
    athena "...I see." # VA: # Understanding, but disappointed.
    athena "But I did promise Hermes we'd go over his notes together." # VA: Brief pushback.
    voice voice_demo_fencing_zeus_08
    zeus "Very well, but please make sure to come to my office after that, all right?" # VA: Relents, but still excited.
    athena "Alright." # VA; Short, clipped. 
    voice voice_demo_fencing_zeus_09
    zeus "Love you, my wonderful daughter!" # VA: Zeus loves getting the last word in, even if it means repeating himself.
    athena "...Love you too, father." # Going through the motions, but isn't really feeling it. 
    play sound audio.phone_hangup # ?
    pause 2.0
    show athena_fencing_annoyed at Position(xalign=0.5)
    athena "Ugh." # Frustrated, annoyed.
    athena "Just my luck for being the Rector's daughter." # Exhausted, exasperated.
    show nike_worried at Position(xalign=0.3)
    voice voice_demo_fencing_nike_15
    nike "What's wrong, Athena?" # VA: Concerned, gentle.
    athena "It's..." # VA: Athena finds it hard to get the words out. 
    show dionysus_fencing_neutral at Position(xalign=0.7)
    voice voice_demo_fencing_dionysus_19
    dionysus "Come on." 
    voice voice_demo_fencing_dionysus_20
    dionysus "Spit it out already."
    voice voice_demo_fencing_hephaestus_11
    hephaestus "Yeah, Athena. Tell us." # VA: Concerned, supportive.
    pause 2.0
    athena "...It's Medusa." # VA: Hesitant, nervous but finally gets it out.
    scene black_bg
    return
