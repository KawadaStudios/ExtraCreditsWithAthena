# The script of the game goes in this file.

# Declare characters used by this game. The color argument colourises the
# name of the character.
# region Characters
# Main Characters AKA The blossoming lesbians of Olympus University
define a = Character("Athena", color="#ad3303")
define m = Character("Medusa", color="#135b03")

# The Faculty of Olympus University
define z = Character("Zeus", color="#cfc20d") # Head Rector of Olympus University
define p = Character("Poseidon", color="#053582") # Sports Professor and also with a minor in marine biology
define spx = Character("Sphinx", color="#c7a912")
define am = Character("Ahura Mazda", color="#ff69b4") # Head Librarian and also the only one who can read the ancient cuneiform tablets in the library.
define ahr = Character("Ahriman", color="#ff69b4") # Assistant Librarian and Ahura Mazda's daughter.

# Athena and Medusa's Inner Circle
define art = Character("Artemis", color="#009525") # Goddess of the Hunt
define n = Character("Nike", color="#ffffff") # Goddess of Victory, close friend of Athena and idolises Poseidon
define d = Character("Dionysus", color="#6259b4")
define he = Character("Hephaestus", color="#89571d")
define k = Character("Kanaloa", color="#269ca4") # Poseidon's accomplice and transfer student from Hawaii University.
define minv = Character("Minerva", color="#c8aa25") # Athena's Owl and only furbaby, who is a barn owl and not a white owl like most people think.

# Other important characters
define aph = Character("Aphrodite", color="#ffffff")
define are = Character("Ares", color="#ffffff")

# Miscellaneous characters
define anon = Character("???", color="#000000")
define na = Character("Narrator", color="#ffffff")

init python:
    renpy.music.register_channel("ambience", mixer="music", loop=True)

define flash = Fade(0.25, 0.0, 0.5, color="#fff")

# Placeholder image definitions for testing without art
image bg cold_hallway = "placeholder.png"
image bg fencing = "placeholder.png"
image bg forest = "placeholder.png"
image bg hallway = "placeholder.png"
image bg owl_house_door = "placeholder.png"
image bg owl_house_interior = "placeholder.png"
image bg stairs = "placeholder.png"
image bg zeus_office = "placeholder.png"

image cg athena_artemis_fight = "placeholder.png"
image cg athena_changing_room = "placeholder.png"
image cg athena_dionysus_fencing = "placeholder.png"
image cg athena_dissertation = "placeholder.png"
image cg athena_dissertation2 = "placeholder.png"
image cg athena_dissertation3 = "placeholder.png"
image cg athena_medusa_pond = "placeholder.png"
image cg checkers_athena = "placeholder.png"
image cg checkers_athena_win = "placeholder.png"
image cg classroom_sphinx = "placeholder.png"
image cg hallway_medusa_shade = "placeholder.png"
image cg hallway_medusa_skate = "placeholder.png"
image cg medusa_bed = "placeholder.png"
image cg medusa_door = "placeholder.png"
image cg medusa_door_day = "placeholder.png"
image cg medusa_door_explosion = "placeholder.png"
image cg medusa_dressed = "placeholder.png"
image cg medusa_helping_athena = "placeholder.png"
image cg medusa_holding_owl = "placeholder.png"
image cg medusa_mirror_happy = "placeholder.png"
image cg medusa_mirror_neutral = "placeholder.png"
image cg medusa_office = "placeholder.png"
image cg medusa_refusing_athena = "placeholder.png"
image cg medusa_slams_alarm = "placeholder.png"
image cg medusa_teeth_brush = "placeholder.png"
image cg minerva_owl = "placeholder.png"
image cg owl_house_door_medusa = "placeholder.png"
image cg owl_house_door_artemis = "placeholder.png"
image cg poseidon_hallway = "placeholder.png"
image cg office_medusa_chair = "placeholder.png"
image cg sphinx_door = "placeholder.png"
image cg TITLE_collab_potatoes = "placeholder.png"
image cg TITLE_Extra = "placeholder.png"
image cg TITLE_kawada_studios_presents = "placeholder.png"
image cg TITLE_kimia_kore_novel = "placeholder.png"
image cg zeus_door_frown = "placeholder.png"
image cg zeus_door_neutral = "placeholder.png"
image cg_checkers_athena_look_down = "placeholder.png"
image cg_checkers_athena_look_up = "placeholder.png"
image cg_checkers_medusa = "placeholder.png"

image artemis_angry = "placeholder.png"
image artemis_furious = "placeholder.png"
image artemis_laugh = "placeholder.png"
image artemis_neutral = "placeholder.png"

image athena_angry = "placeholder.png"
image athena_annoyed = "placeholder.png"
image athena_blue_call = "placeholder.png"

image athena_bra_annoyed = "placeholder.png"
image athena_bra_happy = "placeholder.png"
image athena_bra_neutral = "placeholder.png"

image athena_concerned = "placeholder.png"
image athena_cringe = "placeholder.png"
image athena_deflated = "placeholder.png"
image athena_determined = "placeholder.png"
image athena_happy = "placeholder.png"
image athena_lightbulb = "placeholder.png"
image athena_mouth_covered = "placeholder.png"
image athena_neutral = "placeholder.png"
image athena_proud = "placeholder.png"
image athena_red = "placeholder.png"
image athena_sigh = "placeholder.png"
image athena_surprised = "placeholder.png"
image athena_thinking = "placeholder.png"
image athena_tired = "placeholder.png"

image athena_fencing_annoyed = "placeholder.png"
image athena_fencing_call_closed = "placeholder.png"
image athena_fencing_call_open = "placeholder.png"
image athena_fencing_neutral = "placeholder.png"
image athena_fencing_phone = "placeholder.png"
image athena_fencing_sad = "placeholder.png"
image athena_fencing_happy = "placeholder.png"

image dionysus_fencing_angry = "placeholder.png"
image dionysus_fencing_happy = "placeholder.png"
image dionysus_fencing_neutral = "placeholder.png"
image dionysus_fencing_surprised = "placeholder.png"
image dionysus_fencing_tired = "placeholder.png"

image hephaestus_angry = "placeholder.png"
image hephaestus_curious = "placeholder.png"
image hephaestus_happy = "placeholder.png"
image hephaestus_neutral = "placeholder.png"

image medusa_angry = "placeholder.png"
image medusa_annoyed = "placeholder.png"
image medusa_confused = "placeholder.png"
image medusa_content = "placeholder.png"
image medusa_dismissive = "placeholder.png"
image medusa_excited = "placeholder.png"
image medusa_eyebrow = "placeholder.png"
image medusa_grin = "placeholder.png"
image medusa_happy = "placeholder.png"
image medusa_nervous = "placeholder.png"
image medusa_neutral = "placeholder.png"

image medusa_pond_annoyed = "placeholder.png"
image medusa_pond_arm_raised = "placeholder.png"
image medusa_pond_blush = "placeholder.png"
image medusa_pond_dismissive = "placeholder.png"
image medusa_pond_eyebrow = "placeholder.png"
image medusa_pond_happy = "placeholder.png"
image medusa_pond_look = "placeholder.png"
image medusa_pond_neutral = "placeholder.png"
image medusa_pond_roll_eyes = "placeholder.png"
image medusa_pond_sad = "placeholder.png"
image medusa_pond_sigh = "placeholder.png"
image medusa_pond_slump = "placeholder.png"
image medusa_pond_smile = "placeholder.png"
image medusa_pond_thinking = "placeholder.png"

