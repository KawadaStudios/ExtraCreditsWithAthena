label Ch2_Athena_Room:
    scene black
    play sound audio.athena_door_shut
    scene black with fade
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
    show athena_room_bg with fade
    show athena_robes_angry at Position(xalign=0.3) with dissolve
    athena "So, what can I do to kill Chronos before Chronos kills me?" # VA: Dark humor masking stress.
    menu athena_bedroom_choices:
        "What do you do?":
        "Spend time on the Internet":
            $ friends += 1
            $ enemies += 1
            show athena_robes_lightbulb at Position(xalign=0.3)
            athena "Of course!"
            athena "The internet!"
            athena "By the Moirai, who knows how many hours I've wasted on the internet..."
            athena "Debating all the classical nerds online!"
            athena "I've won every single argument online too!"
            play sound athena_giggle
            scene athena_computer with fade(3.0)
            play sound athena_knuckles
            athena "Alright. Let's see what's happening online today."
            play sound athena_typing
            scene athena_computer_frown
            athena "Ugh."
            athena "I can't believe me and Medusa are making the rounds online already."
            play sound athena_typing
            scene olympus_forum_1
            athena "Ugh."
            athena "LadyOfTheWilds wrote: "
            athena "*Cough* Artemis *Cough*"
            scene artemis_computer
            artemis "Athena and Medusa secretly in a lesbian relationship?" # VA: Shocked, incredulous online comment. Pretending she didn't make it up.
            artemis "Who would've thought the golden girl and the gorgon troublemaker would be OU's hottest new couple?"
            scene apollo_computer
            athena "DefinitelyNotApollo wrote: "
            apollo "Definitely not me. I don't even know how to use a computer."
            scene aphrodite_computer
            athena "SeafoamSweetheart wrote: "
            aphrodite "By the dregs, Artemis is really scraping the bottom of the barrel when it comes to online gossip."
            scene artemis_computer
            artemis "At least I didn't act the gutter rat like you were around Ares." 
            scene ares_computer
            ares "She was just trying to help me out with my love life, Artemis."
            scene artemis_computer
            artemis "With fishnets, you mean."
            scene apollo_computer
            apollo "Are you sure it wasn't fishnet stockings, Artemis?"
            scene ares_computer_angry
            athena "GodOfGains wrote calmly: "
            ares "It's not what you think!"
            ares "Aphrodite and I were just trying to help out Cernunnos..."
            scene apollo_computer
            apollo "Cernunnos?"
            scene aphrodite_computer
            aphrodite "You know the Pothead hanging out in the Art Department, all the time?"
            apollo "Doesn't ring any bells."
            scene artemis_computer
            artemis "...The one always talking about his throuple plans?"
            scene apollo_computer
            apollo "Oh, that guy."
            scene cernunnos_computer
            cernunnos "Did someone call my name?"
            scene athena_computer_angry
            play sound computer_kick
            athena "Ugh."
            athena "That's enough internet for one day."
            scene athena_computer_hunch
            play sound computer_off
            scene black with fade(3.0)

        "Alone time with a Vibrator":
            $ lovers += 1
            $ rivals += 1
            show athena_robes_lust at Position(xalign=0.3)
            athena "Maybe I should just take a break from all of this." # VA: Tentative self-indulgent thought.
            athena "Alone time." # VA: Quietly decisive.
            athena "With my favourite toy." # VA: Intimate, private confession.
            show athena_robes_lust_thinking at Position(xalign=0.3)
            athena "How long has it been?" # VA: Reflective, intimate musing.
            athena "Months now?" # VA: Realization of time passed.
            athena "By the Moirai, helping others with their homework takes up so much time!" # VA: Soft lament.
            scene black with fade 3.0
            play sound drawer_open_close
            show vibrator
            athena "Found it!" 
            scene black_bg with fade 3.0
            play sound vibrator loop
            athena "..." # VA: Brief moan of pleasure.
            athena "Oh, gods..." # VA: Quiet, intimate pleasure.
            athena "Fuck, yes..." # VA: Quiet, intimate pleasure.
            athena "Yes, yes, yes..." # VA: Quiet, intimate pleasure.
            athena "Give it to me, Centaur!"
            athena "..." # VA: Another moan of pleasure.
            pause 1.0
            athena "I was trying to fantasise about a centuar anyway."
            athena "But something else was in the way."
            athena "I'm not sure what it was."
            athena "I couldn't quite focus on the centaur."
            athena "Something about his hairy chest and big strong legs..."
            athena "Just didn't it for me."
            athena "..." # VA: Quiet, intimate reflection.
            athena "This was the fifth time I'd tried."
            athena "And the thought of a centaur hammering me wasn't all that appealing."
            pause 1.0
            athena "Nor the thought of a satyr pounding me from behind either."
            athena "Or a cyclops taking me into his arms and ravishing me."
            athena "Or even a minotaur dragging me into his labyrinth and making me his."
            athena "..."
            athena "Or being with, well..."
            athena "any kind of man at all."
            stop sound vibrator
            show athena_bed with fade
            athena "The thought was there in my mind..."
            athena "And I knew in all the wisdom of my heart that it was true."
            athena "But I kept pushing it away."
            athena "Kept submerging it into the depths of my mind."
            athena "..."
            athena "But it wouldn't leave me, no matter how hard I tried."

        "Late night studying":
            $ friends += 1
            $ enemies += 1
            $ rivals += 1
            show athena_robes_happy at Position(xalign=0.3)
            athena "Of course!"
            athena "How could I forget the chance to do some late-night studying?"
            athena "These moments don't come up everyday, you know."
            scene black with fade(3.0)
            athena "Now, what should I study first?"
            athena "Lyre composition? Or maybe the history of the Olympian pantheon?"
            athena "Professor Poseidon has been teach me a lot about the history of the Olympian pantheon."
            athena "..."
            athena "Why is Medusa so off put by him, anyway?"
            athena "We spar a lot in class..."
            athena "But I don't get the bad feelings she has about him."
            athena "Maybe I should ask her about it."
            play sound book_turn loop
            scene athena_desk_book
            athena "Anyway, I should get back to studying."
            athena "Before he went back to Heliopolis University..."
            athena "Thoth left me a few of his books to study."
            athena "Maybe I should start with the one on the history of the Egyptian sky gods."
            athena "NO! WAIT!" # VA: Quick, excited pivot. 
            athena "What about a quick treatise on the extent of Aten worship?"
            athena "Yes! That's so much more funny!"
            play sound athena_giggle

    scene black with fade
    athena "..." #
    scene athena_bedside
    athena "The moonlight fell like rays onto my skin."
    athena "Pestering me to get down and sleep."
    athena "But I couldn't."
    athena "Even if this was Artemis way of getting under my skin."
    athena "..."
    scene athena_bedside_pallas
    play sound athena_sigh
    athena "What would you do, Pallas?"
    athena "I couldn't turn to anyone else."
    athena "Even if I wanted to."
    athena "..."
    return