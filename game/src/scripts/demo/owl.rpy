label demo_owl:
    scene black_bg
    play sound audio.footsteps
    scene owl_house_door_bg with fade #
    show athena_robes_neutral at Position(xalign=0.3)
    show medusa_neutral at Position(xalign=0.5)
    medusa "I've never been in here before." # VA: Cautious wonder.
    play sound audio.keys_jingle
    athena "I know." # VA: Neutral tone.
    athena "You told me that like, ten thousand times already." # VA: Neutral, but with a hint of impatience.
    play sound audio.keys_jingle2
    show athena_robes_annoyed at Position(xalign=0.3)
    athena "s?at?!" # VA: Frustrated swear at the jammed door.
    show medusa_confused at Position(xalign=0.5)
    medusa "Something wrong?" # VA: Concerned check-in.
    athena "No, it's just..." # VA: Slightly embarrassed hesitation. Athena isn't used to asking for help - she's often the one who gives out help to others. 
    athena "I need help opening the door." # VA: Shy, awkward request. Help isn't something Athena is used to asking for, and she doesn't know how to do it.
    pause 2.0
    medusa "I wanted to shy away at first when I heard that." # Medusa begins to pull away. Beginning of internal monologue, conflicted.
    medusa "Not because I didn't want to help Athena." # VA: Internal monologue, conflicted. Her mind is beginning to race with worst-case scenarios.
    medusa "But because I was afraid of what might happen if I did." # VA: Internal monologue, anxious vulnerability. We start to see what Medusa's fears are.
    scene black_bg with fade
    pause 2.0
    scene owl_house_door_medusa_cg with dissolve
    medusa "I could be a trap." # VA: Internal monologue, fearful.
    medusa "It had happened before." # VA: Internal monologue, bitter memory.
    medusa "Athena is going to push me inside and lock me in there with the owls." # VA: Internal monologue, spiraling worst-case fear. She's catostrophizing hard.
    scene owl_house_door_artemis_cg with fade
    medusa "Then Artemis will appear and join in on the fun by laughing at me like a pair of harpies." # VA: Internal monologue, dread mixed with resentment.
    play sound audio.artemis_laugh
    medusa "And that will be it for me." # VA: Internal monologue, dramatic dread.
    medusa "Pecked to death by owls, hawks, and whatever else was in here." # VA: Internal monologue, darkly vivid fear.
    medusa "All because I put my trust in Athena." # VA: Internal monologue, wounded caution.
    scene owl_house_door_bg
    show athena_robes_angry at Position(xalign=0.3)
    show medusa_sad at Position(xalign=0.5)
    athena "MEDUSA!" # VA: Sharp snap to break Medusa out of her sprialing mind.
    medusa "..." # VA: Blank beat, caught off-guard.
    show medusa_confused at Position(xalign=0.5)
    medusa "What?" # VA: Confused, defensive. She doens't know how much time she's spent spiraling in her own head. 
    show athena_robes_annoyed at Position(xalign=0.3)
    athena "...The door?" # VA: Pointed reminder, trying to stay patient with her priestess.
    show medusa_nervous at Position(xalign=0.5)
    medusa "Oh, right." # VA: Sheepish, quick recovery.
    medusa "The door." # VA: Quick self-correction.
    show athena_robes_neutral at Position(xalign=0.3)
    athena "Are you going to help me with it, or not?" # VA: Firm but not cruel. She can sense Medusa is zoning in and out. 
    show medusa_sad at Position(xalign=0.5)
    medusa "Well..." # VA: Hesitant. Uncertain.
    menu m_owl_door:
        "What do you choose?"
        "Help Athena open the door":
            $ friends += 1
            $ lovers += 1
            show medusa_helping_athena_cg
            medusa "Okay, I can do this. Nothing is going to happen. I can do this." # VA: Internal monologue. Shaky confidence.
            medusa "Many hands make light work, right?" # VA: Quick attempt at upbeat teamwork after a long period of internal monologue and spiraling.
            athena "Yes, it does." # VA: Encouraging agreement.
            medusa "Alright, on three!" # VA: Rallying energy.
            medusa "One... Two... Three!" # VA: Count with effort and momentum and some slight comedic timing.
            scene black_bg with fade
            play sound audio.door_open # ?
            play sound audio.footsteps
            pause 1.0
        "Refuse to help Athena":
            $ enemies += 1
            $ rivals += 1
            show medusa_refusing_athena_cg
            medusa "I'm sure you can open it on your own, Athena." # VA: Polite refusal with distance.
            play sound audio.athena_sigh
            athena "Fine, I'll do it myself then." # VA: Controlled disappointment. She isn't happy, but somewhat expecting this from Medusa.
            athena "Remember though, this Goddess-Priestess relationship is a two-way street." # VA: Firm reminder of responsibility.
            scene black_bg with fade
            play sound audio.door_open # ?
            play sound audio.footsteps
            pause 1.0
    play ambience audio.mews loop # ?
    show owl_house_interior_bg with fade
    show medusa_happy at Position(xalign=0.7) with dissolve
    show athena_robes_happy at Position(xalign=0.3) with dissolve
    medusa "Wow..." # VA: Breathless awe.
    athena "Welcome to the Owl House, Medusa!" # VA: Warm, inviting pride. This is a place Athena is proud of, and she wants to share it with her priestess.
    medusa "Athena, this place is amazing!" # VA: Genuine excitement.
    athena "I know, right?" # VA: Pleased that Medusa sees how great it is.
    athena "It's like my own little pond." # VA: Soft personal admission.
    show medusa_eyebrow at Position(xalign=0.7)
    medusa "Your own little pond?" # VA: Slightly curious. Beginning of a heartfelt conversation.
    pause 2.0
    show athena_robes_neutral at Position(xalign=0.3)
    athena "Well, yeah..." # VA: Slightly shy opening up. # She isn't used to baring her soul like this to someone else.
    athena "I come here at times..." # VA: Reflective, gentle.
    athena "When everything is just too much for me to handle." # VA: Honest vulnerability.
    athena "When I just want to be alone with my thoughts." # VA: Quiet and introspective. Not unlike Medusa with her pond. 
    athena "And with my owls." # VA: Fond warmth. Not unlike Medusa with her snakes.
    show medusa_surprised at Position(xalign=0.7)
    medusa "Wait, all the owls here are yours?" # VA: Surprised curiosity, incredulous.
    pause 2.0
    show athena_robes_neutral at Position(xalign=0.3) # Athena's made a mistake. She doesn't make too many mistakes.
    athena "No, just the one." # VA: Casual correction. Athena's made a mistake.
    athena "The rest of them are just...offcuts the Moirai don't know what to do with yet." # VA: Matter-of-fact, but a little awkward admission. 
    show medusa_happy at Position(xalign=0.7)
    medusa "So, Pallas Athena has only one furbaby then?" # VA: Playful tease. She's good at getting under the skin of her Goddess. 
    show athena_robes_annoyed at Position(xalign=0.3)
    play sound audio.athena_sigh
    athena "I hate that term." # VA: Dry annoyance.
    athena "So very much." # VA: Dead serious emphasis.
    show athena_robes_neutral at Position(xalign=0.3)
    athena "But yes, I only have the one." # VA: Resigned confirmation.
    show medusa_eyebrow at Position(xalign=0.7)
    medusa "I see." # VA: Taking it all in. A thoughtful pause, as she processes the information.
    pause 1.0
    show medusa_excited at Position(xalign=0.7)
    medusa "Can I see it?" # VA: Eager ask, quick pivot. 
    show athena_robes_annoyed at Position(xalign=0.3)
    athena "...What?" # VA: Briefly thrown off by the question. She isn't used to people asking to see her owl.
    show medusa_excited at Position(xalign=0.7)
    medusa "Can I see Ms. Athena's furbaby?" # VA: Deliberately teasing repeat, with an emphasis onike "furbaby."
    show athena_robes_neutral at Position(xalign=0.3)
    athena "Only to stop you from crying about furbabies like a schoolgirl with scabby knees." # VA: Dry comment, but not truly mean.
    show medusa_angry at Position(xalign=0.7)
    medusa "HEY!" # VA: Offended yelp.
    show athena_robes_blue_call_minerva at Position(xalign=0.3)
    athena "MINERVA!" # VA: Loud call. Practiced thousands of times down the years. 
    scene black_bg with fade
    pause 2.0
    show minerva_owl_cg with fade
    medusa "Wow, it's so cute!" # VA: Childlike wonder.
    athena "She, not it." # VA: Gentle correction. Athena doesn't like people referring to her owl as "it."
    medusa "Sorry..." # VA: Quick apology.
    medusa "SHE." # VA: Self-correction with emphasis.
    medusa "Is really cute!" # VA: Bright enthusiasm.
    athena "Minerva is my owl." # VA: Soft pride.
    medusa "You named her after the Roman version of yourself?" # VA: Curious and lightly teasing. The first hint of how much the Gods know about us. 
    athena "Well, I thought it was a fitting name for her." # VA: Modest, affectionate.
    athena "She's my little Minerva, after all." # VA: Warm tenderness.
    medusa "I thought she would be white instead of brown." # VA: Innocent observation.
    athena "Why? She's a barn owl, Medusa." # VA: Practical correction.
    medusa "I don't know, humans always draw you with a white owl." # VA: Casual explanation.
    medusa "But it makes sense that you'd have a brown one, since you have brown hair and all." # VA: Rambling logic, trying to be nice.
    pause 2.0
    athena "I'm auburn, actually." # VA: Corrective but composed.
    medusa "What?" # VA: Confused reaction.
    athena "My hair isn't brown; it's auburn." # VA: Patient clarification.
    medusa "Oh, right. Sorry about that." # VA: Sheepish apology.
    athena "It's fine." # VA: Reassuring, no hard feelings.
    medusa "I'm just sorta colourblind." # VA: Honest confession.
    athena "...I see." # VA: Soft, understanding beat.
    pause 2.0
    medusa "...Can I hold her?" # VA: Careful, hopeful ask.
    athena "Sure, be careful though." # VA: Trusting but cautious.
    scene black_bg with fade
    athena "Here you go." # VA: Gentle handoff.
    play sound audio.ruffled_feathers
    medusa "Oh boy, she's heavy!" # VA: Surprised strain.
    athena "Relax, she isn't going to bite." # VA: Calm reassurance.
    athena "Yet." # VA: Dry joke.
    medusa "Yet?" # VA: Alarmed squeak.
    athena "She only tried to nip my eyes out the first time I held her." # VA: Deadpan anecdote.
    medusa "That's not helping, you know." # VA: Nervous complaint.
    show medusa_holding_owl_cg with fade
    medusa "Once it became clear to me that Minerva wasn't going to devour me, I relaxed a little bit." # Internal monologue
    medusa "I even let myself stare dreamily into her big, round eyes." # VA: Internal monologue, softened and tender.
    medusa "They were a grey colour." # VA: Internal monologue, lingering observation.
    medusa "The same as my..." # VA: Internal monologue, trailing realization.
    pause 2.0
    if lovers >= 2:
        medusa "Goddess." # VA: Reverent whisper.
        pause 2.0
        medusa "I wondered if the stories were true." # VA: Internal monologue, hushed curiosity.
        medusa "That Athena used Minerva to spy on others." # VA: Internal monologue, fascinated rumor recall.
        medusa "That she could see through Minerva's eyes and hear through her ears." # VA: Internal monologue, awe mixed with nerves.
        medusa "If they were, it meant I was staring into my goddess's eyes right now." # VA: Internal monologue, intimate realization.
        medusa "Something which, as my skin prickled with goosebumps, I didn't mind in the slightest." # VA: Internal monologue, breathy and entranced.
    elif enemies >= 2 or rivals >= 2:
        play sound audio.owl_squeaking
        medusa "Ugh." # VA: Irritated grunt.
        medusa "Keeper of furbabies." # VA: Snarky mutter.
        medusa "By the Goddesses, do these things squeak!" # VA: Exasperated complaint.
    else:
        medusa "Well, new friend." # VA: Internal monologue, tentative warmth.
        medusa "..." # VA: Internal pause, letting the word settle.
        medusa "Friend." # VA: Internal monologue, testing the word.
        medusa "It sounded strange when I described her like that." # VA: Internal monologue, surprised by her own feelings.
        medusa "I couldn't even recall the last time I had a friend." # VA: Internal monologue, lonely reflection.
        medusa "..." # VA: Internal pause, emotional beat.
        medusa "And yet, I wished I'd had one sooner." # VA: Internal monologue, soft regret.
        medusa "This new feeling within me was strange." # VA: Internal monologue, cautious wonder.
        medusa "And I didn't want to let it go." # VA: Internal monologue, quiet longing.
    stop ambience fadeout 0.5
    return