image medusa_sad = "placeholder.png"
image medusa_pond_scared = "placeholder.png"
image medusa_shocked = "placeholder.png"
image medusa_smug = "placeholder.png"
image medusa_surprised = "placeholder.png"
image medusa_thoughtful = "placeholder.png"
image medusa_wow = "placeholder.png"

image nike_angry = "placeholder.png"
image nike_annoyed = "placeholder.png"
image nike_embarrassed = "placeholder.png"
image nike_excited = "placeholder.png"
image nike_neutral = "placeholder.png"
image nike_red = "placeholder.png"
image nike_sick = "placeholder.png"
image nike_smug = "placeholder.png"
image nike_tired = "placeholder.png"
image nike_worried = "placeholder.png"

image poseidon_neutral = "placeholder.png"

image zeus_determined = "placeholder.png"
image zeus_embarrassed = "placeholder.png"
image zeus_excited = "placeholder.png"
image zeus_flask = "placeholder.png"
image zeus_happy = "placeholder.png"
image zeus_neutral = "placeholder.png"
image zeus_stern = "placeholder.png"
image zeus_tired = "placeholder.png"

init python:
    renpy.music.register_channel(
        "ambience",
        mixer="music",
        loop=True
    )





# endregion

# label splashscreen:
#     scene black
#     with fade
#     show text "{i}“She was once most beautiful, the jealous aspiration of many suitors. Neptune violated her in Minerva’s temple: the goddess turned away, and hid her chaste eyes behind her aegis.”{/i}\n-Ovid" at truecenter
#     pause 4
#     hide text
#     with dissolve 

# ---START---
label start:
    call demo
    return

# ---demo---
label demo:
    call demo_dissertation
    call demo_medusa_introduction
    call demo_fencing
    call demo_office
    call demo_fencing_2
    call demo_forest
    call demo_stairs
    call demo_owl
    call demo_checkers
    call demo_end
    call demo_poseidon
    return

label demo_dissertation:
    scene black
    play ambience "assets/sfx/DissTalk.ogg" fadein 2.0
    show cg intro_quote_1
    pause 2.0
    show cg intro_quote_2
    pause 2.0
    show cg intro_quote_3
    pause 2.0
    play sound "assets/sfx/wine_tap.ogg"
    z "So, my wonderful daughter, how many PhDs do you have now?"
    a "Ninety-nine, Father."
    z "Ninety-nine PhDs?"
    play sound "assets/sfx/zeus_laugh.ogg"
    z "So that headache you gave me when you were born, it was worth it after all!"
    a "...I'd think so, yes."
    d "So what was the subject of your dissertation this time, Athena?"
    show cg athena_dissertation with fade
    a "Etruscan influences on the development of Greek pottery."
    play sound "assets/sfx/dionysus_drunk.ogg"
    d "And I thought it was the other way around!"
    n "Me too!"
    n "Shows us how much we know about ancient history, huh?"
    play sound "assets/sfx/athena_snort.ogg"
    show cg athena_dissertation2 with fade
    z "A toast then."
    z "To Athena."
    z "My daughter, in case anyone here on Olympus University has lived underneath, well, how shall we say..."
    play sound "assets/sfx/zeus_cough.ogg"
    z "A Persian boulder for the last few years."
    play sound "assets/sfx/crowd_boo.ogg"
    am "I heard that."
    z "Yes, boo all you want. But keep in mind we DO have a few Persian boulders here on campus, so they might take offence to it."
    play sound "assets/sfx/crowd_laugh.ogg"
    am "Hmph."
    z "Anyway, to Athena."
    z "To the most brilliant student in the history of Olympus University."
    z "And the best daughter a father could ever ask for."
    play sound "assets/sfx/crowd_cheer.ogg"
    pause 1.0
    show cg athena_dissertation3 with fade
    stop audio fadeout 0.5
    play audio "assets/sfx/dissertation_question.ogg" loop
    a "Between all the badgering of questions, I realised I should've been happy." # Athena's internal monologue.
    a "I'd completed my 99th dissertation, and graduation from Olympus University was only weeks away."
    a "I should be happy."
    scene black with fade
    pause 1.5
    stop audio
    a "But I wasn't."
    a "Something was missing."
    a "After everything I'd done, I still felt unsatisfied."
    a "Like there was some lost soul hiding underneath a Persian boulder, that I hadn't unearthed yet."
    a "Someone who needed my help."
    pause 0.5
    a "But where?"
    pause 1.0
    return

label demo_medusa_introduction:
    scene black
    play ambience "assets/sfx/medusa_alarm.ogg" loop
    anon "Ugh..."
    anon "Not again..."
    play sound "assets/sfx/medusa_bed.ogg"
    pause 2.0
    anon "Ugh!"
    anon "I swear on the phallus of Apollo this thing gets louder every day!"
    pause 2.0
    play sound "assets/sfx/medusa_bed.ogg"
    stop ambience fadeout 0.2
    play sound "assets/sfx/alarm_slam.ogg"
    scene cg medusa_slams_alarm with vpunch
    pause 2.0
    scene black
    m "Finally."
    pause 2.0
    play sound "assets/sfx/medusa_sigh.ogg"
    m "Mondays."
    m "The gut punch of the week."
    m "And that means..."
    pause 2.0
    scene cg medusa_bed
    m "Oh no."
    m "I have to head into divine daycare again."

    scene cg TITLE_kawada_studios_presents
    pause 2.0
    scene cg medusa_teeth_brush
    play sound "assets/sfx/medusa_teeth_brush.ogg"
    pause 2.0
    scene cg TITLE_collab_potatoes
    pause 2.0
    scene cg medusa_dressed
    play sound "assets/sfx/medusa_dressed.ogg"
    pause 2.0
    scene cg TITLE_kimia_kore_novel
    pause 2.0
    scene cg medusa_mirror_neutral
    m "Focus Meddy, focus."
    scene cg medusa_mirror_happy
    m "You can do this."
    m "Today you ace your final exam..."
    m "Get the hell out of Olympus University..."
    m "And step into the myths for good!"
    scene cg medusa_door_day
    play sound "assets/sfx/medusa_door_explosion.ogg"
    with vpunch
    scene cg medusa_door_explosion
    m "Cowabunga!"
    scene cg TITLE_Extra with flash
    pause 2.0
    play sound "assets/sfx/medusa_hum_skate.ogg" loop
    scene cg hallway_medusa_skate # Medusa skating through the hallway.
    scene cg hallway_medusa_shade # Frontal shot of Medusa trying desperately to look cool, wearing dark shades.
    pause 2.0
    scene cg sphinx_door
    m "FOUND IT!"
    stop sound fadeout 0.5
    scene black
    play sound "assets/sfx/door_open.ogg"
    pause 1.0
    play ambience "assets/sfx/class_talking.ogg" loop
    spx "Ahem!"
    spx "Now class, is everyone ready for the exam?"
    spx "Raise your hand if you are!"
    pause 2.0
    spx "Good!"
    spx "It seems like everyone is ready, except for..."
    spx "Medusa, what are you doing?"
    spx "Why do you have a book in your-"
    play sound "assets/sfx/book_throw.ogg"
    m "FASCIST BASTARD!"
    stop ambience fadeout 0.2
    pause 2.0
    scene cg classroom_sphinx
    spx "MEDUSA!"
    spx "GET OUT OF MY CLASSROOM!"
    pause 1.0
    scene black
    play sound "assets/sfx/door_close.ogg"
    pause 1.0
    play sound "assets/sfx/footsteps.ogg"
    pause 1.0
    play sound "assets/sfx/door_open.ogg"
    pause 1.0
    play sound "assets/sfx/zeus_hum.ogg"
    pause 2.0
    play sound "assets/sfx/door_open.ogg"
    scene cg zeus_door_neutral
    scene cg zeus_door_frown
    play sound "assets/sfx/zeus_sigh.ogg"
    scene cg medusa_office
    scene black with Dissolve(3.0)
    return

