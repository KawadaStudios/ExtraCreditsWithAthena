label demo_office:
    scene bg_black
    play ambience audio.tapping_desk loop
    pause 2.0
    play sound audio.zeus_sigh
    zeus "Eight years." # VA: Weary, tired exhale.
    zeus "Eight years of this." # VA: Continued weary tone.
    zeus "The most troublesome and mischievous student I've ever had." # VA: Continued weary tone.
    zeus "In all my years acting as the Rector of Olympus University." # VA: Continued weary tone.
    scene bg zeus_office with Dissolve(3.0)
    show sprite_zeus_stern at Position(xalign=0.3)
    show sprite_medusa_neutral at Position(xalign=0.7)
    pause 2.0
    zeus "Do you know why you are here, Medusa?" # VA: Firm. 
    medusa "...Throwing a book at an exchange professor?" # VA: Pretending to be oblivious.
    zeus "Well that..." # VA: Matter-of-fact, but not the main point.
    zeus "And the fact she's left Olympus University already..." # VA: Building the case.
    zeus "Which no doubt has sullied our reputation in the eyes of the other pantheons..." # VA: Deep reputational concern for Olympus.
    zeus "All because of you and your reckless behaviour." # VA: Firm reprimand.
    show sprite_medusa_sad at Position(xalign=0.7)
    pause 2.0
    show sprite_zeus_tired at Position(xalign=0.3)
    stop ambience fadeout 0.2
    play sound audio.zeus_sigh
    zeus "I'm not giving up on you, Medusa." # VA: Steady resolve. He doesn't want to give up on her. 
    medusa "I wish you would, in a way." # VA: Sad, resigned tone. Medusa feels she's a hopeless basket case.
    medusa "We've been at this for eight years now." # VA: Continuation of sad, resigned tone.
    medusa "And I still feel like the same dolt I was when I first came here." # VA: Continuation of sad, resigned tone.
    medusa "It's hopeless." # VA: Continuation of sad, resigned tone.
    medusa "I'll never graduate from Olympus University." # VA: Continuation of sad, resigned tone. She really does believe this, that she'll never graduate. 
    play sound audio.medusa_sigh
    pause 2.0
    show sprite_zeus_determined at Position(xalign=0.3)
    zeus "That's why the faculty and I have decided to take a different approach with you." # VA: Testing the waters, but still firm.
    zeus "In order to help you finish your studies." # VA: Reassuring intent.
    show sprite_medusa_surprised at Position(xalign=0.7)
    medusa "Huh, what's that?" # VA: Surprised, tone. It causes Medusa to perk up a little. 
    zeus "Do you know who Athena is?" # VA: Probing question.
    pause 2.0 # A Beat to let the question sink in.
    medusa "Athena?" # VA: Confused. Medusa knows who Athena, but she doesn't know why Zeus is asking her about her.
    zeus "Yes, Athena." # VA: Patient.
    medusa "You mean Pallas Athena?" # VA: Still confused, but now a little more curious.
    medusa "Your daughter?" # VA: Subtle hint that Medusa is starting to understand the situation.
    show sprite_zeus_neutral at Position(xalign=0.3)
    zeus "Yes, is there anything wrong with that?" # VA: Patient, considerate.
    medusa "No, no, it's just..." # VA: Trying to play it cool, but still her nerves are getting the better of her.
    zeus "You do know who Athena is, don't you?" # VA: Incredulous, getting impatient.
    show sprite_medusa_nervous at Position(xalign=0.7)
    pause 2.0
    medusa "Of course I knew who Athena was." # VA: Beginning of Medusa's internal monologue.
    medusa "Who didn't?" # VA: She finds it hard to believe that Zeus would even ask her such a question.
    medusa "She was the perfect student." # VA: Not praise, not envious, but the reality of Athena's character.
    medusa "Brilliant, clever, selfless and not going to be spending the rest of her life on campus like me." # VA: Medusa can see the contrast between herself and Athena, and it makes her feel even worse about herself.
    medusa "She was everything that I wasn't." # VA: Medusa's internal monologue, sharp, overtly critical of herself.
    play sound audio.medusa_sigh
    pause 1.0
    zeus "Athena is nearing the end of her Goddess degree here at Olympus University." # VA: Brief explanation.
    zeus "But before she can graduate, she has to complete a final project." # VA: The setup.
    pause 2.0
    show sprite_medusa_annoyed at Position(xalign=0.7)
    medusa "Which is...?" # VA: Annoyed tone. She can sense Zeus is planning something, and wants him to get on with it.
    show sprite_zeus_determined at Position(xalign=0.3)
    zeus "She has to take on a student as a follower and guide them..." # VA: Careful reveal.
    medusa "So I am to be her test monkey then?" # VA: Quick cut-in. She's beginning to feel defensive once more. 
    play sound audio.zeus_sigh
    show sprite_zeus_tired at Position(xalign=0.3)
    pause 1.0
    zeus "Not a test monkey, Medusa." # VA: Gently correcting.
    zeus "A follower." # VA: Deliberate emphasis.
    zeus "A priestess, if you will." # VA: Reframing the role in a more mythology-friendly way.
    show sprite_medusa_eyebrow at Position(xalign=0.7)
    medusa "So I have to be her priestess?" # VA: Raised eyebrow, incredulous. She can't believe what she's hearing.
    medusa "And she will be my...?" # VA: Continued incredulous tone. She can't believe what she's hearing.
    zeus "Goddess, of course." # VA: Bingo, the perfect word to describe Athena's role in this arrangement.
    pause 2.0
    show sprite_medusa_neutral at Position(xalign=0.7)
    medusa "I see." # VA: Neutral tone. Medusa is quietly processing what she's heard. 
    medusa "I started to mull the idea in my mind." # VA: Beginning of Medusa's internal monologue. She isn't sure what to make of it. 
    medusa "This was the Rector's incredibly bizarre way of saying..." # VA: Continued internal monologue. It really does come off as bizarre to her. 
    medusa "Yes Medusa, you're quite the troublemaker..." # VA: Continued internal monologue. She can see the truth in it, but it still stings.
    medusa "And we need someone to chaperone and keep an eye on you..." # VA: Continued internal monologue. Feels like something from a 90's sitcom, but she can see the truth in it.
    medusa "So here's my daughter, only a few credits shy of graduating..." # VA: Continued internal monologue. Zeus pragmatic solution is not lost on her. 
    medusa "And you can be her final project." # VA: End of internal monologue. It all comes together nicely in her mind when it's described like that. 
    medusa "..." # VA: Internal monologue pause, quietly overwhelmed.
    pause 2.0
    show sprite_zeus_neutral at Position(xalign=0.3)
    zeus "This will kill two griffons with one stone." # VA: Practical optimism.
    zeus "Are you up for it, Medusa?" # VA: Gentle, probing question, but he really wants her to do it.
    pause 1.0
    menu m_choice:
        "What do you choose?"
        "Umm...":
            show sprite_medusa_confused at Position(xalign=0.7)
            medusa "I mean..." # VA: Hesitant, unsure.
            medusa "I don't have much of a choice, do I?" # VA: Resigned, but still hoping for a way out.
            zeus "No, you don't. But I know you can do it, Medusa." # VA: Firm encouragement.
    pause 1.0
    medusa "..." # VA: Internal beat, still uncertain.
    medusa "It could be a change." # VA: Beginning of Medusa's internal monologue. Medusa is trying to find a silver lining in this arrangement.
    medusa "A fresh start." # VA: Continued internal monologue.
    medusa "But I wasn't sure if Athena and I would click." # VA: Continued internal monologue. She's lowkey worried if her and Athena will even get along.
    medusa "At all." # VA: End of internal monologue.
    pause 1.0
    zeus "...I can't force it upon you, of course." # VA: Softening his tone.
    zeus "But Athena's well versed in all the subjects you struggle with." # VA: Practical reassurance.
    zeus "And I'm sure she can help you out with your studies." # VA: Confident reassurance.
    pause 1.0
    medusa "It could even be a chance to make a new friend." # VA: Beginning and end of Medusa's internal monologue. A much softer, reflective tone. 
    pause 2.0
    show sprite_medusa_happy at Position(xalign=0.7)
    medusa "Alright, I'll give it a shot." # VA: Happy, excited tone. Medusa for the first time since coming to Zeus office, appears to be in better spirits.
    show sprite_zeus_happy at Position(xalign=0.3)
    zeus "Wonderful news, Medusa!" # VA: Delighted.
    zeus "I'll send her a letter to fetch her later on!" # VA: Excited momentum.
    show sprite_medusa_confused at Position(xalign=0.7)
    medusa "Umm..." # VA: A bit confused. 
    medusa "I think it would be easier to phone her instead." # VA: Practical, matter-of-fact. They live on a modern campus, after all. It's not like they have to send letters anymore like in Ancient Greece.
    show sprite_medusa_neutral at Position(xalign=0.7)
    zeus "Right! Phone her! Will do!" # VA: Quick enthusiastic pivot.
    medusa "..." # VA: Brief pause before leaving, composed.
    medusa "I'll take my leave then." # VA: Polite, neutral tone. She doesn't want to stay and see Zeus get too excited about this arrangement. 
    hide medusa_neutral with Dissolve(0.5)
    play sound audio.medusa_hallway_footsteps # ?
    play sound audio.zeus_door_open # ?
    pause 1.0
    show sprite_zeus_excited at Position(xalign=0.3)
    zeus "YES! YES! YES! YES! YES! YES! YES!" # VA: Explosive celebration. Finally, the Gorgon is out of his hair.
    pause 1.0
    medusa "I can still hear you from outside here, you know." # VA: Firm reprimand. Not unlike the ones Zeus gave to her at the start of the scene. 
    show sprite_zeus_embarrassed at Position(xalign=0.3)
    zeus "Oh, sorry about that. I just got a little excited." # VA: Embarassed comedown.
    pause 1.0
    scene bg_black
    with fade
    return