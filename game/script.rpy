# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# region Characters

define a = Character("Athena", color="#05a1da")
define m = Character("Medusa", color="#187d02")
define p = Character("Poseidon",)
define z = Character("Zeus", color="#cfc20d")
define art = Character("Artemis", color="#009525")
define n = Character("Nike",)
define d = Character("Dionysus",)
define anon = Character("???", color="#ff0000")
define spx = Character("Sphinx", color="#c7a912")
define na = Character("Narrator", color="#ffffff")


# endregion

# label splashscreen:
#     scene black
#     with fade
#     show text "{i}“She was once most beautiful, the jealous aspiration of many suitors. Neptune violated her in Minerva’s temple: the goddess turned away, and hid her chaste eyes behind her aegis.”{/i}\n-Ovid" at truecenter
#     pause 4
#     hide text
#     with dissolve 

default route = ""

# ---START---
label start:
    call choose_route
    return

# ---ROUTE SELECTION---
label choose_route:
    menu:
        "Choose a route":
            "Medusa's Route":
                $ route = "medusa"
                jump medusa_prologue
            "Athena's Route":
                $ route = "athena"
                jump athena_prologue

# ---medusa_prologue---
label medusa_prologue:
    call m_pro_exam
    call m_pro_pond
    call m_pro_office
    call m_pro_forest
    return

label m_pro_exam:
    scene black
    anon "Ahem!"
    anon "Now class, is everyone ready for the exam?"
    anon "raise your hand if you are!"
    play sound "assets/sfx/raise_hand.wav"
    anon "It seems like everyone is ready, except for..."
    anon "Medusa, what are you doing?"
    anon "Why do you have a book in your-"
    play sound "assets/sfx/book_throw.wav"
    pause 0.5
    m "FASCIST BASTARD!"
    pause 0.5
    scene cg classroom_sphinx
    with fade(1.0)
    sph "MEDUSA!"
    sph "GET OUT OF MY CLASSROOM!"
    pause 1.0
    scene black
    play sound "assets/sfx/door_close.wav"
    pause 1.0
    play sound "assets/sfx/footsteps.wav"
    pause 1.0
    play sound "assets/sfx/medusa_cry.wav"
    pause 1.0
    return

label m_pro_pond:
    scene black
    play sound "assets/sfx/pond_cry.wav"
    scene bg pond_medusa_cry
    with fade(1.0)
    m "Why can't I do anything right?"
    m "Why can't I be normal?"
    m "I just want to be normal..."
    play sound "assets/sfx/medusa_cry.wav"
    pause 1.0
    return