label demo_fencing:
    scene black
    play ambience "assets/sfx/fencing.ogg" loop
    d "Crap. Crap. Crap."
    n "You know, running away from Athena like this isn't going to make you win."
    d "Oh shut up, Nike."
    he "Listen to her Dionysus."
    he "Before you make the same mistake I did."
    n "Obviously, fencing and pint-sized steampunk nerds don't mix."
    he "Shut up, Nike."
    d "Oh fuck."
    d "Fuck! Fuck! Fuck!"
    a "One..."
    d "OH NO!"
    a "Two..."
    d "BY THE FATES, HAVE MERCY!"
    a "Three..."
    stop ambience fadeout 0.2
    play sound "assets/sfx/fencing2.ogg"
    show cg athena_dionysus_fencing with fade
    d "Ugh. You win again, Athena."
    n "Amazing work, as always."
    he "Flawless Victory!"
    a "Enough with the video game references!"
    a "Time for a water break."
    show bg fencing with fade
    show athena_fencing_neutral at Position(xalign=0.5) with dissolve
    show dionysus_fencing_neutral at Position(xalign=0.7) with dissolve
    show nike_neutral at Position(xalign=0.3) with dissolve
    show hephaestus_neutral at Position(xalign=0.9) with dissolve
    a "So guys, what are our plans tonight?"
    show nike_excited at Position(xalign=0.3)
    n "HESTIA'S HOMEBREW!"
    show dionysus_fencing_tired at Position(xalign=0.7)
    d "...We've been there like a billion times already, Nike."
    show nike_annoyed at Position(xalign=0.3)
    n "Well, where else could we go then?"
    n "Wait, don't tell me it's the Hanging Gardens, Dionysus?"
    show hephaestus_curious at Position(xalign=0.9)
    he "Why not? I've never been."
    show nike_sick at Position(xalign=0.3)
    n "They make seafood."
    he "So? I thought you'd like that, Nike."
    he "Being buddy-buddy with Professor Poseidon and all."
    show nike_angry at Position(xalign=0.3)
    n "We're NOT buddies."
    show nike_embarrassed at Position(xalign=0.3)
    n "He's just my professor in Marine Biology, that's all."
    show dionysus_fencing_happy at Position(xalign=0.7)
    d "And your track & field coach too."
    d "And the first person you turn to when you need homework help."
    d "And the guy you dote on and make sappy poems about in your spare time."
    d "And sometimes he even catches you making lovey-dovey faces at him in class when you think no one is looking."
    show nike_red at Position(xalign=0.3)
    show hephaestus_happy at Position(xalign=0.7)
    show athena_fencing_happy at Position(xalign=0.5)
    play sound "assets/sfx/hephaestus_snort.ogg"
    d "If I wasn't such a self-induced dullard from all my drunken wine escapades..."
    d "I'd suspect you might even have a crush on him, Nike."
    show nike_angry at Position(xalign=0.3)
    n "Shut Up."
    a "I take it that means we're going to the Hanging Gardens then?"
    a "We might even get a glimpse of Professor Poseidon there, who knows?"
    n "Shut."
    n "Up."
    he "I know the prospect of that just brightens Nike's day, Athena."
    play sound "assets/sfx/athena_snort.ogg"
    play audio "assets/sfx/athena_phone.ogg" loop
    show athena_fencing_annoyed at Position(xalign=0.5)
    a "Gods, who could that be now?"
    d "I wonder what the chances of that are, Hephaestus?"
    d "20%%? 30%%? 50%%?"
    he "Honestly, I'm surprised Nike hasn't arranged a dinner date with Poseidon already."
    he "Given how relentless her pursuit of him is."
    show nike_tired at Position(xalign=0.3)
    n "...Shut up, Hephaestus." # Her voice lacks any real conviction.
    show athena_fencing_phone at Position(xalign=0.5)
    a "Sorry guys, I have to take this."
    show dionysus_fencing_surprised at Position(xalign=0.7)
    d "EVERYONE QUIET DOWN! ATHENA IS ABOUT TO MAKE A VERY IMPORTANT PHONE CALL!"
    show hephaestus_neutral at Position(xalign=0.9)
    show nike_neutral at Position(xalign=0.3)
    show dionysus_fencing_neutral
    stop audio
    play sound "assets/sfx/phone_click.ogg"
    show athena_fencing_call__eyes_open at Position(xalign=0.5)
    a "Hello?"
    z "Is this my wondrous daughter I'm speaking to?"
    pause 1.0
    a "...Yes, it is."
    a "I wished he didn't call me wondrous."
    a "All the praise from everyone else around me was tiresome enough."
    pause 1.0
    a "...Yes, it is."
    show athena_fencing_call_eyes_closed at Position(xalign=0.5)
    a "Is there something you wanted to talk to me about, father?"
    z "Yes! I did!"
    z "How's your schedule looking for this afternoon?"
    show athena_fencing_call_eyes_open at Position(xalign=0.5)
    a "Well, I have to help Hermes go over some notes before his final exam in Latin..."
    pause 1.0
    show dionysus_fencing_happy at Position(xalign=0.7)
    d "...You'd think he'd pick Greek instead, but Latin is the domain of hipster gods, I guess."
    show nike_angry at Position(xalign=0.3)
    n "Shush!"
    pause 1.0
    a "Then I was thinking about heading to the great Alexandrian library to do some research for my final project..."
    a "Then I have to take a class on the history of the underworld with Persephone..."
    a "But since she's on leave right now with custodian Hades, I have to teach the other students in the class for her..."
    z "Forget all that!"
    z "Are you free right now?"
    pause 1.0
    a "Umm...I guess I am."
    z "Great! Come down to my office then, would you?"
    z "Love you, daughter!"
    a "Wait, what's this all about?"
    pause 1.0
    z "..."
    z "..."
    a "...I understand."
    a "But I did promise Hermes we'd go over his notes together."
    z "Very well, but please make sure to come to my office after that, all right?"
    a "Alright."
    z "Love you, my wonderful daughter!"
    a "...Love you too, father."
    play sound "assets/sfx/phone_hangup.ogg"
    pause 2.0
    show athena_fencing_annoyed at Position(xalign=0.5)
    a "Ugh."
    a "Just my luck for being the Rector's daughter."
    show nike_worried at Position(xalign=0.3)
    n "What's wrong, Athena?"
    a "It's..."
    show dionysus_fencing_neutral at Position(xalign=0.7)
    d "Come on."
    d "Spit it out already."
    pause 2.0
    a "...It's Medusa."
    scene black
    return

