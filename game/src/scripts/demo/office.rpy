label demo_office:
    scene black_bg
    call ambience(audio.tapping_desk) # ?
    pause 2.0
    play sound audio.zeus_sigh
    voice voice_demo_office_zeus_01
    zeus "Eight years." # VA: Weary, tired exhale.
    voice voice_demo_office_zeus_02
    zeus "Eight years of this." # VA: Continued weary tone.
    voice voice_demo_office_zeus_03
    zeus "The most troublesome and mischievous student I've ever had." # VA: Continued weary tone.
    voice voice_demo_office_zeus_04
    zeus "In all my years acting as the Rector of Olympus University." # VA: Continued weary tone.
    scene bg zeus_office_bg with Dissolve(3.0)
    show zeus_stern at Position(xalign=0.3)
    show medusa_neutral at Position(xalign=0.7)
    pause 2.0
    voice voice_demo_office_zeus_05
    zeus "Do you know why you are here, Medusa?" # VA: Firm. 
    voice voice_demo_office_medusa_01
    medusa "...Throwing a book at an exchange professor?" # VA: Pretending to be oblivious.
    voice voice_demo_office_zeus_06
    zeus "Well that..." # VA: Matter-of-fact, but not the main point.
    voice voice_demo_office_zeus_07
    zeus "And the fact she's left Olympus University already..." # VA: Building the case.
    voice voice_demo_office_zeus_08
    zeus "Which no doubt has sullied our reputation in the eyes of the other pantheons..." # VA: Deep reputational concern for Olympus.
    voice voice_demo_office_zeus_09
    zeus "All because of you and your reckless behaviour." # VA: Firm reprimand.
    show medusa_sad at Position(xalign=0.7)
    pause 2.0
    show zeus_stern at Position(xalign=0.3)
    stop ambience fadeout 0.2
    pause 1.0
    call wait_sfx(audio.zeus_sigh) # ?
    voice voice_demo_office_zeus_10
    zeus "I'm not giving up on you, Medusa." # VA: Steady resolve. He doesn't want to give up on her. 
    voice voice_demo_office_medusa_02
    medusa "I wish you would, in a way." # VA: Sad, resigned tone. Medusa feels she's a hopeless basket case.
    voice voice_demo_office_medusa_02b
    medusa "We've been at this for eight years now." # VA: Continuation of sad, resigned tone.
    voice voice_demo_office_medusa_02c
    medusa "And I still feel like the same dolt I was when I first came here." # VA: Continuation of sad, resigned tone.
    voice voice_demo_office_medusa_02d
    medusa "It's hopeless." # VA: Continuation of sad, resigned tone.
    voice voice_demo_office_medusa_02e
    medusa "I'll never graduate from Olympus University." # VA: Continuation of sad, resigned tone. She really does believe this, that she'll never graduate. 
    call wait_sfx(audio.medusa_sigh) # ?
    pause 2.0
    show zeus_determined at Position(xalign=0.3)
    voice voice_demo_office_zeus_11
    zeus "That's why the faculty and I have decided to take a different approach with you." # VA: Testing the waters, but still firm.
    show medusa_surprised at Position(xalign=0.7)
    voice voice_demo_office_medusa_03
    medusa "Huh, what's that?" # VA: Surprised, tone. It causes Medusa to perk up a little. 
    voice voice_demo_office_zeus_13
    zeus "Do you know who Athena is?" # VA: Probing question.
    pause 2.0 # A Beat to let the question sink in.
    voice voice_demo_office_medusa_04
    medusa "Athena?" # VA: Confused. Medusa knows who Athena, but she doesn't know why Zeus is asking her about her.
    voice voice_demo_office_zeus_14
    zeus "Yes, Athena." # VA: Patient.
    voice voice_demo_office_medusa_05
    medusa "You mean Pallas Athena? Your daughter?" # VA: Still confused, but now a little more curious.
    show zeus_neutral at Position(xalign=0.3)
    voice voice_demo_office_zeus_15
    zeus "Yes, is there anything wrong with that?" # VA: Patient, considerate.
    voice voice_demo_office_medusa_06
    medusa "No, no, it's just..." # VA: Trying to play it cool, but still her nerves are getting the better of her.
    voice voice_demo_office_zeus_16
    zeus "You do know who Athena is, don't you?" # VA: Incredulous, getting impatient.
    show medusa_nervous at Position(xalign=0.7)
    show zeus_neutral at Position(xalign=0.3)
    pause 2.0
    voice voice_demo_office_medusa_07
    medusa "Of course I knew who Athena was." # VA: Beginning of Medusa's internal monologue.
    voice voice_demo_office_medusa_07b
    medusa "Who didn't?" # VA: She finds it hard to believe that Zeus would even ask her such a question.
    voice voice_demo_office_medusa_07c
    medusa "She was the perfect student." # VA: Not praise, not envious, but the reality of Athena's character.
    voice voice_demo_office_medusa_07d
    medusa "Brilliant, clever, selfless and not going to be spending the rest of her life on campus like me." # VA: Medusa can see the contrast between herself and Athena, and it makes her feel even worse about herself.
    voice voice_demo_office_medusa_07e
    medusa "She was everything that I wasn't." # VA: Medusa's internal monologue, sharp, overtly critical of herself.
    play sound audio.medusa_sigh_2
    pause 1.0
    voice voice_demo_office_zeus_17
    zeus "Athena is nearing the end of her Goddess degree here at Olympus University." # VA: Brief explanation.
    voice voice_demo_office_zeus_18
    zeus "But before she can graduate, she has to complete a final project." # VA: The setup.
    pause 2.0
    show medusa_annoyed at Position(xalign=0.7)
    voice voice_demo_office_medusa_08
    medusa "Which is...?" # VA: Annoyed tone. She can sense Zeus is planning something, and wants him to get on with it.
    show zeus_determined at Position(xalign=0.3)
    voice voice_demo_office_zeus_19
    zeus "She has to take on a student as a follower and guide them..." # VA: Careful reveal.
    voice voice_demo_office_medusa_09
    medusa "So I am to be her test monkey then?" # VA: Quick cut-in. She's beginning to feel defensive once more. 
    play sound audio.zeus_sigh
    show zeus_tired at Position(xalign=0.3)
    pause 1.0
    voice voice_demo_office_zeus_20
    zeus "Not a test monkey, Medusa." # VA: Gently correcting.
    voice voice_demo_office_zeus_21
    zeus "A follower." # VA: Deliberate emphasis.
    voice voice_demo_office_zeus_22
    zeus "A priestess, if you will." # VA: Reframing the role in a more mythology-friendly way.
    show medusa_eyebrow at Position(xalign=0.7)
    voice voice_demo_office_medusa_10
    medusa "So I have to be her priestess?" # VA: Raised eyebrow, incredulous. She can't believe what she's hearing.
    voice voice_demo_office_medusa_11
    medusa "And she will be my...?" # VA: Continued incredulous tone. She can't believe what she's hearing.
    voice voice_demo_office_zeus_23
    zeus "Goddess, of course." # VA: Bingo, the perfect word to describe Athena's role in this arrangement.
    pause 2.0
    show medusa_neutral at Position(xalign=0.7)
    voice voice_demo_office_medusa_12
    medusa "I see." # VA: Neutral tone. Medusa is quietly processing what she's heard. 
    voice voice_demo_office_medusa_13
    medusa "I started to mull the idea in my mind." # VA: Beginning of Medusa's internal monologue. She isn't sure what to make of it. 
    voice voice_demo_office_medusa_14
    medusa "This was the Rector's incredibly bizarre way of saying..." # VA: Continued internal monologue. It really does come off as bizarre to her. 
    voice voice_demo_office_medusa_14b
    medusa "Yes Medusa, you're quite the troublemaker..." # VA: Continued internal monologue. She can see the truth in it, but it still stings.
    voice voice_demo_office_medusa_15
    medusa "And we need someone to chaperone and keep an eye on you..." # VA: Continued internal monologue. Feels like something from a 90's sitcom, but she can see the truth in it.
    voice voice_demo_office_medusa_16
    medusa "So here's my daughter, only a few credits shy of graduating and you can be her final project." # VA: Continued internal monologue. Zeus pragmatic solution is not lost on her. 
    voice voice_demo_office_medusa_17
    medusa "..." # VA: Internal monologue pause, quietly overwhelmed.
    pause 2.0
    show zeus_neutral at Position(xalign=0.3)
    voice voice_demo_office_zeus_24
    zeus "This will kill two griffons with one stone." # VA: Practical optimism.
    voice voice_demo_office_zeus_25
    zeus "Are you up for it, Medusa?" # VA: Gentle, probing question, but he really wants her to do it.
    pause 1.0
    menu m_choice:
        "What do you choose?"
        "Umm...":
            show medusa_confused at Position(xalign=0.7)
            voice voice_demo_office_medusa_18
            medusa "I mean..." # VA: Hesitant, unsure.
            voice voice_demo_office_medusa_18b
            medusa "I don't have much of a choice, do I?" # VA: Resigned, but still hoping for a way out.
            voice voice_demo_office_zeus_26
            zeus "No, you don't. But I know you can do it, Medusa." # VA: Firm encouragement.
    pause 1.0
    play sound audio.medusa_sigh_2
    voice voice_demo_office_medusa_19
    medusa "It could be a change." # VA: Beginning of Medusa's internal monologue. Medusa is trying to find a silver lining in this arrangement.
    voice voice_demo_office_medusa_19b
    medusa "A fresh start." # VA: Continued internal monologue.
    voice voice_demo_office_medusa_19c
    medusa "But I wasn't sure if Athena and I would click." # VA: Continued internal monologue. She's lowkey worried if her and Athena will even get along.
    voice voice_demo_office_medusa_19d
    medusa "At all." # VA: End of internal monologue.
    pause 1.0
    voice voice_demo_office_zeus_27
    zeus "...I can't force it upon you, of course." # VA: Softening his tone.
    voice voice_demo_office_zeus_28
    zeus "But Athena's well versed in all the subjects you struggle with." # VA: Practical reassurance.
    voice voice_demo_office_zeus_29
    zeus "And I'm sure she can help you out with your studies." # VA: Confident reassurance.
    pause 1.0
    voice voice_demo_office_medusa_20
    medusa "It could even be a chance to make a new friend." # VA: Beginning and end of Medusa's internal monologue. A much softer, reflective tone. 
    pause 2.0
    show medusa_happy at Position(xalign=0.7)
    voice voice_demo_office_medusa_21
    medusa "Alright, I'll give it a shot." # VA: Happy, excited tone. Medusa for the first time since coming to Zeus office, appears to be in better spirits.
    show zeus_happy at Position(xalign=0.3)
    voice voice_demo_office_zeus_30
    zeus "Wonderful news, Medusa!" # VA: Delighted.
    voice voice_demo_office_zeus_31
    zeus "I'll send her a letter to fetch her later on!" # VA: Excited momentum.
    show medusa_confused at Position(xalign=0.7)
    voice voice_demo_office_medusa_22
    medusa "Umm, I think it would be easier to phone her instead." # VA: Practical, matter-of-fact. They live on a modern campus, after all. It's not like they have to send letters anymore like in Ancient Greece.
    show medusa_neutral at Position(xalign=0.7)
    voice voice_demo_office_zeus_32
    zeus "Right! Phone her! Will do!" # VA: Quick enthusiastic pivot.
    voice voice_demo_office_medusa_23
    medusa "...I'll take my leave then." # VA: Polite, neutral tone. She doesn't want to stay and see Zeus get too excited about this arrangement. 
    hide medusa_neutral with Dissolve(0.5)
    play sound audio.medusa_hallway_footsteps # ?
    play sound audio.zeus_door_open # ?
    pause 1.0
    show zeus_excited at Position(xalign=0.3)
    voice voice_demo_office_zeus_33
    zeus "YES! YES! YES! YES! YES! YES! YES!" # VA: Explosive celebration. Finally, the Gorgon is out of his hair.
    pause 1.0
    voice voice_demo_office_medusa_24
    medusa "I can still hear you from outside here, you know." # VA: Firm reprimand. Not unlike the ones Zeus gave to her at the start of the scene. 
    show zeus_embarrassed at Position(xalign=0.3)
    voice voice_demo_office_zeus_34
    zeus "Oh, sorry about that. I just got a little excited." # VA: Embarassed comedown.
    pause 1.0
    scene black_bg
    with fade
    return