label m_pro_office:
    scene black
    play sound "assets/sfx/tapping_desk.wav"
    pause 1.0
    play sound "assets/sfx/zeus_ugh.wav"
    z "Eight years."
    z "Eight years of this."
    z "The most troublesome and mischievous student I've ever had."
    z "In all my years acting as the Rector of Olympus University."
    play sound "assets/sfx/office_door_open.wav"
    pause 0.5
    play sound "assets/sfx/footsteps.wav"
    pause 0.5
    m "You called for me, sir?"
    z "Yes, I did. Please, have a seat."
    play sound "assets/sfx/footsteps.wav"
    z "You forgot to close the door again."
    m "Oh, sorry about that."
    play sound "assets/sfx/footsteps.wav"
    pause 0.5
    play sound "assets/sfx/door_close.wav"
    pause 0.5
    play sound "assets/sfx/footsteps.wav"
    pause 0.5
    scene cg office_medusa_chair ## Medusa sitting in a chair, looking nervous, while Zeus is standing in front of her, looking stern.
    with fade(1.0)
    pause 1.0
    scene bg zeus_office
    with fade
    show zeus stern at Position(xalign=0.3)
    show medusa neutral at Position(xalign=0.7)
    with fade    
    z "Do you know why I called you here today, Medusa?"
    m "Throwing a book at an exchange professor?"
    play sound "assets/sfx/zeus_sigh.wav"
    pause 1.0
    z "Well that, and the fact she's already left Olympus University entirely."
    z "Which no doubt has sullied our reputation in the eyes of the academic community."
    z "All because of you and your reckless behavior, Medusa."
    show medusa sad at Position(xalign=0.7)
    pause 1.0
    show zeus tired at Position(xalign=0.3)
    play sound "assets/sfx/zeus_sigh.wav"
    z "I'm not giving up on you, Medusa."
    m "I wish you would, in a way."
    m "We've been at this for eight years now."
    m "And I still feel like the same dolt I was when I first came here."
    pause 1.0
    m "It's hopeless. I'll never graduate from Olympus University."
    play sound "assets/sfx/medusa_sigh.wav"
    pause 1.0
    show zeus determined at Position(xalign=0.3)
    z "That's why me and the faculty have decided to take a different approach with you."
    z "In order to help finish your studies."
    show medusa surprised at Position(xalign=0.7)
    m "Huh, what's that?"
    z "Do you know who Athena is?"
    pause 1.0
    m "Athena?"
    z "Yes, Athena."
    m "You mean Pallas Athena?"
    m "Your daughter?"
    play sound "assets/sfx/flask_open.wav"
    play sound "assets/sfx/flask_pour.wav"
    show zeus flask at Position(xalign=0.3)
    z "Yes, is there anything wrong with that?"
    show zeus drink at Position(xalign=0.3)
    play sound "assets/sfx/zeus_drink.wav"
    pause 1.0
    show zeus flask at Position(xalign=0.3)
    m "No, no, it's just..."
    z "You do know who Athena is, don't you?"
    pause 1.0
    scene black
    with fade(1.0)
    m "Of course I knew who Athena was."
    m "Who didn't?"
    m "She was the academic rock star of Olympus University."
    m "And one without an equal."
    scene cg athena_office
    with fade(1.0)
    m "She was the best student in the history of the university."
    m "Fluent in several different languages."
    m "Doctorates in several different subjects." 
    m "University champion in many strategic games."
    m "Expert orator, fencer and archer."
    m "And she even doubled as a skillful counselor and lecturer in her spare time."
    scene black
    with fade(1.0)
    m "She was the perfect student."
    m "Brilliant, clever selfless and not going to be spending the rest of her life on campus like me."
    m "She was everything that I wasn't."
    play sound "assets/sfx/medusa_sigh.wav"
    pause 1.0
    scene bg zeus_office
    with fade(1.0)
    show zeus determined at Position(xalign=0.3)
    show medusa surprised at Position(xalign=0.7)
    z "Athena is nearing the end of her Goddess degree here at Olympus University."
    z "But before she can graduate, she has to complete a final project."
    pause 1.0
    m "Which is...?"
    z "She has to take on a student as a follower and guide them..."
    m "So I am to be her test monkey then?"
    play sound "assets/sfx/zeus_grunt.wav"
    pause 1.0
    z "Not a test monkey, Medusa. A follower."
    z "A priestess, if you will."
    m "So I have to be her priestess?"
    m "And she will be my...?"
    z "Goddess, of course."
    pause 2.0
    m "I see."
    m "I started to mull the idea in my mind."
    m "This was the Rector's incredibly bizarre way of saying..."
    m "Yes Medusa, you're quite the troublemaker..."
    m "And we need someone to chaperone and keep an eye on you..."
    m "So here's my daughter, only a few credits shy of graduating...."
    m "And you can be her final project."
    m "..."
    pause 1.0
    z "This will kill two griffons with one stone."
    z "Are you up for it, Medusa?"
    pause 1.0
    menu m_choice:
        "What do you choose?"
        "Umm...":
            m "I don't have much of a choice, do I?"
            z "No, you don't. But I know you can do it, Medusa."
    pause 1.0
    m "..."
    m "It could be a change."
    m "A fresh start."
    m "But I wasn't sure if me and Athena would click."
    m "At all."
    pause 1.0
    z "...I can't force it upon you, of course."
    z "But Athena's well versed in all the subjects you struggle with."
    z "And I'm sure she can help you out with your studies."
    pause 1.0
    m "It could be even a chance to make a new friend."
    pause 2.0
    show medusa happy at Position(xalign=0.7)
    m "Alright, I'll give it a shot."
    show zeus happy at Position(xalign=0.3)
    z "Wonderful news, Medusa!"
    z "I'll send Hermes a missive to fetch her later on." 
    z "Once she's finished teaching another fencing class."
    m "...Okay."
    m "I'll take my leave then."
    hide medusa with dissolve 1.0
    play sound "assets/sfx/footsteps.wav"
    play sound "assets/sfx/door_close.wav"
    pause 1.0
    show zeus excited at Position(xalign=0.3)
    z "YES! YES! YES! YES! YES! YES! YES!"
    play sound "assets/sfx/zeus_excited.wav"
    pause 1.0
    m "I can still hear you from outside here, you know."
    show zeus embarrassed at Position(xalign=0.3) 
    z "Oh, sorry about that. I just got a little excited."
    pause 1.0
    scene black
    with fade(2.0)
    return