label demo_office:
    scene black
    play ambience "assets/sfx/tapping_desk.ogg" loop
    pause 2.0
    play sound "assets/sfx/zeus_sigh.ogg"
    z "Eight years."
    z "Eight years of this."
    z "The most troublesome and mischievous student I've ever had."
    z "In all my years acting as the Rector of Olympus University."
    scene bg zeus_office with Dissolve(3.0)
    show zeus_stern at Position(xalign=0.3)
    show medusa_neutral at Position(xalign=0.7)
    stop ambience fadeout 0.2
    pause 2.0
    z "Do you know why you are here, Medusa?"
    m "...Throwing a book at an exchange professor?"
    z "Well that..."
    z "And the fact she's left Olympus University already..."
    z "Which no doubt has sullied our reputation in the eyes of the other pantheons..."
    z "All because of you and your reckless behaviour."
    show medusa_sad at Position(xalign=0.7)
    pause 2.0
    show zeus_tired at Position(xalign=0.3)
    play sound "assets/sfx/zeus_sigh.ogg"
    z "I'm not giving up on you, Medusa."
    m "I wish you would, in a way."
    m "We've been at this for eight years now."
    m "And I still feel like the same dolt I was when I first came here."
    m "It's hopeless."
    m "I'll never graduate from Olympus University."
    play sound "assets/sfx/medusa_sigh.ogg"
    pause 2.0
    show zeus_determined at Position(xalign=0.3)
    z "That's why the faculty and I have decided to take a different approach with you."
    z "In order to help you finish your studies."
    show medusa_surprised at Position(xalign=0.7)
    m "Huh, what's that?"
    z "Do you know who Athena is?"
    pause 2.0
    m "Athena?"
    z "Yes, Athena."
    m "You mean Pallas Athena?"
    m "Your daughter?"
    show zeus_neutral at Position(xalign=0.3)
    z "Yes, is there anything wrong with that?"
    m "No, no, it's just..."
    z "You do know who Athena is, don't you?"
    show medusa_nervous at Position(xalign=0.7)
    pause 2.0
    m "Of course I knew who Athena was."
    m "Who didn't?"
    m "She was the perfect student."
    m "Brilliant, clever, selfless and not going to be spending the rest of her life on campus like me."
    m "She was everything that I wasn't."
    play sound "assets/sfx/medusa_sigh.ogg"
    pause 1.0
    scene bg zeus_office
    with fade
    show zeus_neutral at Position(xalign=0.3)
    show medusa_neutral at Position(xalign=0.7)
    z "Athena is nearing the end of her Goddess degree here at Olympus University."
    z "But before she can graduate, she has to complete a final project."
    pause 2.0
    show medusa_annoyed
    m "Which is...?"
    show zeus_determined
    z "She has to take on a student as a follower and guide them..."
    m "So I am to be her test monkey then?"
    play sound "assets/sfx/zeus_sigh.ogg"
    show zeus_tired at Position(xalign=0.3)
    pause 1.0
    z "Not a test monkey, Medusa."
    z "A follower."
    z "A priestess, if you will."
    show medusa_thoughtful
    m "So I have to be her priestess?"
    m "And she will be my...?"
    z "Goddess, of course."
    pause 2.0
    show medusa_neutral at Position(xalign=0.7)
    m "I see."
    m "I started to mull the idea in my mind."
    m "This was the Rector's incredibly bizarre way of saying..."
    m "Yes Medusa, you're quite the troublemaker..."
    m "And we need someone to chaperone and keep an eye on you..."
    m "So here's my daughter, only a few credits shy of graduating..."
    m "And you can be her final project."
    m "..."
    pause 2.0
    show zeus_neutral at Position(xalign=0.3)
    z "This will kill two griffons with one stone."
    z "Are you up for it, Medusa?"
    pause 1.0
    menu m_choice:
        "What do you choose?"
        "Umm...":
            show medusa_confused at Position(xalign=0.7)
            m "I mean..."
            m "I don't have much of a choice, do I?"
            z "No, you don't. But I know you can do it, Medusa."
    pause 1.0
    m "..."
    m "It could be a change."
    m "A fresh start."
    m "But I wasn't sure if Athena and I would click."
    m "At all."
    pause 1.0
    z "...I can't force it upon you, of course."
    z "But Athena's well versed in all the subjects you struggle with."
    z "And I'm sure she can help you out with your studies."
    pause 1.0
    m "It could even be a chance to make a new friend."
    pause 2.0
    show medusa_happy at Position(xalign=0.7)
    m "Alright, I'll give it a shot."
    show zeus_happy at Position(xalign=0.3)
    z "Wonderful news, Medusa!"
    z "I'll send her a letter to fetch her later on!"
    show medusa_confused at Position(xalign=0.7)
    m "Umm..."
    m "I think it would be easier to phone her instead."
    show medusa_neutral at Position(xalign=0.7)
    z "Right! Phone her! Will do!"
    m "..."
    m "I'll take my leave then."
    hide medusa_neutral with Dissolve(0.5) 
    play sound "assets/sfx/footsteps.ogg"
    play sound "assets/sfx/door_close.ogg"
    pause 1.0
    show zeus_excited at Position(xalign=0.3)
    z "YES! YES! YES! YES! YES! YES! YES!"
    pause 1.0
    m "I can still hear you from outside here, you know."
    show zeus_embarrassed at Position(xalign=0.3)
    z "Oh, sorry about that. I just got a little excited."
    pause 1.0
    scene black
    with fade
    return

label demo_fencing_2:
    scene black
    play sound "assets/sfx/athena_sigh.ogg"
    a "Please stop calling her all those foul names."
    scene bg fencing
    show athena_fencing_neutral at Position(xalign=0.5)
    show dionysus_fencing_angry at Position(xalign=0.7)
    show nike_angry at Position(xalign=0.3)
    show hephaestus_angry at Position(xalign=0.9)
    pause 1.0
    d "Foul language?"
    d "What about her foul behaviour?"
    show athena_fencing_annoyed at Position(xalign=0.5)
    pause 1.0
    a "She just needs a little bit of help, that's all."
    show nike_smug at Position(xalign=0.3)
    play sound "assets/sfx/nike_snort.ogg"
    n "Yes, as if giving her every advantage to pass through Medieval Greek wasn't enough on your father's part."
    he "Dictionaries, cheat sheets, having other students do her assignments and essays."
    d "Now since our Rector can't solve the problem, he's decided to shift the burden onto his daughter."
    show athena_fencing_sad at Position(xalign=0.5)
    pause 2.0
    a "You're just in a bad mood." # Athena's voice lacks any real conviction.
    d "I'm in a bad mood?"
    d "What about your father having to deal with that headache for eight years on his own?"
    pause 1.0
    a "..."
    d "He always looks so stressed when he's finished dealing with Snakehead!"
    d "And then a few months ago, Zeus was almost in tears when he caught her scribbling on the walls of the library with a marker!"
    show athena_fencing_neutral at Position(xalign=0.5)
    a "Enough."
    a "I'll see you next week for our next lesson."
    scene black with fade
    pause 2.0
    play sound "assets/sfx/footsteps.ogg"
    play sound "assets/sfx/door_open.ogg"
    play sound "assets/sfx/door_close.ogg"
    play sound "assets/sfx/athena_sigh.ogg"
    show cg athena_changing_room
    a "Am I really just cleaning up my father's mistakes?"
    pause 2.0
    a "No matter how hard I tried to run away from it..."
    a "Dionysus's words echoed in my mind."
    pause 2.0
    a "Snakehead."
    scene black with Dissolve(3.0)
    return

label demo_forest:
    scene black
    play ambience "assets/sfx/forest_ambience.ogg" loop
    pause 1.0
    m "This is my forest."
    m "Well, technically Groundskeeper Pan's forest, but I like to think of it as mine."
    scene bg forest
    with Dissolve(3.0)
    m "The place I hung out when I wanted to be alone."
    m "The place I went when everything in life was too much for me to handle."
    m "Where I could just be myself and not have to worry about anything."
    show medusa_pond_neutral at Position(xalign=0.7) with dissolve
    m "When I was really down in the dumps, I'd come here and sit inside this pond for hours."
    m "I couldn't get an entry into Pan's forest pool."
    m "The one where the nymphs acted as lifeguards."
    m "And dryads and satyrs had impromptu volleyball matches."
    m "Nobody wanted the gorgon troublemaker around them."
    m "So I had to make my own."
    play audio "assets/sfx/pond_ambience.ogg" loop
    pause 1.0
    show medusa_pond_sigh at Position(xalign=0.7)
    stop audio fadeout 0.5
    play audio "assets/sfx/medusa_sigh.ogg"
    pause 1.0
    m "Things could be a whole lot worse."
    m "I had this place to myself at least."
    m "For now."
    pause 1.0
    play sound "assets/sfx/forest_footsteps.ogg"
    show medusa_pond_look at Position(xalign=0.7)
    m "Huh, who's that?"
    pause 1.0
    play sound "assets/sfx/forest_footsteps.ogg"
    pause 1.0
    a "Σκατά, I have stepped on centaur dung."
    m "Pan is such an uncivilized brute!"
    a "And those were my best sandals too!"
    a "μαλάκα!"
    play sound "assets/sfx/forest_footsteps.ogg"
    play sound "assets/sfx/athena_footsteps.ogg"
    pause 1.0
    show athena_neutral at Position(xalign=0.3)

    a "Medusa Margoyles?"
    show athena_mouth_covered at Position(xalign=0.3)
    play sound "assets/sfx/athena_gasp.ogg"
    play sound "assets/sfx/medusa_ugh.ogg"
    show medusa_pond_roll_eyes at Position(xalign=0.7)
    m "...That's my nickname on campus, dear player."
    pause 1.0
    show medusa_pond_arm_raised at Position(xalign=0.7)
    m "HERE!"
    m "You called?"
    show athena_neutral at Position(xalign=0.3)
    a "I have."
    a "I am Athena, daughter of Zeus and goddess of wis-"
    show medusa_pond_dismissive at Position(xalign=0.7)
    m "Blah, blah, blah. I know who you are."
    show athena_annoyed at Position(xalign=0.3)
    m "You're Athena. The golden girl on campus."
    m "I know all that stuff already."
    pause 2.0
    a "...Well, I'm sure you already know this then, but I'm going to be your mentor for the next few months."
    show medusa_pond_annoyed at Position(xalign=0.7)
    m "Goddess, you mean."
    m "Let's not downplay it."
    m "At all."
    pause 2.0
    a "...Correct. Goddess."
    a "And you are to be my priestess, Medusa."
    menu m_priestess:
        "How do you respond?"
        
        "Keep your mouth shut and nod":
            m "Sure, I guess."
            m "I mean, someone has to help me get through my final year of university, right?"
            a "Yes, that's right."
            m "But I can't hack these tests or exams."
            m "At all."
        
        "Piss Athena off by being sarcastic":
            m "And you're doing all this to get those extra credits, right?"
            m "Finally ascend your way into Goddesshood?"
            m "And leave me and Olympus University in the dust, right?"
            m "Right?"
            show athena_angry at Position(xalign=0.3)
            play sound "assets/sfx/athena_angry.ogg"
            show medusa_pond_scared at Position(xalign=0.7)
            a "Yes, you caught me!"
            a "I'm doing this all for the love of credits!" 
            a "And not because I want to learn to look after someone who chooses to follow me!"
            a "Which is what a goddess would do!"
            show medusa_pond_slump at Position(xalign=0.7)
            pause 2.0
            play sound "assets/sfx/athena_sigh.ogg"
            show athena_tired at Position(xalign=0.3)
            a "I didn't mean to snap like that."
            a "That was...terribly out of character for me."
            pause 2.0
            show medusa_pond_smile at Position(xalign=0.7)
            m "It's okay, I get it."
            m "That usually happens when someone is forced to spend a lot of time with me."
            m "It just happens when you're around poor old Medusa."
            m "The perennial senior who can't get her act together."
            m "Who can't even graduate from university."

    pause 2.0
    a "You just need to study more, Medusa."
    a "I didn't get everything right on my first go, either."
    m "But these tests haven't been my first go in years now!"
    a "I know. That's why I'm here."
    a "To make sure they're your last."
    pause 2.0
    m "I thought I should snap back."
    m "We'd had a bit of a rough start, but I felt at least we'd come to an understanding."
    m "She wanted to help me, and I wanted to be helped."
    m "She wanted to cross the finish line, and get her degree."
    m "...And so did I, deep down."
    pause 2.0
    m "...Does this mean I'm going to have to go through my Greek conjugations right now?"
    m "Anything but that, I thought."
    show athena_happy at Position(xalign=0.3)
    a "No, not yet."
    a "Instead, we'll do something you'd like to do."
    show medusa_pond_eyebrow at Position(xalign=0.7)
    m "Something I like to do?"
    pause 2.0
    m "It was the first time anyone had ever asked me what I wanted to do."
    m "The first time, like ever."
    pause 2.0
    a "Yes. Think of something and we'll do it together."
    show medusa_pond_thinking at Position(xalign=0.7)
    pause 2.0
    m "Well..."
    m "How about..."
    menu m_athena_activity:
        "What do you choose?"

        "The Owl House":
            m "How about The Owl House?"
            show athena_thinking at Position(xalign=0.3)
            a "The Owl House?"
            m "Yeah, the Owl House."
            pause 1.0
            play sound "assets/sfx/athena_lightbulb.ogg"
            show athena_lightbulb at Position(xalign=0.3)
            pause 2.0
            show athena_happy
            a "Oh. You mean the mews!"
            show medusa_pond_roll_eyes at Position(xalign=0.7)
            m "Everyone just calls it the Owl House, Athena."
            pause 2.0
            show medusa_pond_sad at Position(xalign=0.7)
            m "But I've never been."
            show athena_neutral at Position(xalign=0.3)
            a "Why not?"
            pause 2.0
            m "...Snakes and birds of prey don't usually mix."
            m "But if you're there, I might feel safe."
            a "I am the head of it, I suppose."
            a "Alongside a billion other clubs on campus."
            show athena_determined at Position(xalign=0.3)
            a "Very well. I'll show you the Mews."
            m "...The Owl House."
            a "Yes, Owl House!"
            a "...Just get dressed, would you?"
            m "Alright."
            scene black with Dissolve(3.0)
            pause 1.0
        "Get into the pond with me":
            m "Why don't you come in here with me?"
            a "What?"
            m "I'm serious. Get in."
            a "...But I don't have my swimming gear with me."
            m "So? I'm not wearing mine either."
            show athena_red at Position(xalign=0.3)
            m "For a moment, I felt her cheeks flush."
            m "She was embarrassed about stripping down in front of me."
            m "I didn't think she was used to it, even in front of other women."
            m "C'mon, for the day that's in it."
            show athena_neutral at Position(xalign=0.3)
            a "Hmph, alright."
            a "I did say something that you'd like to do."
            m "Yup."
            m "Now get in."
            show athena_bra_neutral at Position(xalign=0.3)
            with dissolve
            show medusa_pond_blush at Position(xalign=0.7)
            m "Oh my."
            show athena_bra_happy at Position(xalign=0.3)
            a "What?"
            m "Nothing."
            m "It's just..."
            a "Just...?"
            pause 2.0
            show medusa_pond_happy at Position(xalign=0.7)
            m "Redheads shouldn't wear red, you know."
            show athena_bra_annoyed at Position(xalign=0.3)
            a "Ugh."
            show medusa_pond_roll_eyes at Position(xalign=0.7)
            m "Just get your butt in here, golden girl!"
            pause 2.0
            scene black with fade
            scene cg athena_medusa_pond with Dissolve(2.0)
            m "See?" 
            m "Not so bad now, is it?"
            a "I guess not."
            scene black with fade
            pause 1.0    
    m "So tell me."
    m "How does this Goddess and Priestess thing work again?"
    stop ambience fadeout 0.5
    return