label m_pro_forest:
    scene black
    play sound "assets/sfx/forest_ambience.wav"
    pause 1.0
    m "This is my forest."
    m "Well, technically Groundskeeper Pan's forest, but I like to think of it as mine."
    scene bg forest
    with fade(1.0)    
    m "The place I hung out when I wanted to be alone."
    m "This place when everything in life was too much for me to handle."
    m "Where I could just be myself and not have to worry about anything."
    show medusa pond at Position(xalign=0.7) with dissolve
    m "When I was really down in the dumps, I'd come here and sit inside this pond for hours."
    m "I couldn't get an entry into Pan's forest pool, so I made my own."
    play audio "assets/sfx/pond_ambience.wav" loop
    pause 1.0
    show medusa pond_sigh at Position(xalign=0.7)
    play audio "assets/sfx/medusa_sigh.wav"
    pause 1.0
    m "Things could be worse."
    m "I at least have this place to myself."
    m "For now."
    pause 1.0
    play sound "assets/sfx/footsteps.wav"
    pause 1.0
    show medusa pond_look at Position(xalign=0.7)
    m "Huh, who's that?"
    play sound "assets/sfx/footsteps.wav"
    pause 1.0
    a "Σκατά, I have stepped on centaur dung."
    m "Hmph. Pan is such an uncivilized brute."
    a "And those were my best sandals too!"
    a "μαλάκα!"
    play sound "assets/sfx/footstepsforest.wav"
    play sound "assets/sfx/athena_footsteps.wav"
    pause 1.0
    show athena neutral at Position(xalign=0.3)
    with dissolve
    a "Medusa Margoyles?"
    show athena mouth_covered at Position(xalign=0.3)
    play sound "assets/sfx/athena_gasp.wav"
    play sound "assets/sfx/medusa_ugh.wav" 
    pause 1.0
    m "...That's my nickname on campus, dear player."
    pause 1.0
    show medusa arm_raised at Position(xalign=0.7)
    m "HERE!"
    m "You called?"
    show athena eye_closed at Position(xalign=0.3)
    a "I have."
    a "I am Athena, daughter of Zeus and goddess of wis-"
    show medusa dismissive at Position(xalign=0.7)
    m "Blah, blah, blah. I know who you are."
    show athena eye_open at Position(xalign=0.3)
    m "You're Athena. The golden girl on campus."
    m "I know all that stuff already."
    show athena annoyed at Position(xalign=0.3)
    pause 1.0
    a "...Well, I'm sure you know this already then, but I'm going to be your mentor for the next few months."
    m "Goddess, you mean."
    m "Let's not downplay it."
    m "At all."
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
            m "and leave me and Olympus University in the dust?"
            m "Right?"
            show athena angry at Position(xalign=0.3)
            play sound "assets/sfx/athena_angry.wav"
            show medusa scared at Position(xalign=0.7)
            a "Yes, you caught me!"
            a "I'm doing this all for the love of credits!" 
            a "And not because I want to learn to look after someone who chooses to follow me!"
            a "Which is what a goddess would do!"
            show medusa slump at Position(xalign=0.7)
            pause 2.0
            play sound "assets/sfx/athena_sigh.wav"
            show athena tired at Position(xalign=0.3)
            a "I didn't mean to snap like that."
            a "That was....terribly out of character for me."
            pause 2.0
            show medusa smile at Position(xalign=0.7)
            m "It's okay, I get it."
            m "That usually happens when someone is forced to spend a lot of time with me."
            m "It just happens when you're around poor old Medusa."
            m "The perennial senior who can't get her act together."
            m "Who can't even graduate from university."
    pause 1.0
    a "You just need to study more, Medusa."
    a "I didn't get everything right on my first go, either."
    m "But these tests haven't been my first go in years now!"
    a "I know. That's why I'm here."
    a "To make sure they're your last."
    pause 2.0
    m "I thought I should snap back."
    m "We'd a bit of a rough start, but I felt at least we'd come to an understanding."
    m "She wanted to help me, and I wanted to be helped."
    m "She wanted to cross the finish line, and get her degree."
    m "....And so did I, deep down."
    pause 3.0
    m "...Does this mean I'm going to have go through my Greek conjugations right now?"
    m "Anything but that, I thought."
    show athena eye_closed_smile at Position(xalign=0.3)
    a "No, not yet."
    show athena eye_open_smile at Position(xalign=0.3)
    a "Instead, we'll do something you'd like to do."
    m "Something I like to do?"
    m "It was the first time anyone had asked me what I'd actually wanted to do."
    a "Yes. Think of something and we'll do it together."
    pause 1.0
    m "Well...."
    m "How about..."
    menu m_athena_activity:
        "What do you choose?"

        "The Owl House":
            m "How about The Owl House?"
            show athena squint at Position(xalign=0.3)
            a "The Owl House?"
            m "Yeah, the Owl House."
            pause 1.0
            show athena lightbulb at Position(xalign=0.3)
            a "Oh. You mean the mews!"
            m "Everyone just calls it the Owl House, Athena."
            m "But I've never been."
            a "Why not?"
            pause 1.0
            m "...Snakes and birds of prey don't usually mix."
            m "But if you're there, I might feel safe."
            a "I am the head of it, I suppose."
            a "Alongside a billion other clubs on campus."
            show athena determined at Position(xalign=0.3)
            a "Very well. I'll show you the Mews."
            m "...The Owl House."
            a "Yes, Owl House!"
            a "....Just get dressed, would you?"
            m "Alright."
            scene black with dissolve
            pause 1.0

        "Get into the pond with me":
            m "Why don't you come in here with me?"
            a "What?"
            m "I'm serious. Get in."
            a "...But I don't have my swimming gear with me."
            m "So? I'm not wearing mine either."
            show athena red at Position(xalign=0.3)
            m "For a moment, I felt her cheeks flush."
            m "She was embarrassed about stripping down in front of me."
            m "I didn't think she was used to it, even in front of other women."
            m "C'mon, for the day that's in it."
            show athena neutral at Position(xalign=0.3)
            a "Hmph, alright."
            a "I did say something that you'd like to do."
            m "Yup."
            m "Now get in."
                    show athena bra at Position(xalign=0.3)
            with dissolve
            show medusa blush at Position(xalign=0.7)
            m "Oh my."
            a "What?"
            m "Nothing."
            show medusa determined at Position(xalign=0.7)
            m "Just get your butt in here, golden girl!"
            pause 1.0
            scene black with fade
            show cg athena_medusa_pond
            m "See?" 
            m "Not so bad now, is it?"
            m "I guess not."
            scene black with dissolve
            pause 1.0    
    m "So tell me."
    m "How does this Goddess and Priestess thing work?"
    return