label demo_stairs:
    scene black
    a "So you've never been inside this place?"
    m "Never. Rector Zeu-"
    pause 2.0
    m "Your daddy."
    a "My daddy?"
    m "Forbade me from coming in."
    a "Please don't call him my daddy, Medusa."
    pause 2.0
    m "...But that's what he is."
    m "Your Daddy."
    a "Medusa..."
    m "You're the one who sprang out of his forehead, not me."
    pause 2.0
    play sound "assets/sfx/athena_ugh.ogg"
    a "Okay. Forget I said anything."
    m "Noted."
    a "So why did my..."
    m "Daddy?"
    a "..."
    a "Esteemed, divine father..."
    a "Forbid you from coming in?"
    pause 2.0
    m "Guess."
    play sound "assets/sfx/athena_ugh.ogg"
    m "Come on! Use that brainpower of yours."
    a "I don't know."
    a "Because snakes and birds don't mix?"
    m "Exactly!"
    a "So it wasn't out of pettiness then."
    m "Your daddy's too soft to be petty, Athena."
    a "..."
    a "I'm going to pretend that didn't conjure up odd images of my father, Medusa."
    pause 1.0
    show bg stairs with dissolve
    show medusa_neutral at Position(xalign=0.5) with dissolve
    show athena_neutral at Position(xalign=0.3) with dissolve
    a "But I'm not sure why you'd think snakes and birds are going to mix now."
    show medusa_happy
    m "Well, I thought if you were at my side..."
    m "Maybe the owls wouldn't nitpick me to death."
    show athena_happy at Position(xalign=0.3)
    play sound "assets/sfx/athena_giggle.ogg"
    a "That won't happen, Medusa."
    a "Not under my watch."
    m "Promise?"
    a "Pinky promi-"
    art "Fetching new luncheon meat for the owls, I see."
    show athena_surprised at Position(xalign=0.3)
    show medusa_surprised at Position(xalign=0.5)
    pause 1.0
    show artemis_neutral at Position(xalign=0.7) with dissolve
    art "Or not."
    art "Maybe a snake sandwich is on the menu today."
    play sound "assets/sfx/artemis_laugh.ogg"
    show medusa_angry at Position(xalign=0.5)
    show athena_angry at Position(xalign=0.3)
    a "Ugh, Artemis. What do you want?"
    art "I just wanted to say hi to my favourite keeper of furballs!"
    art "And handler of snakes!"
    show artemis_laugh at Position(xalign=0.7)
    play sound "assets/sfx/artemis_laugh.ogg"
    show medusa_eyebrow at Position(xalign=0.5)
    m "Hmph."
    m "Still not over me trashing you in paintball, huh?"
    show artemis_angry at Position(xalign=0.7)
    show athena_surprised at Position(xalign=0.3)
    a "You beat Artemis in paintball?"
    play sound "assets/sfx/artemis_grunt.ogg"
    art "We all have our off days."
    show medusa_smug at Position(xalign=0.5)
    m "Sure did."
    m "I've met town bicycles who took fewer shots to the head than Artemis did that day."
    play sound "assets/sfx/artemis_angry.ogg"
    show artemis_furious at Position(xalign=0.7)
    art "WHY YOU LITTLE-"
    play sound "assets/sfx/artemis_scream.ogg"
    scene black with fade
    pause 2.0
    show cg athena_artemis_fight
    play sound "assets/sfx/artemis_cry.ogg"
    a "TO HADES WITH YOU!"
    scene black with fade
    pause 1.0
    play sound "assets/sfx/stairs_crash.ogg"
    pause 1.0
    show bg stairs with fade
    show athena_cringe at Position(xalign=0.3) with dissolve
    a "Ow."
    a "That's going to leave a mark."
    show medusa_wow at Position(xalign=0.7) with dissolve
    m "Wow, Athena. That was..."
    m "AMAZING!"
    show athena_proud at Position(xalign=0.3)
    a "I know, right?"
    a "Osoto Gari is one of my signature moves."
    a "I learned it from Amaterasu, the goddess of the sun."
    a "You remember her, right?"
    m "Of course I do."
    m "She was the substitute PE professor for a while when..."
    pause 2.0
    show medusa_nervous at Position(xalign=0.7)
    a "...When Poseidon was on leave."
    m "Right, Professor Poseidon."
    show athena_concerned at Position(xalign=0.3)
    a "Are you alright?"
    show medusa_content at Position(xalign=0.7)
    m "Yeah, I'm fine."
    a "You sure? You look a little...lightheaded."
    m "Totally fine."
    show medusa_happy at Position(xalign=0.7)
    m "Come on! Let's go see your furbabies!"
    show athena_sigh at Position(xalign=0.3)
    play sound "assets/sfx/athena_sigh.ogg"
    a "You know, I've always hated that nickname."
    show medusa_confused at Position(xalign=0.7)
    m "What, 'furbabies'?"
    m "So you threw archery nerd down the stairs for that?"
    m "Not for me?"
    show athena_happy at Position(xalign=0.3)
    a "Yes. We're not quite there friendship-wise yet."
    a "But eventually you might do something dumb enough for me to protect you."
    show medusa_happy at Position(xalign=0.7)
    m "Glad to hear that."
    play sound "assets/sfx/athena_giggle.ogg"
    a "Anyway, let's go see the owls."
    scene black with fade
    play sound "assets/sfx/footsteps.ogg"
    pause 2.0
    return