label m_pro_TOH:
    scene black
    a "So you've never been inside this place?"
    m "Never. Rector Zeu-"
    pause 2.0
    m "Your father. Forbid me from coming in."
    a "Because snakes and birds don't mix?"
    m "Exactly."
    a "It wasn't out of pettiness then."
    a "But I'm now sure how you think snakes and birds will get along now."
    show bg stairs with fade
    show medusa neutral at Position(xalign=0.5) with dissolve
    show athena neutral at Position(xalign=0.3) with dissolve
    m "Well, I thought if you were at my side..."
    m "Maybe the owls wouldn't nitpick me to death."
    play sound "assets/sfx/athena_giggle.wav"
    a "Tht won't happen, Medusa."
    a "Not under my watch."
    m "Promise?"
    a "Pinky promi-"
    art "Fetching new luncheon meat for the owls, I see."
    show athena surprised at Position(xalign=0.3)
    show medusa surprised at Position(xalign=0.5)
    pause 1.0
    show artemis neutral at Position(xalign=0.7) with dissolve
    art "Or not. Maybe a snake sandwich is on the menu today."
    play sound "assets/sfx/artemis_laugh.wav"
    show athena angry at Position(xalign=0.3)
    show athena angry_arms at Position(xalign=0.3)
    a "Ugh, Artemis. What do you want?"
    art "I just wanted to say hi to you, Athena."
    
        



    


        




# ---athena_prologue---
label athena_prologue:
    call a_pro_diss
    call a_pro_fencing
    call a_pro_office
    return
    
    scene black