label demo_owl:
    scene black
    play sound "assets/sfx/footsteps.ogg"
    scene bg owl_house_door with fade #
    show athena_neutral at Position(xalign=0.3)
    show medusa_neutral at Position(xalign=0.5)
    m "I've never been in here before."
    play sound "assets/sfx/keys_jingle.ogg"
    a "I know."
    a "You told me that like, ten thousand times already."
    play sound "assets/sfx/keys_jingle2.ogg"
    show athena_annoyed at Position(xalign=0.3)
    a "σκατά!"
    show medusa_confused at Position(xalign=0.5)
    m "Something wrong?"
    a "No, it's just..."
    a "I need someone to help me open the door."
    pause 2.0
    m "I wanted to shy away at first when I heard that." # Medusa begins to pull away.
    m "Not because I didn't want to help Athena."
    m "But because I was afraid of what might happen if I did."
    scene black with fade
    pause 2.0
    scene cg owl_house_door_medusa with dissolve
    m "I thought it might be a trap."
    m "It had happened before, after all."
    m "I thought Athena would push me inside and lock me in there with the owls."
    scene cg owl_house_door_artemis with fade
    m "And then Artemis would appear, and join in on the fun by laughing at me."
    play audio "assets/sfx/artemis_laugh.ogg"
    m "That would be the end of me."
    m "Pecked to death by owls, hawks and whatever else was in here."
    m "All because I put my trust in Athena."
    scene bg owl_house_door
    show athena_angry at Position(xalign=0.3)
    show medusa_sad at Position(xalign=0.5)
    a "MEDUSA!"
    m "..."
    show medusa_neutral
    m "What?"
    show athena_annoyed at Position(xalign=0.3)
    a "...The door?"
    show medusa_confused at Position(xalign=0.5)
    m "Oh, right."
    m "The door."
    show athena_neutral at Position(xalign=0.3)
    a "Are you going to help me with it, or not?"
    show medusa_sad at Position(xalign=0.5)
    m "Well..."
    menu m_owl_door:
        "What do you choose?"
        "Help Athena open the door":
            show cg medusa_helping_athena
            m "Many hands make light work, right?"
            a "Yes, it does."
            m "Alright, on three!"
            m "One... Two... Three!"
            scene black with fade
            play sound "assets/sfx/door_open.ogg"
            play sound "assets/sfx/footsteps.ogg"
            pause 1.0
        "Refuse to help Athena":
            show cg medusa_refusing_athena
            m "I'm sure you can open it on your own, Athena."
            play sound "assets/sfx/athena_sigh.ogg"
            a "Alright, I'll do it myself then."
            a "Remember though, this Goddess-Priestess relationship is a two-way street."
            scene black with fade
            play sound "assets/sfx/door_open.ogg"
            play sound "assets/sfx/footsteps.ogg"
            pause 1.0
    show bg owl_house_interior with fade
    show medusa_happy at Position(xalign=0.7) with dissolve
    show athena_happy at Position(xalign=0.3) with dissolve
    m "Wow..."
    a "Welcome to the Owl House, Medusa!"
    m "Athena, this place is amazing!"
    a "I know, right?"
    a "It's like my own little pond."
    show medusa_eyebrow at Position(xalign=0.7)
    m "Your own little pond?"
    pause 2.0
    show athena_neutral at Position(xalign=0.3) # Athena isn't used to baring her soul like this to someone else.
    a "Well, yeah..."
    a "I come here at times..."
    a "When everything is just too much for me to handle."
    a "When I just want to be alone with my thoughts."
    a "And with my owls."
    show medusa_shocked at Position(xalign=0.7)
    m "Wait, all the owls here are yours?"
    pause 2.0
    show athena_neutral at Position(xalign=0.3) # Athena's made a mistake. She doesn't make too many mistakes.
    a "No, just the one."
    a "The rest of them are just...offcuts the Moirai don't know what to do with yet."
    show medusa_happy at Position(xalign=0.7)
    m "So, Pallas Athena has only one furbaby then?"
    show athena_annoyed at Position(xalign=0.3)
    play sound "assets/sfx/athena_sigh.ogg"
    a "I hate that term."
    a "So very much."
    show athena_neutral at Position(xalign=0.3)
    a "But yes, I only have the one."
    show medusa_eyebrow at Position(xalign=0.7)
    m "I see."
    pause 1.0
    show medusa_excited at Position(xalign=0.7)
    m "Can I see it?"
    show athena_annoyed at Position(xalign=0.3)
    a "...What?"
    show medusa_excited at Position(xalign=0.7)
    m "Can I see Ms Athena's furbaby?"
    show athena_neutral at Position(xalign=0.3)
    a "Only to stop hearing you prattle on about furbabies like a schoolgirl with scabby knees."
    show medusa_angry at Position(xalign=0.7)
    m "HEY!"
    show athena_blue_call at Position(xalign=0.3)
    a "MINERVA!"
    scene black with fade
    play audio "assets/sfx/owl_hoots.ogg" loop
    pause 2.0
    show cg minerva_owl with fade
    m "Wow, it's so cute!"
    a "She, not it."
    m "Sorry..."
    m "SHE."
    m "Is really cute!"
    a "Minerva is my owl."
    m "You named her after the Roman version of yourself?"
    a "Well, I thought it was a fitting name for her."
    a "She's my little Minerva, after all."
    m "I thought she would be white instead of brown."
    a "Why? She's a barn owl, Medusa."
    m "I don't know, humans always draw you with a white owl."
    m "But it makes sense that you'd have a brown one, since you've brown hair and all."
    pause 2.0
    a "I'm auburn, actually."
    m "What?"
    a "My hair isn't brown, it's auburn."
    m "Oh, right. Sorry about that."
    a "It's fine."
    m "I'm just sorta colourblind."
    a "...I see."
    pause 2.0
    m "...Can I hold her?"
    a "Sure, be careful though."
    scene black with fade
    a "Here you go."
    play sound "assets/sfx/ruffled_feathers.ogg"
    m "Oh boy, she's heavy!"
    a "Relax, she isn't going to bite."
    a "Yet."
    m "Yet?"
    a "She only tried to nip my eyes out the first time I held her."
    m "That's not helping, you know."
    show cg medusa_holding_owl with fade
    m "Once it became clear to me that Minerva wasn't going to devour me, I relaxed a little bit." # Internal monologue
    m "I even let myself stare dreamily into her own big, round eyes."
    m "They were a grey colour."
    m "The same as my..."
    pause 2.0
    m "Goddess."
    pause 2.0
    m "I wondered if the stories were true."
    m "That Athena used Minerva to spy on others."
    m "That she could see through Minerva's eyes and hear through her ears."
    m "If it were, it meant I was staring into my goddess's eyes right now."
    m "Something which, as my skin prickled with goosebumps, I didn't mind in the slightest."
    stop audio fadeout 0.5
    return

label demo_checkers:
    scene black
    play ambience "assets/sfx/checkers.ogg" loop
    m "So tell me, Athena."
    m "How does the round piece work again?"
    scene cg checkers_athena
    a "I was tired, but somehow I eked out a smile." ## Beginning of Athena's internal monologue
    a "Look, it's pretty simple."
    a "Every piece does the same thing."
    a "You take one step and try to jump over the others to capture them."
    a "That's the game in a nutshell."
    pause 2.0
    m "..."
    m "It does sound easy when you put it like that."
    m "OKAY, LET ME TRY!"
    a "I knew she was hopeless at games, but not this bad."
    a "I didn't even bother to look at the board, since I was already several steps ahead of her."
    scene cg_checkers_athena_look_up
    a "Instead, something else caught my eye."
    scene cg_checkers_medusa
    a "She was concentrating."
    a "Or rather, the snakes were concentrating."
    a "I wasn't sure which one of them was in control."
    scene cg_checkers_athena_look_up
    a "I didn't even understand how serpentine hair worked."
    a "Did each one have a strange, stifling mind of its own..."
    a "Pulling Medusa in so many different directions in life?"
    a "Maybe it was why she couldn't sit still in class."
    a "Or why, as my father had said, she'd started so many electives and never finished them."
    a "Perhaps."
    m "YOUR MOVE!"
    show cg_checkers_athena_look_down
    a "Huh?"
    a "Oh, right. The game."
    scene black with fade
    play sound "assets/sfx/checkers.ogg"
    m "What the..."
    play sound "assets/sfx/athena_giggle.ogg"
    scene cg checkers_athena_win
    a "I win!"
    play sound "assets/sfx/medusa_grunt.ogg"
    m "Not fair."
    a "Athena 1, Medusa 0."
    scene black with fade
    pause 1.0
    stop ambience fadeout 0.5
    play sound "assets/sfx/checkers_put_away.ogg"
    return

label demo_end:
    scene black
    a "If we'd tried playing chess, I think your head might've exploded."
    a "Mine nearly did."
    pause 1.0
    show bg hallway with dissolve
    show athena_neutral at Position(xalign=0.3) with dissolve
    show medusa_confused at Position(xalign=0.7) with dissolve
    m "I thought you were the campus champion in board games?"
    a "I am."
    show athena_tired at Position(xalign=0.3)
    a "...Just not in chess."
    a "That's Professor Poseidon's domain."
    show medusa_nervous at Position(xalign=0.7)
    pause 1.0
    m "Oh."
    show athena_concerned at Position(xalign=0.3)
    a "What?"
    show medusa_surprised at Position(xalign=0.7)
    m "Nothing."
    m "It's just..."
    a "Just what?"
    m "...I think it would be hard to play chess underwater, wouldn't you?"
    pause 1.0
    a "Poseidon does come up to campus to lecture in Marine studies, remember?"
    m "Yeah, I know but..."
    pause 2.0
    a "Is there something wrong?"
    show medusa_dismissive at Position(xalign=0.7)
    m "No! Nothing wrong."
    a "Are you sure?"
    a "Every time you hear Poseidon's name, you get very-"
    show medusa_eyebrow at Position(xalign=0.7)
    m "It's just bizarre to know!"
    m "That even the golden girl on campus has her off days."
    pause 0.5
    show athena_determined at Position(xalign=0.3)
    a "I don't have off days, Medusa."
    a "Poseidon just has a head start-"
    m "Your uncle."
    pause 0.5
    show medusa_grin at Position(xalign=0.7)
    show athena_annoyed at Position(xalign=0.3)
    play sound "assets/sfx/athena_sigh.ogg"
    pause 1.0
    a "My uncle, who has a head start-"
    m "I bet you're very happy I didn't call him your daddy."
    show athena_angry at Position(xalign=0.3)
    a "MY UNCLE!"
    a "..."
    pause 0.5
    show athena_neutral at Position(xalign=0.3)
    a "Just has a head start on me."
    a "from centuries of practice."
    pause 0.5
    show medusa_thoughtful at Position(xalign=0.7)
    m "I see."
    pause 1.0
    m "I wonder if he sleeps with them, like he does with his fish."
    show athena_annoyed at Position(xalign=0.3)
    play sound "assets/sfx/athena_ugh.ogg"
    a "Please don't say that again."
    a "That's Artemis' domain."
    a "The rumour mill."
    show medusa_happy at Position(xalign=0.7)
    m "Sorry, I just thought it was funny."
    a "What I'm trying to say..."
    a "Is that there's no substitute for persistence in life."
    show athena_determined at Position(xalign=0.3)
    a "I will defeat Poseidon in chess..."
    a "And so too will you graduate from Olympus University, Medusa."
    show medusa_neutral at Position(xalign=0.7)
    m "...I think what you're trying to say there, Athena..."
    m "Is that practice makes perfect, right?"
    pause 0.5
    show athena_deflated at Position(xalign=0.3)
    a "Yes, that's right."
    a "Too obvious?"
    m "Zeus gave me the same pep talk a billion times before."
    play sound "assets/sfx/athena_sigh.ogg"
    a "Well, I thought it was worth a try."
    pause 1.0
    show athena_neutral at Position(xalign=0.3)
    a "Same time tomorrow, then?"
    a "You still have whole catalogues of board games to get through, after all."
    a "Scrabble. Snakes and Ladders. Dungeons and Dragons. Monopoly. Dominoes."
    m "The pizza place?"
    show athena_deflated at Position(xalign=0.3)
    play sound "assets/sfx/athena_sigh.ogg"
    a "I'll pretend not to hear that."
    show medusa_sad at Position(xalign=0.7)
    m "...Hmm, alright."
    show athena_happy at Position(xalign=0.3)
    a "Great! I'll see you tomorrow, Medusa!"
    show medusa_happy at Position(xalign=0.7)
    m "See you tomorrow, Athena!"
    scene black with fade
    pause 1.0
    a "It was a start."
    a "Medusa might never be a board game genius like me, but at least she was trying."
    a "She wanted to keep going on."
    a "She wanted to get better."
    a "And I was happy for that - at least for the time being."
    return

label demo_poseidon:
    scene black
    m "Athena had offered to walk me back to my dorm after our board game session."
    m "But I'd said no."
    m "We'd been paired up enough for the day, and I wanted to be alone."
    m "Besides..."
    m "I didn't want her to wear out her welcome just yet."
    m "..."
    play sound "assets/sfx/medusa_footsteps.ogg"
    show bg cold_hallway with dissolve
    show medusa_sad at Position(xalign=0.3) with dissolve
    m "Just yet."
    m "Athena had smiled at me when I said that."
    m "I thought it was harsh to say that now..."
    m "But she didn't mind."
    pause 1.0
    m "She was persistent with me."
    m "I had to give her credit there."
    m "Besides her father, everyone else had given up on me."
    m "Nobody else seem to acknolwedge me on campus..."
    m "Well..."
    m "Except for the person I dreaded seeing most..."
    scene black with fade
    play sound "assets/sfx/footsteps.ogg"
    pause 2.0
    show poseidon_neutral at Position(xalign=0.7)
    pause 2.0
    m "Poseidon."
    m "Professor Poseidon."
    m "Campus legend. Sporting icon. Beloved by everyone."
    pause 2.0
    m "...And someone who I could never shake the feeling was an especially evil son of a bitch, underneath it all."
    m "What's worse, he had his eye on me."
    m "I knew that."
    scene black with Fade(3.0)
    pause 1.0
    scene bg cold_hallway with dissolve
    show medusa_angry_left at Position(xalign=0.7)
    show poseidon_neutral at Position(xalign=0.3)
    m "Even while my back was turned, I felt him watching me."
    m "Like a bloated shark might do when sizing up its prey..."
    m "Wondering if an extra morsel was worth the stomach-ache."
    pause 1.0
    scene black with fade
    m "I hated that."
    m "Hated feeling so weak."
    m "Hated that someone could have so much power over my mind."
    m "Hated."
    m "Hated."
    m "Hated it."
    show cg medusa_door with dissolve
    m "Even by the time I'd reached my room, I couldn't help but feel he was still watching me."
    m "Still waiting."
    m "Still pestering."
    m "Ready for any chance to claw his dirty fingertips deep into my harsh, green skin."
    scene black with fade
    pause 2.0
    return
