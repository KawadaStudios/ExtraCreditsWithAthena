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
define ahu = Character("Ahura Mazda", color="#ff69b4") # Head Librarian and also the only one who can read the ancient cuneiform tablets in the library.
define ahr = Character("Ahriman", color="#ff69b4") # Assistant Librarian and Ahura Mazda's daughter.

# Athena and Medusa's Inner Circle
define art = Character("Artemis", color="#009525") # Goddess of the Hunt
define n = Character("Nike", color="#906d01") # Goddess of Victory, close friend of Athena and idolises Poseidon
define d = Character("Dionysus", color="#6259b4")
define he = Character("Hephaestus", color="#89571d")
define k = Character("Kanaloa", color="#269ca4") # Poseidon's accomplice and transfer student from Hawaii University.
define minv = Character("Minerva", color="#c8aa25") # Athena's Owl and only furbaby, who is a barn owl and not a white owl like most people think.

# Other important characters
define aph = Character("Aphrodite", color="#ffffff")
define are = Character("Ares", color="#ffffff")

# Miscellaneous characters
define anon = Character("???", color="#ffffff")
define na = Character("Narrator", color="#ffffff")

# Counters
default lovers = 0
default friends = 0
default rivals = 0
default enemies = 0

init python:
    renpy.music.register_channel("ambience", mixer="music", loop=True)

# Sound effects

# Athena
define audio.athena_angry = "assets/sfx/athena_angry.ogg"
define audio.athena_fencing_footsteps = "assets/sfx/athena_fencing_footsteps.ogg" # ?
define audio.athena_gasp = "assets/sfx/athena_gasp.ogg"
define audio.athena_giggle = "assets/sfx/athena_giggle.ogg"
define audio.athena_lightbulb = "assets/sfx/athena_lightbulb.ogg" # ?
define audio.athena_phone = "assets/sfx/athena_phone.ogg" # ?
define audio.athena_forest_footsteps_1 = "assets/sfx/athena_forest_footsteps_1.ogg" # ?
define audio.athena_forest_footsteps_2 = "assets/sfx/athena_forest_footsteps_2.ogg" # ?
define audio.athena_forest_footsteps_3 = "assets/sfx/athena_forest_footsteps_3.ogg" # ?
define audio.athena_pond_footsteps = "assets/sfx/athena_pond_footsteps.ogg" # ?
define audio.athena_sigh = "assets/sfx/athena_sigh.ogg"
define audio.athena_snort = "assets/sfx/athena_snort.ogg"
define audio.athena_ugh = "assets/sfx/athena_ugh.ogg"
define audio.athena_ugh_2 = "assets/sfx/athena_ugh_2.ogg"

# Medusa
define audio.medusa_alarm = "assets/sfx/medusa_alarm.ogg"
define audio.medusa_alarm_1 = "assets/sfx/medusa_alarm_1.ogg" # ?
define audio.medusa_alarm_2 = "assets/sfx/medusa_alarm_2.ogg" # ?
define audio.medusa_alarm_3 = "assets/sfx/medusa_alarm_3.ogg" # ?
define audio.medusa_bed = "assets/sfx/medusa_bed.ogg" # ?
define audio.medusa_door_explosion = "assets/sfx/medusa_door_explosion.ogg" # ?
define audio.medusa_dressed = "assets/sfx/medusa_dressed.ogg" # ?
define audio.medusa_hallway_footsteps = "assets/sfx/medusa_hallway_footsteps.ogg" # ?
define audio.medusa_grunt = "assets/sfx/medusa_grunt.ogg"
define audio.medusa_hum_skate = "assets/sfx/medusa_hum_skate.ogg"
define audio.medusa_sigh = "assets/sfx/medusa_sigh.ogg"
define audio.medusa_sigh_relief = "assets/sfx/medusa_sigh_relief.ogg"
define audio.medusa_sigh_relief_2 = "assets/sfx/medusa_sigh_relief_2.ogg"
define audio.medusa_teeth_brush = "assets/sfx/medusa_teeth_brush.ogg" # ?
define audio.medusa_ugh = "assets/sfx/medusa_ugh.ogg"

# Artemis
define audio.artemis_angry = "assets/sfx/artemis_angry.ogg"
define audio.artemis_cry = "assets/sfx/artemis_cry.ogg"
define audio.artemis_grunt = "assets/sfx/artemis_grunt.ogg"
define audio.artemis_laugh = "assets/sfx/artemis_laugh.ogg"
define audio.artemis_scream = "assets/sfx/artemis_scream.ogg"

# Zeus
define audio.zeus_cough = "assets/sfx/zeus_cough.ogg"
define audio.zeus_door_open = "assets/sfx/zeus_door_open.ogg" # ?
define audio.zeus_hum = "assets/sfx/zeus_hum.ogg"
define audio.zeus_laugh = "assets/sfx/zeus_laugh.ogg"
define audio.zeus_sigh = "assets/sfx/zeus_sigh.ogg"

# Other characters
define audio.dionysus_drunk = "assets/sfx/dionysus_drunk.ogg"
define audio.hephaestus_snort = "assets/sfx/hephaestus_snort.ogg"
define audio.nike_snort = "assets/sfx/nike_snort.ogg"

# Ambience and crowds
define audio.class_talking = "assets/sfx/class_talking.ogg"
define audio.crowd_boo = "assets/sfx/crowd_boo.ogg"
define audio.crowd_cheer = "assets/sfx/crowd_cheer.ogg"
define audio.crowd_laugh = "assets/sfx/crowd_laugh.ogg"
define audio.dissertation_question = "assets/sfx/dissertation_question.ogg"
define audio.disstalk = "assets/sfx/DissTalk.ogg" # ?
define audio.forest_ambience = "assets/sfx/forest_ambience.ogg" # ?
define audio.mews = "assets/sfx/Mews.ogg" # ?
define audio.pond = "assets/sfx/pond.ogg" # ?

# General sound effects
define audio.alarm_slam = "assets/sfx/alarm_slam.ogg" # ?
define audio.book_throw = "assets/sfx/book_throw.ogg" # ?
define audio.checkers = "assets/sfx/checkers.ogg" # ?
define audio.checkers_put_away = "assets/sfx/checkers_put_away.ogg" # ?
define audio.door_close = "assets/sfx/door_close.ogg" # ?
define audio.door_open = "assets/sfx/door_open.ogg" # ?
define audio.fencing = "assets/sfx/fencing.ogg" # ?
define audio.fencing2 = "assets/sfx/fencing2.ogg" # ?
define audio.fencing_door_open_close = "assets/sfx/fencing_door_open_close.ogg" # ?
define audio.footsteps = "assets/sfx/athena_medusa_hallway_footsteps.ogg" # ?
define audio.keys_jingle = "assets/sfx/keys_jingle.ogg" # ?
define audio.keys_jingle2 = "assets/sfx/keys_jingle2.ogg" # ?
define audio.owl_hoots = "assets/sfx/owl_hoots.ogg"
define audio.owl_squeaking = "assets/sfx/owl_squeaking.ogg"
define audio.phone_click = "assets/sfx/phone_click.ogg" # ?
define audio.phone_hangup = "assets/sfx/phone_hangup.ogg" # ?
define audio.ruffled_feathers = "assets/sfx/ruffled_feathers.ogg" # ?
define audio.stairs_crash = "assets/sfx/stairs_crash.ogg" # ?
define audio.tapping_desk = "assets/sfx/tapping_desk.ogg" # ?
define audio.wine_tap = "assets/sfx/wine_tap.ogg" # ?

define flash = Fade(0.25, 0.0, 0.5, color="#fff")
image black = Solid("#000")

# Placeholder image definitions for testing without art
image bg fencing = "placeholder.png"
image bg zeus_office = "placeholder.png" # A large desk in the centre, with Zeus chair in the back and one visiter chair in the fron
image bg forest = "placeholder.png" # The forest should be a darker shade of green, much like a darker shade of Medusa' skin colour herself. In the centre, a pond that two people could fit into. It's still, as though no one has ever sat inside it. The water should be a turqoise colour.
image bg stairs = "placeholder.png" # Centre staircase of Olympus University. I was thinking a great spiral in the middle, and long pathways on the side.
image bg owl_house_door = "placeholder.png" # A clean corridor, with a large door to the right side.
image bg owl_house_interior = "placeholder.png" # A large mews. Instead of the birds in cages, I'd like them to just be everywhere - perched on walls, perched on cages etc. The Owl house is in many ways just one large mews for the Owls to fly trhough.
image bg hallway = "placeholder.png" # A hallway Medusa and Athena are walking through. Maybe some flyers here and there on the walls for this or that club, or a framed photo of a star student
image bg cold_hallway = "placeholder.png" # Could be the same hallway again, just shaded in darker colours to reflect Poseidon's darker intentions around Medusa.

# Intro CGs
image cg INTRO_quote_1 = "placeholder.png"
image cg INTRO_quote_2 = "placeholder.png"
image cg INTRO_quote_3 = "placeholder.png"

# Title CGs
image cg TITLE_kawada_studios_presents = "placeholder.png"
image cg TITLE_collab_potatoes = "placeholder.png"
image cg TITLE_kimia_kore_novel = "placeholder.png"
image cg TITLE_Extra = "placeholder.png"

# Regular CGs
image cg athena_dissertation = "placeholder.png" # Athena in the midst of a celebration for her PhD. She is in the centre, in her usual robes, holding a wine glass wih white wine while her friends (Dionysus, Nike and Hephatutes) crowd around her. Zeus is off to the centre. The primary focus be Athena in this key shot.
image cg athena_dissertation2 = "placeholder.png" # Zeus raises his own wine glass in toast. It was thinking this could be a horizontal shot - Athena and the gang to the left, Zeus to the right. In the background, maybe a few more figures to give the gathering density? (You can draw them simply if that's easier for you, they don't need to be entirely new character designs)
image cg athena_dissertation3 = "placeholder.png" # Close up shot of Athena. Still holding her wine glass, and still smiling, albeit her smile seems faint and hollow
image cg medusa_slams_alarm = "placeholder.png" # Medusa crushing the alarm clock with her hand in annoyance. Being Medusa, the alarm should be snake themed. I'm open to any ideas you have.
image cg medusa_bed = "placeholder.png" # Bird's eye view of Medusa's bed. Medusa is wearing black satin and she is under the covers, though her hands are stretched out on top. Her snakes either sleeping, dazed and confused or wide awake. Some even have minature eye-masks on.
image cg medusa_teeth_brush = "placeholder.png" # Medusa brushing her teeth in the bathroom mirror. The snakes are getting ready for their day too. Some have minature toothbrushes stuck in their mouths, others have shower caps
image cg medusa_dressed = "placeholder.png" # Medusa getting dressed behind her bedroom mirror. Once we decide on the final outfit, we'll iron out the details then. The snakes are trying out minautre outfits too. One of them is wearing black shades - important.
image cg medusa_mirror_neutral = "placeholder.png" # Medusa in front of her living room mirror. Neutral expression.
image cg medusa_mirror_happy = "placeholder.png" # Medusa in front of her living room mirror. The same CG, this time with a happy expression.
image cg medusa_door_day = "placeholder.png" # Medusa's dorm room door. A large snake as a door knocker. Very Medusa.
image cg medusa_door_explosion = "placeholder.png" # Door explosion to the side. Medusa appears in the air above it, riding a skateboard.
image cg hallway_medusa_skate = "placeholder.png" # Medusa skating through the hallways. The students around her hardly take notice and ignore her. This is just a normal thing on Olympus University.
image cg hallway_medusa_shade = "placeholder.png" # Frontal shot of Medusa wearing shades, drinking some soda from a straw, trying desperately to look cool.
image cg sphinx_door = "placeholder.png" # Door to the Sphinx classroom. I like the idea Potato of their being some kind of notice board on the wall next to it. Filled with pamphlets about clubs or events that are coming up. It would make the game feel more like it's a universe that acutal people live in.
image cg classroom_sphinx = "placeholder.png" # Sphnix hiding behind their desk, using it as some kind of cover as their head pokes over it.
image cg zeus_door_neutral = "placeholder.png" # Zeus opening the door to his office, slightly. Expression neutral.
image cg zeus_door_frown = "placeholder.png" # Zeus opening the door to his office, slightly. same CG. Expression with a deep frown.
image cg medusa_office = "placeholder.png" # Medusa on a seat in front of his desk. Hunched down. Her head staring down at the ground. Defeated.
image cg athena_dionysus_fencing = "placeholder.png" # Athena brings the tip of her sabre to Dioynus chest. Background is the fencing_room BG.
image cg athena_changing_room = "placeholder.png" # Athena staring into the changing room mirror.
image cg athena_medusa_pond = "placeholder.png" # The two girls in the pond. Maybe some slight splashing of water on Medusa's part to a slightly ticked off Athena? 
image cg athena_artemis_fight = "placeholder.png" # From the ground view of the bottom of the stairs. Artemis lies in a heap, while Athena and Medusa remained unblemished at the top. Medusa looks wowed, Athena is dusting her hands after a job well done.
image cg owl_house_door_medusa = "placeholder.png" # Medusa locked behind the owl house door, banging on it, her face a nervous wreck. I was thinking their should be a circular winodw where we can see Medusa through.
image cg owl_house_door_artemis = "placeholder.png" # Athena and Artemis, smiling and giggling like a pair of cruel mean girls. Thankfully, it's just Medusa's nightmare.
image cg medusa_helping_athena = "placeholder.png" # The two women pressing themselves against the Owl House door, readying for a push. 
image cg medusa_refusing_athena = "placeholder.png" # Medusa waving a distraught Athena away, who is a bit ticked off at having to push the door by herself. 
image cg minerva_owl = "placeholder.png" # Athena holding Minerva on her arm with a falconry gloves. Medusa looks on, eyes wide in wonder.
image cg medusa_holding_owl = "placeholder.png" # Medusa holding the owl in her arms. She looks over in to it's eyes, while Athena looks on at the pair of them. 
image cg checkers_athena = "placeholder.png" # Athena and Medusa at a table, playing checkers. Athena motions to a piece on the board, explaining how this dastardly game works. It's improtant that has Athena has a faint smile here. She's exhausted from babysitting Medusa all day.
image cg_checkers_athena_look_up = "placeholder.png" # Athena's eyes looking up at Medusa. Her chin is resting under her left knuckles, deep in thought.
image cg_checkers_medusa = "placeholder.png" #Medusa peering down at the board, the snake strands all lost in their own conflicting thoughts on what move to play next.
image cg_checkers_athena_look_down = "placeholder.png" # This could just be the look up checkers one again, slightly edited.
image cg checkers_athena_win = "placeholder.png" # Athena celebrates, with a lot more joy than expected of the Goddess of Wisdom. Medusa
image cg medusa_door = "placeholder.png" # Medusa's door closed shut, albeit with some wear and tear after her initial explosion through it in the beginning of the story.

# Athena's default sprites
image athena_robes_neutral = "placeholder.png" # All of Athena's sprites are on the left of the screen (Meaning, she faces right.)
image athena_robes_mouth_covered = "placeholder.png" # Athena covering her mouth in shock. It does not bode well to call Medusa by her nickname Medusa Margoyles. 
image athena_robes_annoyed = "placeholder.png"
image athena_robes_angry = "placeholder.png"
image athena_robes_tired = "placeholder.png"
image athena_robes_happy = "placeholder.png" # Athena, smiling. I think this could be the Neutral one again, just slightly edited.
image athena_robes_thinking = "placeholder.png" # Athena placing a hand to her chin, lost in deep thought.
image athena_robes_lightbulb = "placeholder.png" # A lightbulb appears over Athena's head. I think this could be the surprised sprite again, with a lightbulb over it and maybe some bright emphasis on her head.
image athena_robes_determined = "placeholder.png" # Determined look, with her left hand raised a bit? I'm not sure, open to ideas.
image athena_robes_red = "placeholder.png" # A red blush creeping over Athena's face. Maybe this is the surpised again, just with the red blush on top?
image athena_robes_surprised = "placeholder.png" # A surprised look.
image athena_robes_cringe = "placeholder.png" # Athena's eyes closed, her body cringing.
image athena_robes_proud = "placeholder.png" # Athena in a wide stance - her eyes closed, smiling, her arms crossed.
image athena_robes_concerned = "placeholder.png" # Maybe this could be the thinking one again, slightly edited to make her face look more worried/concerned?
image athena_robes_sigh = "placeholder.png" # A deflated look - almost like she's been caught sighing mid breath.
image athena_robes_blue_call_minerva = "placeholder.png" # A slight shimmer of lightning blue appears in Athena's eyes. Her right hand reaches to the sky as she calls Minerva

# Athena's Swimsuit sprites
image athena_bra_neutral = "placeholder.png" # Athena's default swimsuit sprite.
image athena_bra_happy = "placeholder.png" # Athena, smiling.
image athena_bra_annoyed = "placeholder.png" # Athena, annoyed. How about her arms crossed around her chest? 

# Athena's Fencing sprites
image athena_fencing_neutral = "placeholder.png" # Athena's default fencing sprite. All of Athena's fencing sprites are on the left side of the screen (meaning she faces right, like Nike.)
image athena_fencing_happy = "placeholder.png" # Athena, smiling.
image athena_fencing_annoyed = "placeholder.png" # Athena, annoyed. How about her arms crossed around her chest?
image athena_fencing_phone = "placeholder.png"# Athena holding a sort of brick-esque dumphone. She doesn't like using modern tech if she can help it.
image athena_fencing_call_eyes_open = "placeholder.png" # Athena bringing the phone to her right ear. Eyes open.
image athena_fencing_call_eyes_closed = "placeholder.png" # Athena bringing the phone to her right ear. Eyes closed.
image athena_fencing_sad = "placeholder.png" # Athena, with a sad expression in her fencing outfit.

image dionysus_fencing_neutral = "placeholder.png" # Dionysus default sprite. All of Dionysus sprites are on the right side of the screen (Meaning he faces left, like Medusa.)
image dionysus_fencing_tired = "placeholder.png"
image dionysus_fencing_happy = "placeholder.png"
image dionysus_fencing_surprised = "placeholder.png"
image dionysus_fencing_angry = "placeholder.png"

image nike_neutral = "placeholder.png" # Nike's default sprite. All of Nike's sprites are on the left side of the screen (meaning she faces right, like Athena.)
image nike_excited = "placeholder.png" # Nike's excited sprite. Her eyes are wide, her mouth open in a smile, and her arms raised in excitement.
image nike_annoyed = "placeholder.png" # Nike annoyed, arms crossed, eyes to the side, mouth in a frown.
image nike_sick = "placeholder.png" # Nike sick, eyes closed, mouth in a frown. Maybe a slight green tinge to her face?
image nike_angry = "placeholder.png" # Nike angry, eyes and brow narrowed down, mouth in a frown. Maybe a slight red tinge to her face?
image nike_embarrassed = "placeholder.png" # Embarassed look. 
image nike_red = "placeholder.png" # Maybe the embarassed sprite again, but with a pink glow to her cheeks? Perhaps an exclamatioin point above her head too? Her eyes facing at the player (audience)
image nike_tired = "placeholder.png" # Nike tired. Her eyes closed, her stance bowed down slight, hands on her forehead and one against her hips. A slight frown as well. 
image nike_worried = "placeholder.png" # Nike with a worried expression on her face. 
image nike_smug = "placeholder.png" # Nike with a smug expression on her face. Her mouth is a slight smirk. 

image hephaestus_neutral = "placeholder.png" # Hephaestus default sprite. All of Hephaestus sprites are on the right side of the screen (Meaning he faces left, like Medusa.)
image hephaestus_curious = "placeholder.png" # Curious look.  Raised eyebrow, maybe a slight tilt of the head, neutral expression.
image hephaestus_happy = "placeholder.png" # Happy look. A smile, maybe a slight tilt of the head, eyes wide and bright.
image hephaestus_angry = "placeholder.png" # Angry look. Furrowed brow, narrowed eyes, mouth in a frown. Maybe a slight tilt of the head downwards.

image zeus_stern = "placeholder.png" # Stern look. One can feel the fury brimming underneath that the eccentric Rector often tries to surpress.
image zeus_tired = "placeholder.png" # Tired look. The Rector has been working tirelessly to keep Olympus University running smoothly, and it shows in his weary expression. Maybe a hand to the forehead, or a slight slump of the shoulders.
image zeus_determined = "placeholder.png" # Determined look. Slight smile. Zeus clenches a hand like an anime protagonist, ready to take on the world.
image zeus_neutral = "placeholder.png" # Zeus default sprite. All of Zeus' sprites are on the left side of the screen (Meaning he faces right, like Athena.)
image zeus_happy = "placeholder.png" # Happy look. A smile, maybe a slight tilt of the head, eyes wide and bright.
image zeus_excited = "placeholder.png" # Excited look. A wide, happy go lucky smile. This is Zeus true nature - a big dog trapped in the body of a God. 
image zeus_embarrassed = "placeholder.png" # Embarrassed look. A slight blush on his cheeks, eyes looking away, maybe a hand to the back of his head.

# Medusa's standard sprites
image medusa_neutral = "placeholder.png" # Medusa's default sprite. All of Medusa's sprites are on the right side of the screen (Meaning she faces left.)
image medusa_sad = "placeholder.png" # Downtrodden look, eyes down to the ground. 
image medusa_nervous = "placeholder.png" # Nervous look, eyes darting around, maybe a slight sweat drop on her forehead?
image medusa_confused = "placeholder.png" # Confused look, Maybe a ? above her head too? 
image medusa_surprised = "placeholder.png" # Surprised look - perhaps her jaw slightly open? 
image medusa_eyebrow = "placeholder.png" # A raised eyebrow - thoughtful, contemplative look. 
image medusa_annoyed = "placeholder.png" # Annoyed look, eyes narrowed, mouth in a frown. Perhaps both her arms on her hips too? 
image medusa_dismissive = "placeholder.png" # This could be the annoyed sprite again, but her waving bother her arms in a dismissive way. 
image medusa_angry = "placeholder.png" # Angry look, hands curled in fists, snakes ready to bite. 
image medusa_happy = "placeholder.png" # Happy look, eyes wide and bright. An unusual expression for Medusa, but one that is genuine and heartfelt.
image medusa_smirk = "placeholder.png" # Smirk look. A mischievous expression. More like the Medusa we know. 
image medusa_excited = "placeholder.png"

# Medusa's pond variants
image medusa_pond_neutral = "placeholder.png" # I picture Medusa's pond variants to be half of her. She's submerged in pond water, so we only see her head and neck emerge. I'll draw an example of what I mean, Potatoes. 
image medusa_pond_sad = "placeholder.png"
image medusa_pond_sigh = "placeholder.png"
image medusa_pond_scared = "placeholder.png"
image medusa_pond_surprised = "placeholder.png"
image medusa_pond_eyebrow = "placeholder.png" 
image medusa_pond_annoyed = "placeholder.png"
image medusa_pond_dismissive = "placeholder.png" # This could be the annoyed pond sprite again, but her waving both her arms in a dismissive way. 
image medusa_pond_arm_raised = "placeholder.png"
image medusa_pond_blush = "placeholder.png"
image medusa_pond_happy = "placeholder.png"

# Medusa's left variants (facing right, like Athena)
image medusa_neutral_left = "placeholder.png" # Medusa's neutral, angled to the left (meaning, she faces right like Athena. Sometimes Potato when people flip a sprite it looks awkward, so perhaps we might have to redo this one again)
image medusa_surprised_left = "placeholder.png" # Medusa's surprised sprite, angled to the left (meaning, she faces right like Athena.)
image medusa_eyebrow_left = "placeholder.png"
image medusa_angry_left = "placeholder.png"
image medusa_happy_left = "placeholder.png"
image medusa_proud_left = "placeholder.png"

# Artemis' sprites
image artemis_neutral = "placeholder.png"
image artemis_laugh = "placeholder.png"
image artemis_angry = "placeholder.png"
image artemis_furious = "placeholder.png"

# Poseidon's sprites
image poseidon_neutral = "placeholder.png"

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
    play ambience audio.disstalk fadein 2.0 # ?
    show cg INTRO_quote_1
    pause 2.0
    show cg INTRO_quote_2
    pause 2.0
    show cg INTRO_quote_3
    pause 2.0
    play sound audio.wine_tap
    stop ambience fadeout 0.5
    z "So, my wonderful daughter, how many PhDs do you have now?" # VA: Proud, playful.
    a "Ninety-nine, Father." # VA: Slightly embarrassed, but proud.
    z "Ninety-nine PhDs?" # VA: Genuine disbelief.
    play sound "assets/sfx/zeus_laugh.ogg"
    z "So that headache you gave me when you were born, it was worth it after all!" # VA: Booming dad-joke, but Zeus knows THAT Athena knows how important to him she really is.
    a "...I'd think so, yes." # VA: Slightly embrassed. She still isn't used to such high praises. 
    voice "assets/voice/Dionysus/dionysus_demo_dissertation/demo_dissertation_dionysus_01.ogg"
    d "So what was the subject of your dissertation this time, Athena?"
    show cg athena_dissertation with fade
    a "Etruscan influences on the development of Greek pottery." # VA: Proud, matter-of-fact. Athena is proud of her work, even if the subject matter is a bit on the dry side. 
    play sound "assets/sfx/dionysus_drunk.ogg"
    voice "assets/voice/Dionysus/dionysus_demo_dissertation/demo_dissertation_dionysus_02_drunk.ogg"
    d "And I thought it was the other way around!" # Amazed. 
    n "Me too!" # VA: Bright, eager to agree.
    he "Shows us how much we know about ancient history, huh?" # VA: Smiling, self-deprecating.
    play sound "assets/sfx/athena_snort.ogg"
    show cg athena_dissertation2 with fade
    z "A toast then." # VA: Loud, formal tone. He wants everyone to know how proud he is of his daughter.
    z "To Athena." # VA: Emphasis on her name.
    z "My daughter, in case anyone here on Olympus University has lived underneath, well, how shall we say..." # VA: Long winded set-up for the punchline. 
    play sound "assets/sfx/zeus_cough.ogg"
    z "A Persian boulder for the last few years." # VA: Punchline delivery.
    play sound "assets/sfx/crowd_boo.ogg"
    ahu "I heard that." # Annoyed clip. 
    z "Yes, boo all you want. But keep in mind we DO have a few Persian boulders here on campus, so they might take offence to it." # VA: Playful control of the crowd. He can't help but get a dig into Ahura.
    play sound "assets/sfx/crowd_laugh.ogg"
    ahu "Hmph." # Defiant grunt. 
    z "Anyway, to Athena." # VA: Warm, proud reset. 
    z "To the most brilliant student in the history of Olympus University." # VA: Proud over the top praise.
    z "And the best daughter a father could ever ask for." # VA: Sickly sweet pride, the sort of guff found on a late 90's family sitcom.
    play sound "assets/sfx/crowd_cheer.ogg"
    pause 1.0
    show cg athena_dissertation3 with fade
    stop audio fadeout 0.5
    play audio "assets/sfx/dissertation_question.ogg" loop
    a "Between all the badgering of questions, I realised I should've been happy." # VA: Beginning of Athena's internal monologue. 
    a "I'd completed my 99th dissertation, and graduation from Olympus University was only weeks away." # VA: Reflective, matter-of-fact tone.
    a "I should be happy." # VA: Slightly sad emphasis on the word "should.""
    scene black with fade
    pause 1.5
    stop audio
    a "But I wasn't." # VA: Slight sadness. Disapointment even after all her achievements.
    a "Something was missing." # VA: Athena feels it in her bones, but she can't quite put her finger on it.
    a "Like there was some lost soul hiding underneath a Persian boulder." # VA: Reflective, searching tone. Athena is trying to name the feeling she's carrying.
    a "Like there was someone out there who needed my help." # VA: Quiet conviction. The thought lands with a sense of purpose.
    pause 0.5
    a "But where?" # VA: Slightly more urgent, reflective tone. End of internal monologue.
    pause 1.0
    return

label demo_medusa_introduction:
    scene black
    play ambience audio.medusa_alarm_1 loop # ?
    anon "Ugh..." # VA: Groggy, annoyed.
    anon "Not again..." # VA: Groggy, annoyed, exasperated.
    play sound audio.medusa_bed # ?
    stop ambience fadeout 0.2
    play sound "assets/sfx/medusa_sigh_relief.ogg"
    anon "There we go..." # VA: Relieved, relaxed.
    pause 3.0
    play ambience audio.medusa_alarm_2 loop # ?
    anon "Ugh!" # VA: Groggy, head pain. 
    play sound audio.medusa_bed # ?
    stop ambience fadeout 0.2
    play sound "assets/sfx/medusa_sigh_relief_2.ogg"
    anon "Nice and comfy now..." # VA: Purring, relieved as she settles under the covers for a second time. 
    pause 3.0
    play ambience audio.medusa_alarm_3 loop # ?
    anon "For fuck's sake!" # VA: Angry, furious mood. 
    anon "I swear on the phallus of Apollo this thing gets louder every day!" # VA: Angry, furious mood. Medusa edges close to the point of losing her temper.
    pause 2.0
    play sound audio.medusa_bed # ?
    stop ambience fadeout 0.2
    play sound audio.alarm_slam # ?
    scene cg medusa_slams_alarm with vpunch
    pause 2.0
    scene black
    anon "Finally." # VA: Relieved, exasperated. Medusa has finally silenced the alarm clock.
    pause 2.0
    play sound "assets/sfx/medusa_sigh.ogg"
    anon "Mondays." # VA: Groggy distaste for "Mondays."
    anon "The gut punch of the week." # VA: Strong, scornful emphasis on the word "gut punch."
    anon "And that means..." # VA: Slight, horrible realisation dawning on her.
    pause 2.0
    scene cg medusa_bed
    m "Oh no." # VA: Dread. Something horrible is about to happen.
    m "I have to head into divine daycare again." # VA: Dread. She really doesn't want to head there. 

    scene cg TITLE_kawada_studios_presents
    pause 2.0
    scene cg medusa_teeth_brush
    play sound audio.medusa_teeth_brush # ?
    pause 2.0
    scene cg TITLE_collab_potatoes
    pause 2.0
    scene cg medusa_dressed
    play sound audio.medusa_dressed # ?
    pause 2.0
    scene cg TITLE_kimia_kore_novel
    pause 2.0
    scene cg medusa_mirror_neutral
    m "Focus Meddy, focus." # VA: Medusa's nickname is Meddy. She uses it to calm herself down.
    scene cg medusa_mirror_happy
    m "You can do this." # VA: She says this to herself, trying to psych herself up for the day ahead.
    m "Today you ace your final exam..." # VA: Continued excitable pysching herself up.
    m "Get the hell out of Olympus University..." # VA: Continued excitable pysching herself up.
    m "And step into the myths for good!" # VA: End of excitable pysching herself up. Medusa is ready to take on the day, and the world. 
    scene cg medusa_door_day
    play sound audio.medusa_door_explosion # ?
    with vpunch
    scene cg medusa_door_explosion
    m "Cowabunga!" # VA: Triumphant exclamation, even after the door explodes off it's hinges. 
    scene cg TITLE_Extra with flash
    pause 2.0
    play sound "assets/sfx/medusa_hum_skate.ogg" loop
    scene cg hallway_medusa_skate # Medusa skating through the hallway.
    scene cg hallway_medusa_shade # Frontal shot of Medusa trying desperately to look cool, wearing dark shades.
    pause 2.0
    scene cg sphinx_door
    m "FOUND IT!" # VA: Excited squal of joy. One would even think for a moment that Medusa is happy to be in class.
    stop sound fadeout 0.5
    scene black
    play sound audio.door_open # ?
    pause 1.0
    play ambience "assets/sfx/class_talking.ogg" loop
    spx "Ahem!" # VA: Resounding firm sound. The Sphinx demands, not wants, obedience from her class.
    spx "Now class, is everyone ready for the exam?" # VA: Continued resounding firm sound.
    spx "Raise your hand if you are!" # VA: Continued resounding firm sound.
    pause 2.0
    spx "Good!" # VA: Pleased tone. Everything seems in order. Sphinx is happy with the class' readiness for the exam.
    spx "It seems like everyone is ready, except for..." # VA: She notices something is amiss.
    spx "Medusa, what are you doing?" # VA: Sudden shock. 
    spx "Why do you have a book in your-" # VA: Sudden fear. 
    play sound audio.book_throw
    m "FASCIST BASTARD!" # VA: Loud, defiant exclamation. Medusa is angry, and she is not afraid to show it.
    stop ambience fadeout 0.2
    pause 2.0
    scene cg classroom_sphinx
    spx "MEDUSA!" # VA: Loud scream of anger. 
    spx "GET OUT OF MY CLASSROOM!" # VA: Explosive scream of anger.
    pause 1.0
    scene black
    play sound audio.door_close # ?
    pause 1.0
    play sound audio.medusa_hallway_footsteps # ?
    pause 1.0
    play ambience "assets/sfx/zeus_hum.ogg" loop # VA: Zeus is humming to himself, heads in the cloud, oblivious to the world around him.
    anon "*Humming to himself*"
    pause 2.0
    play sound audio.zeus_door_open # ?
    stop ambience fadeout 0.2
    scene cg zeus_door_neutral
    scene cg zeus_door_frown
    play sound "assets/sfx/zeus_sigh.ogg"
    scene cg medusa_office
    scene black with Dissolve(3.0)
    return

label demo_fencing:
    scene black
    play ambience audio.fencing loop # ?
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_01.ogg"
    d "Crap. Crap. Crap."
    n "You know, running away from Athena like that isn't going to help you win." # VA: Matter-of-fact.
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_02.ogg"
    d "Oh shut up, Nike."
    he "Listen to her Dionysus." # VA: Worried, steady.
    he "Before you make the same mistake I did." # VA: Serious warning.
    n "Obviously, fencing and pint-sized steampunk nerds don't mix." # VA: Playful jab.
    he "Shut up, Nike." # VA: Flat, gruff.
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_03.ogg"
    d "Oh fuck."
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_04.ogg"
    d "Fuck! Fuck! Fuck!"
    a "One..." # VA: Calm count, controlled and confident.
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_05.ogg"
    d "OH NO!"
    a "Two..." # VA: Same calm count, tightening pressure.
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_06.ogg"
    d "BY THE FATES, HAVE MERCY!"
    a "Three..." # VA: Crisp finish to the count, ready to strike.
    stop ambience fadeout 0.2
    play sound audio.fencing2 # ?
    show cg athena_dionysus_fencing with fade
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_07.ogg"
    d "Ugh. You win again, Athena."
    n "Amazing work, as always." # VA: Warm praise.
    he "Flawless Victory!" # VA: Like Shao Khan from Mortal Kombat.
    a "Enough with the video game references!" # VA: Playful annoyance. Athena is trying to restore order.
    a "Time for a water break." # VA: Coach-like and practical.
    show bg fencing with fade
    show athena_fencing_neutral at Position(xalign=0.5) with dissolve
    show dionysus_fencing_neutral at Position(xalign=0.7) with dissolve
    show nike_neutral at Position(xalign=0.3) with dissolve
    show hephaestus_neutral at Position(xalign=0.9) with dissolve
    a "So guys, what are our plans tonight?" # VA: Casual, friendly reset after training.
    show nike_excited at Position(xalign=0.3)
    n "HESTIA'S HOMEBREW!" # VA: Excited exclaim.
    show dionysus_fencing_tired at Position(xalign=0.7)
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_08.ogg"
    d "...We've been there like a billion times already, Nike."
    show nike_annoyed at Position(xalign=0.3)
    n "Well, where else could we go then?" # VA: Annoyed pushback.
    n "Wait, don't tell me it's the Hanging Gardens, Dionysus?" # VA: Annoyed pushback.
    show hephaestus_curious at Position(xalign=0.9)
    he "Why not? I've never been." # VA: Curious, casual.
    show nike_sick at Position(xalign=0.3)
    n "They make seafood." # VA: Grossed out. 
    he "So? I thought you'd like that, Nike." # VA: Oblivious, teasing.
    he "Being buddy-buddy with Professor Poseidon and all." # VA: Joking, still oblivious.
    show nike_angry at Position(xalign=0.3)
    n "We're NOT buddies." # VA: Sharp defensive denial. 
    show nike_embarrassed at Position(xalign=0.3)
    n "He's just my professor in Marine Biology, that's all." # VA: Embarrassed, flustered, downplaying.
    show dionysus_fencing_happy at Position(xalign=0.7)
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_09.ogg"
    d "And your track & field coach too."
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_10.ogg"
    d "And the first person you turn to when you need homework help."
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_11.ogg"
    d "And the guy you dote on and make sappy poems about in your spare time."
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_12.ogg"
    d "And sometimes he even catches you making lovey-dovey faces at him in class when you think no one is looking."
    show nike_red at Position(xalign=0.3)
    show hephaestus_happy at Position(xalign=0.7)
    show athena_fencing_happy at Position(xalign=0.5)
    play sound "assets/sfx/hephaestus_snort.ogg"
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_13.ogg"
    d "If I wasn't such a self-induced dullard from all my drunken wine escapades..."
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_14.ogg"
    d "I'd suspect you might even have a crush on him, Nike."
    show nike_angry at Position(xalign=0.3)
    n "Shut Up." # VA: Angry, full stop.
    a "I take it that means we're going to the Hanging Gardens then?" # VA: Teasing, pretending to be oblivious.
    a "We might even get a glimpse of Professor Poseidon there, who knows?" # VA: Teasing, good-natured.
    n "Shut." # VA: Clipped warning.
    n "Up." # VA: Hard stop.
    he "I know the prospect of that just brightens Nike's day, Athena." # VA: Teasing, good-natured.
    play sound "assets/sfx/athena_snort.ogg"
    play ambience audio.athena_phone loop # ?
    show athena_fencing_annoyed at Position(xalign=0.5)
    a "Gods, who could that be now?" # VA: Annoyed, frustrated. 
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_15.ogg"
    d "I wonder what the chances of that are, Hephaestus?"
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_16.ogg"
    d "20%%? 30%%? 50%%?"
    he "Honestly, I'm surprised Nike hasn't arranged a dinner date with Poseidon already." # VA: Deadpan joke.
    he "Given how relentless her pursuit of him is." # VA: Dry follow-up.
    show nike_tired at Position(xalign=0.3)
    n "...Shut up, Hephaestus." # VA: Tired mumble, no fight left. Defeated. 
    show athena_fencing_phone at Position(xalign=0.5)
    a "Sorry guys, I have to take this." # VA: Apologetic, polite. Athena doesn't want to be away from her friends, but she has to take the call. 
    show dionysus_fencing_surprised at Position(xalign=0.7)
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_17.ogg"
    d "EVERYONE QUIET DOWN! ATHENA IS ABOUT TO MAKE A VERY IMPORTANT PHONE CALL!"
    show hephaestus_neutral at Position(xalign=0.9)
    show nike_neutral at Position(xalign=0.3)
    show dionysus_fencing_neutral at Position(xalign=0.7)
    stop ambience fadeout 0.2
    play sound audio.phone_click # ?
    show athena_fencing_call_eyes_open at Position(xalign=0.5)
    a "Hello?" # VA: Warm and professional.
    z "Is this my wondrous daughter I'm speaking to?" # VA: Warm, proud, fatherly, slightly eccentric. 
    pause 1.0
    a "...Yes, it is." # VA: Polite, but slightly annoyed. Athena doesn't like being called wondrous, even by Zeus. 
    a "I wished he didn't call me wondrous." # VA: Internal monologue, annoyed, frustrated. This is the only place where Athena gets to vent her frustrations from the outside world. 
    a "All the praise from everyone else around me was tiresome enough." # VA: Internal monologue, annoyed, frustrated. End of monologue.
    pause 1.0
    show athena_fencing_call_eyes_closed at Position(xalign=0.5)
    a "Is there something you wanted to talk to me about, father?" # VA: Polite, but she really wishes she was with her friends. 
    z "Yes! I did!" # VA: Excited.
    z "How's your schedule looking for this afternoon?" # VA: Curious, fatherly.
    show athena_fencing_call_eyes_open at Position(xalign=0.5)
    a "Well, I have to help Hermes go over some notes before his final exam in Latin..." # VA: Neutral, beginning of long-winded explanation.
    pause 1.0
    show dionysus_fencing_happy at Position(xalign=0.7)
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_18.ogg"
    d "...You'd think he'd pick Greek instead, but Latin is the domain of hipster gods, I guess."
    show nike_angry at Position(xalign=0.3)
    n "Shush!" # VA: Quick cutoff.
    pause 1.0
    a "Then I was thinking about heading to the great Alexandrian library to do some research for my final project..." # VA: Continutation of long-winded explanation. 
    a "Then I have to take a class on the history of the underworld with Persephone..." # VA: Athena doesn't seem to realise (or care) that this is a whole lot for one person to do.
    a "But since she's on leave right now with custodian Hades, I have to teach the other students in the class for her..." # VA: Continued long-winded explanation, matter-of-fact.
    z "Forget all that!" # VA: Abrupt cutoff.
    z "Are you free right now?" # VA: Not so sublty asking Athena to drop everything and come to his office.
    pause 1.0
    a "Umm...I guess I am." # VA: Neutral, suddenly overwhelmed.
    z "Great! Come down to my office then, would you?" # VA: Upbeat, decisive.
    z "Love you, daughter!" # VA: About to hang up, but still excited.
    a "Wait, what's this all about?" # VA: Confused, concerned.
    pause 1.0
    z "..." # VA: Listening beat.
    z "..." # VA: Measured pause.
    a "...I see." # VA: # Understanding, but disappointed.
    a "But I did promise Hermes we'd go over his notes together." # VA: Brief pushback.
    z "Very well, but please make sure to come to my office after that, all right?" # VA: Relents, but still excited.
    a "Alright." # VA; Short, clipped. 
    z "Love you, my wonderful daughter!" # VA: Zeus loves getting the last word in, even if it means repeating himself.
    a "...Love you too, father." # Going through the motions, but isn't really feeling it. 
    play sound audio.phone_hangup # ?
    pause 2.0
    show athena_fencing_annoyed at Position(xalign=0.5)
    a "Ugh." # Frustrated, annoyed.
    a "Just my luck for being the Rector's daughter." # Exhausted, exasperated.
    show nike_worried at Position(xalign=0.3)
    n "What's wrong, Athena?" # VA: Concerned, gentle.
    a "It's..." # VA: Athena finds it hard to get the words out. 
    show dionysus_fencing_neutral at Position(xalign=0.7)
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_19.ogg"
    d "Come on." 
    voice "assets/voice/Dionysus/dionysus_demo_fencing/demo_fencing_dionysus_20.ogg"
    d "Spit it out already."
    he "Yeah, Athena." # VA: Concerned, supportive.
    he "Tell us." # VA: Gentle push.
    pause 2.0
    a "...It's Medusa." # VA: Hesitant, nervous but finally gets it out.
    scene black
    return

label demo_office:
    scene black
    play ambience audio.tapping_desk loop
    pause 2.0
    play sound "assets/sfx/zeus_sigh.ogg"
    z "Eight years." # VA: Weary, tired exhale.
    z "Eight years of this." # VA: Continued weary tone.
    z "The most troublesome and mischievous student I've ever had." # VA: Continued weary tone.
    z "In all my years acting as the Rector of Olympus University." # VA: Continued weary tone.
    scene bg zeus_office with Dissolve(3.0)
    show zeus_stern at Position(xalign=0.3)
    show medusa_neutral at Position(xalign=0.7)
    pause 2.0
    z "Do you know why you are here, Medusa?" # VA: Firm. 
    m "...Throwing a book at an exchange professor?" # VA: Pretending to be oblivious.
    z "Well that..." # VA: Matter-of-fact, but not the main point.
    z "And the fact she's left Olympus University already..." # VA: Building the case.
    z "Which no doubt has sullied our reputation in the eyes of the other pantheons..." # VA: Deep reputational concern for Olympus.
    z "All because of you and your reckless behaviour." # VA: Firm reprimand.
    show medusa_sad at Position(xalign=0.7)
    pause 2.0
    show zeus_tired at Position(xalign=0.3)
    stop ambience fadeout 0.2
    play sound "assets/sfx/zeus_sigh.ogg"
    z "I'm not giving up on you, Medusa." # VA: Steady resolve. He doesn't want to give up on her. 
    m "I wish you would, in a way." # VA: Sad, resigned tone. Medusa feels she's a hopeless basket case.
    m "We've been at this for eight years now." # VA: Continuation of sad, resigned tone.
    m "And I still feel like the same dolt I was when I first came here." # VA: Continuation of sad, resigned tone.
    m "It's hopeless." # VA: Continuation of sad, resigned tone.
    m "I'll never graduate from Olympus University." # VA: Continuation of sad, resigned tone. She really does believe this, that she'll never graduate. 
    play sound "assets/sfx/medusa_sigh.ogg"
    pause 2.0
    show zeus_determined at Position(xalign=0.3)
    z "That's why the faculty and I have decided to take a different approach with you." # VA: Testing the waters, but still firm.
    z "In order to help you finish your studies." # VA: Reassuring intent.
    show medusa_surprised at Position(xalign=0.7)
    m "Huh, what's that?" # VA: Surprised, tone. It causes Medusa to perk up a little. 
    z "Do you know who Athena is?" # VA: Probing question.
    pause 2.0 # A Beat to let the question sink in.
    m "Athena?" # VA: Confused. Medusa knows who Athena, but she doesn't know why Zeus is asking her about her.
    z "Yes, Athena." # VA: Patient.
    m "You mean Pallas Athena?" # VA: Still confused, but now a little more curious.
    m "Your daughter?" # VA: Subtle hint that Medusa is starting to understand the situation.
    show zeus_neutral at Position(xalign=0.3)
    z "Yes, is there anything wrong with that?" # VA: Patient, considerate.
    m "No, no, it's just..." # VA: Trying to play it cool, but still her nerves are getting the better of her.
    z "You do know who Athena is, don't you?" # VA: Incredulous, getting impatient.
    show medusa_nervous at Position(xalign=0.7)
    pause 2.0
    m "Of course I knew who Athena was." # VA: Beginning of Medusa's internal monologue.
    m "Who didn't?" # VA: She finds it hard to believe that Zeus would even ask her such a question.
    m "She was the perfect student." # VA: Not praise, not envious, but the reality of Athena's character.
    m "Brilliant, clever, selfless and not going to be spending the rest of her life on campus like me." # VA: Medusa can see the contrast between herself and Athena, and it makes her feel even worse about herself.
    m "She was everything that I wasn't." # VA: Medusa's internal monologue, sharp, overtly critical of herself.
    play sound "assets/sfx/medusa_sigh.ogg"
    pause 1.0
    z "Athena is nearing the end of her Goddess degree here at Olympus University." # VA: Brief explanation.
    z "But before she can graduate, she has to complete a final project." # VA: The setup.
    pause 2.0
    show medusa_annoyed at Position(xalign=0.7)
    m "Which is...?" # VA: Annoyed tone. She can sense Zeus is planning something, and wants him to get on with it.
    show zeus_determined at Position(xalign=0.3)
    z "She has to take on a student as a follower and guide them..." # VA: Careful reveal.
    m "So I am to be her test monkey then?" # VA: Quick cut-in. She's beginning to feel defensive once more. 
    play sound "assets/sfx/zeus_sigh.ogg"
    show zeus_tired at Position(xalign=0.3)
    pause 1.0
    z "Not a test monkey, Medusa." # VA: Gently correcting.
    z "A follower." # VA: Deliberate emphasis.
    z "A priestess, if you will." # VA: Reframing the role in a more mythology-friendly way.
    show medusa_eyebrow at Position(xalign=0.7)
    m "So I have to be her priestess?" # VA: Raised eyebrow, incredulous. She can't believe what she's hearing.
    m "And she will be my...?" # VA: Continued incredulous tone. She can't believe what she's hearing.
    z "Goddess, of course." # VA: Bingo, the perfect word to describe Athena's role in this arrangement.
    pause 2.0
    show medusa_neutral at Position(xalign=0.7)
    m "I see." # VA: Neutral tone. Medusa is quietly processing what she's heard. 
    m "I started to mull the idea in my mind." # VA: Beginning of Medusa's internal monologue. She isn't sure what to make of it. 
    m "This was the Rector's incredibly bizarre way of saying..." # VA: Continued internal monologue. It really does come off as bizarre to her. 
    m "Yes Medusa, you're quite the troublemaker..." # VA: Continued internal monologue. She can see the truth in it, but it still stings.
    m "And we need someone to chaperone and keep an eye on you..." # VA: Continued internal monologue. Feels like something from a 90's sitcom, but she can see the truth in it.
    m "So here's my daughter, only a few credits shy of graduating..." # VA: Continued internal monologue. Zeus pragmatic solution is not lost on her. 
    m "And you can be her final project." # VA: End of internal monologue. It all comes together nicely in her mind when it's described like that. 
    m "..." # VA: Internal monologue pause, quietly overwhelmed.
    pause 2.0
    show zeus_neutral at Position(xalign=0.3)
    z "This will kill two griffons with one stone." # VA: Practical optimism.
    z "Are you up for it, Medusa?" # VA: Gentle, probing question, but he really wants her to do it.
    pause 1.0
    menu m_choice:
        "What do you choose?"
        "Umm...":
            show medusa_confused at Position(xalign=0.7)
            m "I mean..." # VA: Hesitant, unsure.
            m "I don't have much of a choice, do I?" # VA: Resigned, but still hoping for a way out.
            z "No, you don't. But I know you can do it, Medusa." # VA: Firm encouragement.
    pause 1.0
    m "..." # VA: Internal beat, still uncertain.
    m "It could be a change." # VA: Beginning of Medusa's internal monologue. Medusa is trying to find a silver lining in this arrangement.
    m "A fresh start." # VA: Continued internal monologue.
    m "But I wasn't sure if Athena and I would click." # VA: Continued internal monologue. She's lowkey worried if her and Athena will even get along.
    m "At all." # VA: End of internal monologue.
    pause 1.0
    z "...I can't force it upon you, of course." # VA: Softening his tone.
    z "But Athena's well versed in all the subjects you struggle with." # VA: Practical reassurance.
    z "And I'm sure she can help you out with your studies." # VA: Confident reassurance.
    pause 1.0
    m "It could even be a chance to make a new friend." # VA: Beginning and end of Medusa's internal monologue. A much softer, reflective tone. 
    pause 2.0
    show medusa_happy at Position(xalign=0.7)
    m "Alright, I'll give it a shot." # VA: Happy, excited tone. Medusa for the first time since coming to Zeus office, appears to be in better spirits.
    show zeus_happy at Position(xalign=0.3)
    z "Wonderful news, Medusa!" # VA: Delighted.
    z "I'll send her a letter to fetch her later on!" # VA: Excited momentum.
    show medusa_confused at Position(xalign=0.7)
    m "Umm..." # VA: A bit confused. 
    m "I think it would be easier to phone her instead." # VA: Practical, matter-of-fact. They live on a modern campus, after all. It's not like they have to send letters anymore like in Ancient Greece.
    show medusa_neutral at Position(xalign=0.7)
    z "Right! Phone her! Will do!" # VA: Quick enthusiastic pivot.
    m "..." # VA: Brief pause before leaving, composed.
    m "I'll take my leave then." # VA: Polite, neutral tone. She doesn't want to stay and see Zeus get too excited about this arrangement. 
    hide medusa_neutral with Dissolve(0.5)
    play sound audio.medusa_hallway_footsteps # ?
    play sound audio.zeus_door_open # ?
    pause 1.0
    show zeus_excited at Position(xalign=0.3)
    z "YES! YES! YES! YES! YES! YES! YES!" # VA: Explosive celebration. Finally, the Gorgon is out of his hair.
    pause 1.0
    m "I can still hear you from outside here, you know." # VA: Firm reprimand. Not unlike the ones Zeus gave to her at the start of the scene. 
    show zeus_embarrassed at Position(xalign=0.3)
    z "Oh, sorry about that. I just got a little excited." # VA: Embarassed comedown.
    pause 1.0
    scene black
    with fade
    return

label demo_fencing_2:
    scene black
    play sound "assets/sfx/athena_sigh.ogg"
    a "Please stop calling her all those foul names." # Defensive. Even though she doesn't know Medusa, she doesn't like it when others call her names.
    scene bg fencing
    show athena_fencing_neutral at Position(xalign=0.5)
    show dionysus_fencing_angry at Position(xalign=0.7)
    show nike_angry at Position(xalign=0.3)
    show hephaestus_angry at Position(xalign=0.9)
    pause 1.0
    voice "assets/voice/Dionysus/dionysus_demo_fencing2/demo_fencing2_dionysus_01.ogg"
    d "Foul language?"
    voice "assets/voice/Dionysus/dionysus_demo_fencing2/demo_fencing2_dionysus_02.ogg"
    d "What about her foul behaviour?"
    show athena_fencing_annoyed at Position(xalign=0.5)
    pause 1.0
    a "She just needs a little bit of help, that's all." # VA: Defensive but gentle. Athena is trying to de-escalate.
    show nike_smug at Position(xalign=0.3)
    play sound "assets/sfx/nike_snort.ogg"
    n "Yes, as if giving her every advantage to pass through Medieval Greek wasn't enough on your father's part." # VA: Snide, snorting.
    he "Dictionaries, cheat sheets, having other students do her assignments and essays." # VA: Matter-of-fact pile-on.
    voice "assets/voice/Dionysus/dionysus_demo_fencing2/demo_fencing2_dionysus_03.ogg"
    d "Now since our Rector can't solve the problem, he's decided to shift the burden onto his daughter."
    show athena_fencing_sad at Position(xalign=0.5)
    pause 2.0
    a "You're just in a bad mood." # Athena's voice lacks any real conviction.
    voice "assets/voice/Dionysus/dionysus_demo_fencing2/demo_fencing2_dionysus_04.ogg"
    d "I'm in a bad mood?"
    voice "assets/voice/Dionysus/dionysus_demo_fencing2/demo_fencing2_dionysus_05.ogg"
    d "What about your father having to deal with that headache for eight years on his own?"
    pause 1.0
    a "..." # VA: Silent beat. Athena bites back a response.
    voice "assets/voice/Dionysus/dionysus_demo_fencing2/demo_fencing2_dionysus_06.ogg"
    d "He always looks so stressed when he's finished dealing with Snakehead!"
    voice "assets/voice/Dionysus/dionysus_demo_fencing2/demo_fencing2_dionysus_07.ogg"
    d "And then a few months ago, Zeus was almost in tears when he caught her scribbling on the walls of the library with a marker!"
    show athena_fencing_neutral at Position(xalign=0.5)
    a "Enough." # VA: Flatly. This is the end of the conversation. Athena is tired of hearing the others pile on about Medusa's misdeeds. 
    a "I'll see you next week for our next lesson." # VA: Flatly. She wants to get out of this conversation as quickly as possible.
    scene black with fade
    pause 2.0
    play sound audio.athena_fencing_footsteps # ?
    play sound audio.fencing_door_open_close # ?
    pause 1.0
    play sound "assets/sfx/athena_sigh.ogg"
    show cg athena_changing_room
    a "Am I really just cleaning up my father's mistakes?" # VA: Beginning of Athena's internal monolgue. Ruminating, reflective.
    pause 2.0
    a "No matter how hard I tried to run away from it..." # VA: Continued internal monologue. She can't escape the reality of her situation.
    a "Dionysus's words echoed in my mind." # VA: Continued internal monologue. Or escape Dionysus's backbiting words.
    pause 2.0
    a "Snakehead." # VA: Exasperated. Even the nickname seems to wear Athena down. 
    scene black with Dissolve(3.0)
    return

label demo_forest:
    scene black
    play ambience audio.forest_ambience loop # ?
    pause 1.0
    m "This is my forest." # Beginning of Medusa's internal monologue.
    m "Well, technically Groundskeeper Pan's forest, but I like to think it's mine." # VA: Continued internal monologue. Possessive tone. She wants to think the forest is hers. 
    scene bg forest
    with Dissolve(3.0)
    m "The place I hung out when I wanted to be alone." # VA: Continued internal monologue. Lonely, wistful. 
    m "The place I went when everything in life was too much for me to handle." # VA: Continued internal monologue. Lonely, wistful. The memories are painful. 
    m "Where I could just be myself and not have to worry about anything." # VA: Continued internal monologue. Deep down, she wished she wasn't by herself in those memories. 
    show medusa_pond_neutral at Position(xalign=0.7) with dissolve
    m "When I was really down in the dumps, I'd come here and sit inside this pond for hours." # VA: Continued internal monologue. She pretends that this wasn't painful as she speaks. 
    m "I couldn't get an entry into Pan's forest pool." # VA: Continued internal monologue. Frustrated tone. She wanted to be there. 
    m "The one where the nymphs acted as lifeguards." # VA: Continued internal monologue. Frustrated tone. She wanted to be there.
    m "And dryads and satyrs had impromptu volleyball matches." # VA: Continued internal monologue. Frustrated tone. She wanted to be there.
    m "Nobody wanted the gorgon troublemaker around them." # VA: 
    m "So I had to make due with my own." # VA: Continued internal monologue. The lonely, wistful tone returns. She wanted to be there, but she couldn't.
    pause 1.0
    show medusa_pond_sigh at Position(xalign=0.7)
    stop audio fadeout 0.5
    play audio "assets/sfx/medusa_sigh.ogg"
    pause 1.0
    m "Things could be a whole lot worse." # VA: Continued internal monologue. She tries to find a silver lining in her situation.
    m "I had this place to myself at least." # VA: Continued internal monologue.
    m "For now." # End of Medusa's internal monologue.
    pause 1.0
    play sound audio.athena_forest_footsteps_1 # ?
    show medusa_pond_surprised at Position(xalign=0.7)
    m "Huh, who's that?" # VA: Sudden alert. Nobody comes this far into the forest, so she is surprised to hear someone. 
    pause 1.0
    play sound audio.athena_forest_footsteps_2 # ?
    pause 1.0
    a "Σκατά! I have stepped on centaur dung." # VA: Athena swears for the first time, albeit in Greek. Which shows how important the sandals are to her.
    m "Pan is such an uncivilized brute!" # VA: Snapping, much unlike the gentle Athena we've seen so far. 
    a "And those were my best sandals too!" # VA: Deeply upset, disgusted. Centaur dung is not something you want to step in, especially when you're wearing sandals.
    a "Μαλάκα!" # VA: Athena swears again in Greek. She is really upset about stepping in the dung.
    play sound audio.athena_forest_footsteps_3 # ?
    pause 1.0
    show athena_robes_neutral at Position(xalign=0.3)

    a "Medusa Margoyles?" # VA: Neutral tone. It happens so fast that Athena doesn't realise the mistake she's made.
    play sound "assets/sfx/athena_gasp.ogg"
    show athena_robes_mouth_covered at Position(xalign=0.3)
    play sound "assets/sfx/medusa_ugh.ogg"
    show medusa_pond_annoyed at Position(xalign=0.7)
    m "...That's my nickname on campus, dear player." # VA: Annoyed. She's used to being called that, but she doesn't like it.
    pause 1.0
    show medusa_pond_arm_raised at Position(xalign=0.7)
    m "HERE!" # VA: Dull chirp, like a student who's name has been called in class. 
    m "You called?" # VA: Neutral tone, like this meeting is the most mundane thing in the world.
    show athena_robes_neutral at Position(xalign=0.3)
    a "I have." # VA: Neutral tone. Athena is trying to be polite, but she doesn't know how to approach Medusa.
    a "I am Athena, daughter of Zeus and goddess of wis-" # VA: Neutral tone. Athena's often makes the mistake of lofty introductions, but she doesn't realise that Medusa is already aware of who she is.
    show medusa_pond_dismissive at Position(xalign=0.7)
    m "Blah, blah, blah. I know who you are." # VA: Dismissive, annoyed. Medusa just wants to get this over with as fast as possible. 
    show athena_robes_annoyed at Position(xalign=0.3)
    m "You're Athena. The golden girl on campus." # VA: Annoyed, matter-of-fact. Medusa is trying to get this over with as fast as possible.
    m "I know all that crap already." # VA: Rushing through, annoyed. 
    pause 2.0
    a "...Well, I'm sure you already know this then, but I'm going to be your mentor for the next few months." # Neutral tone, but the irritation is starting to show. She tries to remain polite. 
    show medusa_pond_annoyed at Position(xalign=0.7)
    m "Goddess, you mean." # VA: Snarky, cut in.
    m "Let's not downplay it." # VA: To the point.
    m "At all." # VA: To the point.
    pause 2.0
    a "...Correct. Goddess." # VA: Trying to remain calm, but the irritation is beginning to boil over.
    a "And you are to be my priestess, Medusa." # VA: Trying to remain calm, but we're moments from disaster.
    menu m_priestess:
        "How do you respond?"

        "Keep your mouth shut and nod":
            show medusa_pond_sigh at Position(xalign=0.7)
            $ friends += 1
            $ rivals += 1
            m "Sure, I guess." # VA: Resigned, but still annoyed. She doesn't want to be here, but she has no choice.
            m "I mean, someone has to help me get through my final year of university, right?" # VA: Resigned acceptance, trying to sound practical.
            a "Yes, that's right." # VA: Polite, but still trying to remain calm. The irritation from earlier is gone. 
            m "But I can't hack these tests or exams." # VA: Resigned, but Medusa can't her hide her frustration.
            m "At all." # VA: Still frustrated, but she can't help it.

        "Piss Athena off by being sarcastic":
            $ enemies += 1
            $ rivals += 1
            m "And you're doing all this to get those extra credits, right?" # VA: Sarcastic jab. Medusa pushes Athena's buttons to their limits.
            m "Finally ascend your way into Goddesshood?" # VA: Continued sarcasm, needling tone.
            m "And leave me and Olympus University in the dust, right?" # VA: Bitter and accusatory.
            m "Right?" # VA: Sharp insistence, forcing a response.
            show athena_robes_angry at Position(xalign=0.3)
            play sound "assets/sfx/athena_angry.ogg"
            show medusa_pond_scared at Position(xalign=0.7)
            a "Yes, you caught me!" # VA: Angry, rapid fire vent. She isn't afraid to show it. 
            a "I'm doing this all for the love of credits!" # VA: Angry, rapid fire vent.
            a "And not because I want to learn how to look after someone who chooses to follow me!" # VA: Angry, rapid fire vent.
            a "Which is what any goddess would do!" # VA: Angry, rapid fire vent.
            pause 2.0
            play sound "assets/sfx/athena_sigh.ogg"
            show athena_robes_tired at Position(xalign=0.3)
            a "I didn't mean to snap like that." # VA: Regretful, apologetic.
            a "That was...terribly out of character for me." # VA: Regretful, apologetic. Totally out of character for Athena. 
            pause 2.0
            show medusa_pond_happy at Position(xalign=0.7)
            m "It's okay, I get it." # VA: Happy, understanding. Medusa is trying to be understanding of Athena's outburst.
            m "It just happens when you're around poor old Medusa." # VA: Happy, understanding, slight self-depracting humor. Emphasis on "Poor Old Medusa."
            m "The perennial senior who can't get her act together." # VA: Medusa's aware of how much of a mess she is, and she's trying to make light of it.
            m "Who can't even graduate from university." # VA: Continuation of that.. 

    pause 2.0
    show athena_robes_determined at Position(xalign=0.3)
    a "You just need to study more, Medusa." # VA: Neutral tone, like this is a simple solution.
    a "I didn't get everything right on my first go, either." # VA: Reassuring and sincere. Athena tries to normalize struggle.
    show medusa_pond_sad at Position(xalign=0.7)
    m "But these tests haven't been my first go in years now!" # VA: Exasperated sound. She's heard this countless times. 
    a "I know. That's why I'm here." # VA: Determined. She really wants to help Medusa, and she wants to make sure she succeeds.
    a "To make sure they're your last." # VA: Determined. She really wants to help Medusa, and she wants to make sure she succeeds.
    pause 2.0
    show medusa_pond_sigh at Position(xalign=0.7)
    m "I thought I should snap back." # VA: Beginning of Medusa's internal monologue. She's trying to find a silver lining in this arrangement.
    m "We'd had a bit of a rough start, but I felt at least we'd come to an understanding." # VA: Reflective internal monologue, cautiously hopeful.
    m "She wanted to help me, and I wanted to be helped." # VA: Soft, honest realisation.
    m "She wanted to cross the finish line, and get her degree." # VA: Thoughtful, connecting their goals.
    m "...And so did I, deep down." # VA: Quiet admission, even if she won't admit this to Athena or in public yet.
    pause 2.0
    m "...Does this mean I'm going to have to go through my Greek conjugations right now?" # VA: Nervous dread with a comedic edge.
    m "Anything but that, I thought." # VA: Internal groan, dramatic despair. She hates her Greek. 
    show athena_robes_happy at Position(xalign=0.3)
    a "No, not yet." # VA: Reassuring calm.
    a "Instead, we'll do something you'd like to do." # VA: Warm, deliberate kindness. Athena's true nature shines through here, and Medusa is touched by it.
    show medusa_pond_eyebrow at Position(xalign=0.7)
    m "Something I like to do?" # VA: Surprised, almost disbelieving.
    pause 2.0
    m "It was the first time anyone had ever asked me what I wanted to do." # VA: Internal monologue, stunned, reflective.
    m "The first time, like ever." # VA: Quiet emphasis, still processing it.
    pause 2.0
    a "Yes. Think of something and we'll do it together." # VA: Patient, encouraging.
    show medusa_pond_eyebrow at Position(xalign=0.7)
    pause 2.0
    m "Well..." # VA: Hesitant, thinking out loud.
    m "How about..." # VA: Hesistant mumbling.
    menu m_athena_activity:
        "What do you choose?"

        "The Owl House":
            $ friends += 1
            $ rivals += 1
            m "How about The Owl House?" # VA: Careful ask, hopeful underneath.
            show athena_robes_thinking at Position(xalign=0.3)
            a "The Owl House?" # VA: Clarifying repeat, curious.
            m "Yeah, the Owl House." # VA: Simple confirmation.
            pause 1.0
            play sound audio.athena_lightbulb # ?
            show athena_robes_lightbulb at Position(xalign=0.3)
            pause 2.0
            show athena_robes_happy at Position(xalign=0.3)
            a "Oh. You mean the mews!" # VA: Lightbulb moment, upbeat correction.
            show medusa_pond_annoyed at Position(xalign=0.7)
            m "Everyone just calls it the Owl House, Athena." # VA: Mildly annoyed correction.
            pause 2.0
            show medusa_pond_sad at Position(xalign=0.7)
            m "But I've never been." # VA: Softer tone, hint of embarrassment.
            show athena_robes_neutral at Position(xalign=0.3)
            a "Why not?" # VA: Gentle curious probe.
            pause 2.0
            m "...Snakes and birds of prey don't usually mix." # VA: Uneasy honesty. This doesn't come naturally to Medusa, but she wants to be honest with Athena.
            m "But if you're there, I might feel safe." # VA: Trusting, vulnerable. This is the beginning of their bond.
            show athena_robes_happy at Position(xalign=0.3)
            a "I am the head of it, I suppose." # VA: Modest pride.
            a "Alongside a billion other clubs on campus." # VA: Dry, self-aware humor.
            show athena_robes_determined at Position(xalign=0.3)
            a "Very well. I'll show you the Mews." # VA: Decisive and reassuring.
            show medusa_pond_annoyed at Position(xalign=0.7)
            m "...The Owl House." # VA: Insistent, slightly irked correction.
            a "Yes, Owl House!" # VA: Quick, confident concession.
            a "...Just get dressed, would you?" # VA: Practical, slightly flustered.
            m "Alright." # VA: Agreeable, easy.
            scene black with Dissolve(3.0)
            pause 1.0
        "Get into the pond with me":
            $ friends += 1
            $ lovers += 1
            show medusa_pond_happy at Position(xalign=0.7)
            m "Why don't you come in here with me?" # VA: Playful invitation. Medusa knows what she's doing, and she wants to see how Athena reacts.
            a "What?" # VA: Sudden surprise.
            m "I'm serious. Get in." # VA: Bold challenge. She really wants to see how far Athena will go.
            a "...But I don't have my swimming gear with me." # VA: Flustered objection. 
            m "So? I'm not wearing mine either." # VA: Casual confidence. She really wants to see Athena get in the pond with her.
            show athena_robes_red at Position(xalign=0.3)
            m "For a moment, I felt her cheeks flush." # VA: Internal monologue, observant and amused.
            m "She was embarrassed about stripping down in front of me." # VA: Continued internal monologue, teasingly curious.
            m "I didn't think she was used to it." # VA: Continued internal monologue, thoughtful.
            m "Even in front of other women." # VA: Continued internal monologue, quietly surprised.
            pause 2.0
            m "C'mon, for the day that's in it." # VA: Warm coaxing.
            a "..." # VA: Silent beat. Athena weighs it up.
            show athena_robes_neutral at Position(xalign=0.3)
            a "Hmph, alright." # VA: Reluctant acceptance. She's still a little embarrassed, but she wants to make Medusa happy.
            a "I did say something that you'd like to do." # VA: Principled follow-through. The Athena way.
            m "Yup." # VA: Satisfied little nod in her voice.
            m "Now get in." # VA: Playful command. Not unlike an officer telling a recruit to jump into the water.
            show athena_bra_neutral at Position(xalign=0.3)
            show medusa_pond_blush at Position(xalign=0.7)
            m "Oh my." # VA: Flustered admiration.
            show athena_bra_happy at Position(xalign=0.3)
            a "What?" # VA: Curious, slightly wary.
            m "Nothing." # VA: Trying to play it off.
            m "It's just..." # VA: Hesitant, searching for words.
            a "Just...?" # VA: Prompting, impatiently curious. Athena wants to know what Medusa is thinking.
            pause 2.0
            show medusa_pond_happy at Position(xalign=0.7)
            m "Redheads shouldn't wear red, you know." # VA: Unsubtle critique.
            show athena_bra_annoyed at Position(xalign=0.3)
            a "Ugh." # VA: Annoyed groan.
            show medusa_pond_annoyed at Position(xalign=0.7)
            m "Just get your butt in here, golden girl!" # VA: Playful taunt. 
            pause 2.0
            scene black with fade
            play sound audio.athena_pond_footsteps # ?
            scene cg athena_medusa_pond with Dissolve(2.0)
            play ambience audio.pond loop # ?
            m "See?" # VA: Triumphant little nudge.
            m "Not so bad now, is it?" # VA: Gentle teasing, warm.
            a "..." # VA: Quiet beat. She softens.
            a "I guess not." # VA: Reluctant but genuine concession.
            scene black with fade
            pause 1.0
    m "So tell me." # VA: Curious, impatient reset.
    m "How does this Goddess and Priestess thing work again?" # VA: Earnest question, trying to understand the arrangement.
    stop ambience fadeout 0.5
    return

label demo_stairs:
    scene black
    a "So you've never been inside this place?" # VA: Casual curiosity.
    m "Never. Rector Zeu-" # VA: Starting matter-of-fact before cutting herself off.
    pause 2.0
    m "Your daddy." # VA: Teasing emphasis on Daddy. She wants to see how Athena reacts to the word.
    a "My daddy?" # VA: Immediate disbelief. 
    m "Forbid me from coming in." # VA: Deadpan explanation.
    a "Please don't call him my daddy, Medusa." # VA: Polite but strained correction. One already knows how she feels about the word, and she doesn't want to hear it again.
    pause 2.0
    m "...But that's what he is." # VA: Unbothered logic. Medusa knows how Athena feels about the word, but she doesn't care.
    m "Your Daddy." # VA: Deliberate repetition to annoy Athena.
    a "Medusa..." # VA: Warning tone, running out of patience. Ready to snap.
    m "You're the one who sprang out of his forehead, not me." # VA: Matter-of-fact with playful bite.
    pause 2.0
    play sound "assets/sfx/athena_ugh.ogg"
    a "Okay. Forget I said anything." # VA: Defeated sigh. Athena knows she can't win this argument, and she doesn't want to waste her energy on it.
    m "Noted." # VA: Satisfied.
    a "So why did my..." # VA: Trying to restart the conversation.
    m "Daddy?" # VA: Quick teasing interruption.
    a "..." # VA: Silent frustration.
    a "Esteemed, divine father..." # VA: Forced rewording through gritted teeth.
    a "Forbid you from coming in?" # VA: Returning to the question.
    pause 2.0
    m "Guess." # VA: Coy challenge.
    play sound audio.athena_ugh_2
    m "Come on! Use that brainpower of yours." # VA: Teasing challenge. Medusa thinks Athena can just flip a switch and figure things out. 
    a "I don't know." # VA: Flat, annoyed admission.
    a "Because snakes and birds of prey don't mix?" # VA: Tentative reasoning.
    m "Exactly!" # VA: Bright, triumphant confirmation.
    a "So it wasn't out of pettiness then." # VA: Thoughtful reassessment.
    m "Your daddy's WAY too soft to be petty, Athena." # VA: Playful jab with emphasis on "WAY."
    a "..." # VA: Internal cringe beat.
    a "I'm going to pretend that didn't conjure up strange images of my father, Medusa." # VA: Disturbed, dry humor. Athena tries to remain formal. 
    pause 1.0
    show bg stairs with dissolve
    show medusa_neutral_left at Position(xalign=0.5) with dissolve
    show athena_robes_neutral at Position(xalign=0.3) with dissolve
    a "But I'm not sure why you'd think snakes and birds are going to mix now." # VA: Genuine concern, cautious.
    show medusa_happy_left at Position(xalign=0.5)
    m "Well, I thought if you were at my side..." # VA: Hesitant vulnerability.
    m "Maybe the owls wouldn't nitpick me to death." # VA: Dark humor masking anxiety.
    show athena_robes_happy at Position(xalign=0.3)
    play sound "assets/sfx/athena_giggle.ogg"
    a "That won't happen, Medusa." # VA: Protective reassurance. Like a Goddess looking after  her priestess.
    a "Not under my watch." # VA: Firm promise. 
    m "Promise?" # VA: Soft, seeking reassurance.
    a "Pinky promi-" # VA: Light playful start, before being cut short.
    art "Fetching new luncheon meat for the owls, I see." # VA: Smug tease.
    show athena_robes_surprised at Position(xalign=0.3)
    show medusa_surprised_left at Position(xalign=0.5)
    pause 1.0
    show artemis_neutral at Position(xalign=0.7) with dissolve
    art "Or not." # VA: Quick, playful pivot.
    art "Maybe a snake sandwich is on the menu today." # VA: Sweet tone, mean intent.
    play sound "assets/sfx/artemis_laugh.ogg"
    show medusa_angry_left at Position(xalign=0.5)
    show athena_robes_angry at Position(xalign=0.3)
    a "Ugh, Artemis. What do you want?" # VA: Immediate irritation. Athena and Artemis have a long history of rivalry, and Athena is not in the mood for it.
    art "I just wanted to say hi to my favourite keeper of furballs!" # VA: Fake cheerful, mocking.
    art "And handler of snakes!" # VA: Strong, cruel emphasis on "Snakes!"
    show artemis_laugh at Position(xalign=0.7)
    play sound "assets/sfx/artemis_laugh.ogg"
    show medusa_eyebrow_left at Position(xalign=0.5)
    m "Hmph." # VA: Dismissive snort.
    m "Still not over me trashing you in paintball, huh?" # VA: Smug provocation. She wants to snark back at Artemis.
    show artemis_angry at Position(xalign=0.7)
    show athena_robes_surprised at Position(xalign=0.3)
    a "You beat Artemis in paintball?" # VA: Genuinely surprised.
    play sound "assets/sfx/artemis_grunt.ogg"
    art "We all have our off days." # VA: Suddenly defensive, anger brimming underneath.
    show medusa_proud_left at Position(xalign=0.5)
    m "Sure did." # VA: Proud, smug confirmation.
    m "I've met town bicycles who took fewer shots to the head than Artemis did that day." # VA: Savage one-liner, delivered with a smirk.
    play sound "assets/sfx/artemis_angry.ogg"
    show artemis_furious at Position(xalign=0.7)
    art "WHY YOU LITTLE-" # VA: Full on Rage - not unlike Homer Simpson when he's about to strangle Bart.
    scene black with fade
    play sound "assets/sfx/artemis_scream.ogg"
    pause 2.0
    play sound "assets/sfx/artemis_cry.ogg"
    a "TO HADES WITH YOU!" # VA: Explosive battle shout.
    pause 1.0
    play sound audio.stairs_crash
    pause 1.0
    show cg athena_artemis_fight
    pause 2.0
    scene black with fade
    show bg stairs with fade
    show athena_robes_cringe at Position(xalign=0.3) with dissolve
    a "Ow." # VA: Short pain reaction.
    a "That's going to leave a mark." # VA: Wry, post-fight wince.
    show medusa_surprised at Position(xalign=0.7) with dissolve
    m "Wow, Athena. That was..." # VA: Awe building.
    show medusa_excited at Position(xalign=0.7) with dissolve
    m "AMAZING!" # VA: Full excited burst.
    show medusa_excited at Position(xalign=0.7) with dissolve
    show athena_robes_proud at Position(xalign=0.3)
    a "I know, right?" # VA: Proud, playful confidence.
    a "Osoto Gari is one of my signature moves." # VA: Confident, slightly showy. Athena, like fencing, is a judo fanatic.
    a "I learned it from Amaterasu, the goddess of the sun." # VA: Informative tone, prideful at the fact she learnt under the best.
    a "You remember her, right?" # VA: Casual question, checking Medusa's memory.
    m "Of course I do." # VA: Quick confirmation.
    m "She was the substitute PE professor for a while when..." # VA: Trail-off as her memory turns uncomfortable.
    pause 2.0
    show medusa_nervous at Position(xalign=0.7)
    a "...When Poseidon was on leave." # VA: Careful completion, reading Medusa's mood.
    m "Right, Professor Poseidon." # VA: Tight, uneasy tone.
    show athena_robes_concerned at Position(xalign=0.3)
    a "Are you alright?" # VA: Concerned and gentle.
    show medusa_neutral at Position(xalign=0.7)
    m "Yeah, I'm fine." # VA: Too quick, too defensive. The first time in the script where Medusa feels way out of character. 
    a "You sure? You look a little...lightheaded." # VA: Careful concern.
    m "Totally fine." # VA: Forced reassurance. 
    show medusa_happy at Position(xalign=0.7)
    m "Come on! Let's go see your furbabies!" # VA: Bright pivot to avoid the topic.
    show athena_robes_sigh at Position(xalign=0.3)
    play sound "assets/sfx/athena_sigh.ogg"
    a "You know, I've always hated that nickname." # VA: Dry exasperation.
    show medusa_confused at Position(xalign=0.7)
    m "What, 'furbabies'?" # VA: Innocent tease. Like Daddy, she doesn't care if this annoys Athena. 
    m "So you threw archery nerd down the stairs for that?" # VA: Mock-serious accusation.
    m "Not for me?" # VA: Playful pouting. Their friendship is moving fast. 
    show athena_robes_happy at Position(xalign=0.3)
    a "Yes. We're not quite there friendship-wise yet." # VA: Teasing honesty.
    a "But eventually you might do something dumb enough for me to protect you." # VA: Dry, affectionate sarcasm. Even Athena can be sarcastic at times. 
    show medusa_happy at Position(xalign=0.7)
    m "Glad to hear that." # VA: Warm, amused.
    play sound "assets/sfx/athena_giggle.ogg"
    a "Anyway, let's go see the owls." # VA: Light, forward-moving comment.
    scene black with fade
    play sound audio.footsteps
    pause 2.0
    return

label demo_owl:
    scene black
    play sound audio.footsteps
    scene bg owl_house_door with fade #
    show athena_robes_neutral at Position(xalign=0.3)
    show medusa_neutral at Position(xalign=0.5)
    m "I've never been in here before." # VA: Cautious wonder.
    play sound audio.keys_jingle
    a "I know." # VA: Neutral tone.
    a "You told me that like, ten thousand times already." # VA: Neutral, but with a hint of impatience.
    play sound audio.keys_jingle2
    show athena_robes_annoyed at Position(xalign=0.3)
    a "s?at?!" # VA: Frustrated swear at the jammed door.
    show medusa_confused at Position(xalign=0.5)
    m "Something wrong?" # VA: Concerned check-in.
    a "No, it's just..." # VA: Slightly embarrassed hesitation. Athena isn't used to asking for help - she's often the one who gives out help to others. 
    a "I need someone to help me open the door." # VA: Shy, awkward request. Help isn't something Athena is used to asking for, and she doesn't know how to do it.
    pause 2.0
    m "I wanted to shy away at first when I heard that." # Medusa begins to pull away. Beginning of internal monologue, conflicted.
    m "Not because I didn't want to help Athena." # VA: Internal monologue, conflicted. Her mind is beginning to race with worst-case scenarios.
    m "But because I was afraid of what might happen if I did." # VA: Internal monologue, anxious vulnerability. We start to see what Medusa's fears are.
    scene black with fade
    pause 2.0
    scene cg owl_house_door_medusa with dissolve
    m "I thought it might be a trap." # VA: Internal monologue, fearful.
    m "It had happened before." # VA: Internal monologue, bitter memory.
    m "I thought Athena would push me inside and lock me in there with the owls." # VA: Internal monologue, spiraling worst-case fear. She's catostrophizing hard.
    scene cg owl_house_door_artemis with fade
    m "And then Artemis would appear, and join in on the fun by laughing at me." # VA: Internal monologue, dread mixed with resentment.
    play audio "assets/sfx/artemis_laugh.ogg"
    m "That would be the end of me." # VA: Internal monologue, dramatic dread.
    m "Pecked to death by owls, hawks and whatever else was in here." # VA: Internal monologue, darkly vivid fear.
    m "All because I put my trust in Athena." # VA: Internal monologue, wounded caution.
    scene bg owl_house_door
    show athena_robes_angry at Position(xalign=0.3)
    show medusa_sad at Position(xalign=0.5)
    a "MEDUSA!" # VA: Sharp snap to break Medusa out of her sprialing mind.
    m "..." # VA: Blank beat, caught off-guard.
    show medusa_confused at Position(xalign=0.5)
    m "What?" # VA: Confused, defensive. She doens't know how much time she's spent spiraling in her own head. 
    show athena_robes_annoyed at Position(xalign=0.3)
    a "...The door?" # VA: Pointed reminder, trying to stay patient with her priestess.
    show medusa_nervous at Position(xalign=0.5)
    m "Oh, right." # VA: Sheepish, quick recovery.
    m "The door." # VA: Quick self-correction.
    show athena_robes_neutral at Position(xalign=0.3)
    a "Are you going to help me with it, or not?" # VA: Firm but not cruel. She can sense Medusa is zoning in and out. 
    show medusa_sad at Position(xalign=0.5)
    m "Well..." # VA: Hesitant. Uncertain.
    menu m_owl_door:
        "What do you choose?"
        "Help Athena open the door":
            $ friends += 1
            $ lovers += 1
            show cg medusa_helping_athena
            m "Many hands make light work, right?" # VA: Quick attempt at upbeat teamwork after a long period of internal monologue and spiraling.
            a "Yes, it does." # VA: Encouraging agreement.
            m "Alright, on three!" # VA: Rallying energy.
            m "One... Two... Three!" # VA: Count with effort and momentum and some slight comedic timing.
            scene black with fade
            play sound audio.door_open # ?
            play sound audio.footsteps
            pause 1.0
        "Refuse to help Athena":
            $ enemies += 1
            $ rivals += 1
            show cg medusa_refusing_athena
            m "I'm sure you can open it on your own, Athena." # VA: Polite refusal with distance.
            play sound "assets/sfx/athena_sigh.ogg"
            a "Alright, I'll do it myself then." # VA: Controlled disappointment. She isn't happy, but somewhat expecting this from Medusa.
            a "Remember though, this Goddess-Priestess relationship is a two-way street." # VA: Firm reminder of responsibility.
            scene black with fade
            play sound audio.door_open # ?
            play sound audio.footsteps
            pause 1.0
    play ambience audio.mews loop # ?
    show bg owl_house_interior with fade
    show medusa_happy at Position(xalign=0.7) with dissolve
    show athena_robes_happy at Position(xalign=0.3) with dissolve
    m "Wow..." # VA: Breathless awe.
    a "Welcome to the Owl House, Medusa!" # VA: Warm, inviting pride. This is a place Athena is proud of, and she wants to share it with her priestess.
    m "Athena, this place is amazing!" # VA: Genuine excitement.
    a "I know, right?" # VA: Pleased that Medusa sees how great it is.
    a "It's like my own little pond." # VA: Soft personal admission.
    show medusa_eyebrow at Position(xalign=0.7)
    m "Your own little pond?" # VA: Slightly curious. Beginning of a heartfelt conversation.
    pause 2.0
    show athena_robes_neutral at Position(xalign=0.3)
    a "Well, yeah..." # VA: Slightly shy opening up. # She isn't used to baring her soul like this to someone else.
    a "I come here at times..." # VA: Reflective, gentle.
    a "When everything is just too much for me to handle." # VA: Honest vulnerability.
    a "When I just want to be alone with my thoughts." # VA: Quiet and introspective. Not unlike Medusa with her pond. 
    a "And with my owls." # VA: Fond warmth. Not unlike Medusa with her snakes.
    show medusa_surprised at Position(xalign=0.7)
    m "Wait, all the owls here are yours?" # VA: Surprised curiosity, incredulous.
    pause 2.0
    show athena_robes_neutral at Position(xalign=0.3) # Athena's made a mistake. She doesn't make too many mistakes.
    a "No, just the one." # VA: Casual correction. Athena's made a mistake.
    a "The rest of them are just...offcuts the Moirai don't know what to do with yet." # VA: Matter-of-fact, but a little awkward admission. 
    show medusa_happy at Position(xalign=0.7)
    m "So, Pallas Athena has only one furbaby then?" # VA: Playful tease. She's good at getting under the skin of her Goddess. 
    show athena_robes_annoyed at Position(xalign=0.3)
    play sound "assets/sfx/athena_sigh.ogg"
    a "I hate that term." # VA: Dry annoyance.
    a "So very much." # VA: Dead serious emphasis.
    show athena_robes_neutral at Position(xalign=0.3)
    a "But yes, I only have the one." # VA: Resigned confirmation.
    show medusa_eyebrow at Position(xalign=0.7)
    m "I see." # VA: Taking it all in. A thoughtful pause, as she processes the information.
    pause 1.0
    show medusa_excited at Position(xalign=0.7)
    m "Can I see it?" # VA: Eager ask, quick pivot. 
    show athena_robes_annoyed at Position(xalign=0.3)
    a "...What?" # VA: Briefly thrown off by the question. She isn't used to people asking to see her owl.
    show medusa_excited at Position(xalign=0.7)
    m "Can I see Ms Athena's furbaby?" # VA: Deliberately teasing repeat, with an emphasis on "furbaby."
    show athena_robes_neutral at Position(xalign=0.3)
    a "Only to stop hearing you prattle on about furbabies like a schoolgirl with scabby knees." # VA: Dry comment, but not truly mean.
    show medusa_angry at Position(xalign=0.7)
    m "HEY!" # VA: Offended yelp.
    show athena_robes_blue_call_minerva at Position(xalign=0.3)
    a "MINERVA!" # VA: Loud call. Practiced thousands of times down the years. 
    scene black with fade
    pause 2.0
    show cg minerva_owl with fade
    m "Wow, it's so cute!" # VA: Childlike wonder.
    a "She, not it." # VA: Gentle correction. Athena doesn't like people referring to her owl as "it."
    m "Sorry..." # VA: Quick apology.
    m "SHE." # VA: Self-correction with emphasis.
    m "Is really cute!" # VA: Bright enthusiasm.
    a "Minerva is my owl." # VA: Soft pride.
    m "You named her after the Roman version of yourself?" # VA: Curious and lightly teasing. The first hint of how much the Gods know about us. 
    a "Well, I thought it was a fitting name for her." # VA: Modest, affectionate.
    a "She's my little Minerva, after all." # VA: Warm tenderness.
    m "I thought she would be white instead of brown." # VA: Innocent observation.
    a "Why? She's a barn owl, Medusa." # VA: Practical correction.
    m "I don't know, humans always draw you with a white owl." # VA: Casual explanation.
    m "But it makes sense that you'd have a brown one, since you've brown hair and all." # VA: Rambling logic, trying to be nice.
    pause 2.0
    a "I'm auburn, actually." # VA: Corrective but composed.
    m "What?" # VA: Confused reaction.
    a "My hair isn't brown, it's auburn." # VA: Patient clarification.
    m "Oh, right. Sorry about that." # VA: Sheepish apology.
    a "It's fine." # VA: Reassuring, no hard feelings.
    m "I'm just sorta colourblind." # VA: Honest confession.
    a "...I see." # VA: Soft, understanding beat.
    pause 2.0
    m "...Can I hold her?" # VA: Careful, hopeful ask.
    a "Sure, be careful though." # VA: Trusting but cautious.
    scene black with fade
    a "Here you go." # VA: Gentle handoff.
    play sound audio.ruffled_feathers
    m "Oh boy, she's heavy!" # VA: Surprised strain.
    a "Relax, she isn't going to bite." # VA: Calm reassurance.
    a "Yet." # VA: Dry joke.
    m "Yet?" # VA: Alarmed squeak.
    a "She only tried to nip my eyes out the first time I held her." # VA: Deadpan anecdote.
    m "That's not helping, you know." # VA: Nervous complaint.
    show cg medusa_holding_owl with fade
    m "Once it became clear to me that Minerva wasn't going to devour me, I relaxed a little bit." # Internal monologue
    m "I even let myself stare dreamily into her big, round eyes." # VA: Internal monologue, softened and tender.
    m "They were a grey colour." # VA: Internal monologue, lingering observation.
    m "The same as my..." # VA: Internal monologue, trailing realization.
    pause 2.0
    if lovers >= 2:
        m "Goddess." # VA: Reverent whisper.
        pause 2.0
        m "I wondered if the stories were true." # VA: Internal monologue, hushed curiosity.
        m "That Athena used Minerva to spy on others." # VA: Internal monologue, fascinated rumor recall.
        m "That she could see through Minerva's eyes and hear through her ears." # VA: Internal monologue, awe mixed with nerves.
        m "If they were, it meant I was staring into my goddess's eyes right now." # VA: Internal monologue, intimate realization.
        m "Something which, as my skin prickled with goosebumps, I didn't mind in the slightest." # VA: Internal monologue, breathy and entranced.
    elif enemies >= 2 or rivals >= 2:
        play sound audio.owl_squeaking
        m "Ugh." # VA: Irritated grunt.
        m "Keeper of furbabies." # VA: Snarky mutter.
        m "By the Goddesses, do these things squeak!" # VA: Exasperated complaint.
    else:
        m "Well, new friend." # VA: Internal monologue, tentative warmth.
        m "..." # VA: Internal pause, letting the word settle.
        m "Friend." # VA: Internal monologue, testing the word.
        m "It sounded strange when I described her like that." # VA: Internal monologue, surprised by her own feelings.
        m "I couldn't even recall the last time I had a friend." # VA: Internal monologue, lonely reflection.
        m "..." # VA: Internal pause, emotional beat.
        m "And yet, I wished I'd had one sooner." # VA: Internal monologue, soft regret.
        m "This new feeling within me was strange." # VA: Internal monologue, cautious wonder.
        m "And I didn't want to let it go." # VA: Internal monologue, quiet longing.
    stop ambience fadeout 0.5
    return

label demo_checkers:
    scene black
    play ambience audio.checkers loop
    m "So tell me, Athena." # VA: Curious ask.
    m "How does the round piece work again?" # VA: Trying to follow along, slightly sheepish.
    scene cg checkers_athena
    a "I was tired, but somehow I eked out a smile." ## Beginning of Athena's internal monologue. 
    a "Look, it's pretty simple." # VA: Patient teacher tone.
    a "Every piece does the same thing." # VA: Clear, instructional.
    a "You take one step and try to jump over the others to capture them." # VA: Practical explanation.
    a "That's the game in a nutshell." # VA: Summing up, confident.
    pause 2.0
    m "..." # VA: Concentration beat.
    m "It does sound easy when you put it like that." # VA: Cautiously optimistic.
    m "OKAY, LET ME TRY!" # VA: Sudden excited burst.
    a "I knew she was hopeless at games, but not this bad." # VA: Internal monologue, amused disbelief.
    a "I didn't even bother to look at the board, since I was already several steps ahead of her." # VA: Internal monologue, confident and teasing.
    scene cg_checkers_athena_look_up
    a "Instead, something else caught my eye." # VA: Internal monologue, attention shifting.
    scene cg_checkers_medusa
    a "She was concentrating." # VA: Internal monologue, observant.
    a "Or rather, the snakes were concentrating." # VA: Internal monologue, curious detail.
    a "I wasn't sure which one of them was in control." # VA: Internal monologue, bemused wonder.
    scene cg_checkers_athena_look_up
    a "I didn't even understand how serpentine hair worked." # VA: Internal monologue, fascinated confusion.
    a "Did each one have a strange, stifling mind of its own..." # VA: Internal monologue, speculative thought.
    a "Pulling Medusa in so many different directions in life?" # VA: Internal monologue, analytical and empathetic.
    a "Maybe it was why she couldn't sit still in class." # VA: Internal monologue, reflective theory.
    a "Or why, as my father had said, she'd started so many electives and never finished them." # VA: Internal monologue, piecing things together.
    a "Perhaps." # VA: Internal monologue, tentative conclusion.
    m "YOUR MOVE!" # VA: Loud interruption, snapping Athena back.
    show cg_checkers_athena_look_down
    a "Huh?" # VA: Startled break from thought.
    a "Oh, right. The game." # VA: Refocusing, slightly flustered.
    scene black with fade
    m "What the..." # VA: Shocked confusion.
    play sound "assets/sfx/athena_giggle.ogg"
    scene cg checkers_athena_win
    a "I win!" # VA: Triumphant burst.
    play sound "assets/sfx/medusa_grunt.ogg"
    m "Not fair." # VA: Sulky complaint.
    a "Athena 1, Medusa 0." # VA: Cheerful scorekeeping.
    scene black with fade
    pause 1.0
    stop ambience fadeout 0.5
    play sound audio.checkers_put_away
    return

label demo_end:
    scene black
    a "If we'd tried playing chess, I think your head might've exploded." # VA: Dry joke.
    a "Mine nearly did." # VA: Deadpan follow-up.
    pause 1.0
    show bg hallway with dissolve
    show athena_robes_neutral at Position(xalign=0.3) with dissolve
    show medusa_confused at Position(xalign=0.7) with dissolve
    m "I thought you were the campus champion in board games?" # VA: Genuine question.
    a "I am." # VA: Matter-of-fact confidence.
    show athena_robes_tired at Position(xalign=0.3)
    a "...Just not in chess." # VA: Reluctant admission.
    a "That's Professor Poseidon's domain." # VA: Respectful frustration.
    show medusa_nervous at Position(xalign=0.7)
    pause 1.0
    m "Oh." # VA: Small uneasy reaction.
    show athena_robes_concerned at Position(xalign=0.3)
    a "What?" # VA: Alert concern.
    show medusa_surprised at Position(xalign=0.7)
    m "Nothing." # VA: Immediate deflection.
    m "It's just..." # VA: Hesitant.
    a "Just what?" # VA: Gentle prompt.
    m "...I think it would be hard to play chess underwater, wouldn't you?" # VA: Awkward joke to dodge the real feeling.
    pause 1.0
    a "Poseidon does come up to campus to lecture in Marine studies, remember?" # VA: Patient clarification.
    m "Yeah, I know but..." # VA: Uneasy trail-off.
    pause 2.0
    a "Is there something wrong?" # VA: Concerned and direct.
    show medusa_dismissive at Position(xalign=0.7)
    m "No! Nothing wrong." # VA: Quick over-defensive denial.
    a "Are you sure?" # VA: Soft persistence.
    a "Every time you hear Poseidon's name, you get very-" # VA: Careful observation.
    show medusa_eyebrow at Position(xalign=0.7)
    m "It's just bizarre to know!" # VA: Forced brightness to mask discomfort.
    m "That even the golden girl on campus has her off days." # VA: Teasing deflection.
    pause 0.5
    show athena_robes_determined at Position(xalign=0.3)
    a "I don't have off days, Medusa." # VA: Competitive pride.
    a "Poseidon just has a head start-" # VA: Defensive correction.
    m "Your uncle." # VA: Playful interruption.
    pause 0.5
    show medusa_smirk at Position(xalign=0.7)
    show athena_robes_annoyed at Position(xalign=0.3)
    play sound "assets/sfx/athena_sigh.ogg"
    pause 1.0
    a "My uncle, who has a head start-" # VA: Reasserting control, irritated.
    m "I bet you're very happy I didn't call him your daddy." # VA: Smug tease.
    show athena_robes_angry at Position(xalign=0.3)
    a "MY UNCLE!" # VA: Full exasperated shout.
    a "..." # VA: Recovering breath.
    pause 0.5
    show athena_robes_neutral at Position(xalign=0.3)
    a "Just has a head start on me." # VA: Controlled reset.
    a "From centuries of practice." # VA: Rational, clipped.
    a "That's all." # VA: Final emphasis.
    pause 0.5
    show medusa_eyebrow at Position(xalign=0.7)
    m "I see." # VA: Light, unconvinced.
    pause 1.0
    m "I wonder if he sleeps with them, like he does with his fish." # VA: Mischievous rumor-baiting.
    show athena_robes_annoyed at Position(xalign=0.3)
    play sound "assets/sfx/athena_ugh.ogg"
    a "Please don't say that again." # VA: Immediate disgust.
    a "That's Artemis' domain." # VA: Dry reprimand.
    a "The rumour mill." # VA: Flat, weary.
    show medusa_happy at Position(xalign=0.7)
    m "Sorry, I just thought it was funny." # VA: Light apology, still amused.
    a "What I'm trying to say..." # VA: Gathering herself.
    a "Is that there's no substitute for persistence in life." # VA: Mentor tone, sincere.
    show athena_robes_determined at Position(xalign=0.3)
    a "I will defeat Poseidon in chess..." # VA: Determined vow.
    a "And so too will you graduate from Olympus University, Medusa." # VA: Firm encouragement.
    show medusa_neutral at Position(xalign=0.7)
    m "...I think what you're trying to say there, Athena..." # VA: Playful translation.
    m "Is that practice makes perfect, right?" # VA: Friendly simplification.
    pause 0.5
    show athena_robes_sigh at Position(xalign=0.3)
    a "Yes, that's right." # VA: Sheepish admission.
    a "Too obvious?" # VA: Self-aware, lightly embarrassed.
    m "Zeus gave me the same pep talk a billion times before." # VA: Dry, familiar frustration.
    play sound "assets/sfx/athena_sigh.ogg"
    a "Well, I thought it was worth a try." # VA: Good-natured concession.
    pause 1.0
    show athena_robes_neutral at Position(xalign=0.3)
    a "Same time tomorrow, then?" # VA: Hopeful invitation.
    a "You still have whole catalogues of board games to get through, after all." # VA: Light teasing structure.
    a "Scrabble. Snakes and Ladders. Dungeons and Dragons. Monopoly. Dominoes." # VA: Listing with playful momentum.
    m "The pizza place?" # VA: Deadpan misunderstanding.
    show athena_robes_sigh at Position(xalign=0.3)
    play sound "assets/sfx/athena_sigh.ogg"
    a "I'll pretend not to hear that." # VA: Sighing amusement.
    show medusa_sad at Position(xalign=0.7)
    m "...Hmm, alright." # VA: Soft agreement.
    show athena_robes_happy at Position(xalign=0.3)
    a "Great! I'll see you tomorrow, Medusa!" # VA: Bright and sincere.
    show medusa_happy at Position(xalign=0.7)
    m "See you tomorrow, Athena!" # VA: Warm return.
    scene black with fade
    pause 1.0
    a "It was a start." # VA: Reflective internal monologue.
    a "Medusa might never be a board game genius like me, but at least she was trying." # VA: Internal monologue, fond realism.
    a "She wanted to keep going on." # VA: Internal monologue, soft encouragement.
    a "She wanted to get better." # VA: Internal monologue, hopeful.
    a "And I was happy for that - at least for the time being." # VA: Internal monologue, cautious contentment.
    return

label demo_poseidon:
    scene black
    m "Athena had offered to walk me back to my dorm after our board game session." # VA: Internal monologue, reflective.
    m "But I'd said no." # VA: Internal monologue, firm but conflicted.
    m "We'd been paired up enough for the day, and I wanted to be alone." # VA: Internal monologue, guarded.
    m "Besides..." # VA: Internal monologue, hesitant pause.
    m "I didn't want her to wear out her welcome just yet." # VA: Internal monologue, self-protective.
    m "..." # VA: Quiet beat.
    play sound medusa_hallway_footsteps
    show bg cold_hallway with dissolve
    show medusa_sad at Position(xalign=0.3) with dissolve
    m "Just yet." # VA: Internal monologue, reaffirming distance.
    m "Athena had smiled at me when I said that." # VA: Internal monologue, surprised by her kindness.
    m "I thought it was harsh to say that now..." # VA: Internal monologue, guilty reflection.
    m "But she didn't mind." # VA: Internal monologue, softened.
    pause 1.0
    m "She was persistent with me." # VA: Internal monologue, reluctant admiration.
    m "I had to give her credit there." # VA: Internal monologue, honest concession.
    m "Besides her father, everyone else had given up on me." # VA: Internal monologue, hurt memory.
    m "Nobody else seemed to acknowledge me on campus..." # VA: Internal monologue, lonely bitterness.
    m "Well..." # VA: Internal monologue, tense lead-in.
    m "Except for the person I dreaded seeing most..." # VA: Internal monologue, rising dread.
    scene black with fade
    play sound medusa_hallway_footsteps
    pause 2.0
    show poseidon_neutral at Position(xalign=0.7)
    pause 2.0
    m "Poseidon." # VA: Internal monologue, heavy and cold.
    m "Professor Poseidon." # VA: Internal monologue, bitter formality.
    m "Campus legend. Sporting icon. Beloved by everyone." # VA: Internal monologue, resentful list.
    pause 2.0
    m "...And someone who I could never shake the feeling was an especially evil son of a bitch, underneath it all." # VA: Internal monologue, disgust and fear.
    m "What's worse, he had his eye on me." # VA: Internal monologue, dread.
    m "I knew that." # VA: Internal monologue, certainty.
    scene black with Fade(3.0)
    pause 1.0
    scene bg cold_hallway with dissolve
    show medusa_angry_left at Position(xalign=0.7)
    show poseidon_neutral at Position(xalign=0.3)
    m "Even while my back was turned, I felt him watching me." # VA: Internal monologue, paranoia grounded in fear.
    m "Like a bloated shark might do when sizing up its prey..." # VA: Internal monologue, vivid contempt.
    m "Wondering if an extra morsel was worth the stomach-ache." # VA: Internal monologue, dark metaphor.
    pause 1.0
    scene black with fade
    m "I hated that." # VA: Internal monologue, clenched anger.
    m "Hated feeling so weak." # VA: Internal monologue, self-directed frustration.
    m "Hated that someone could have so much power over my mind." # VA: Internal monologue, raw and shaken.
    m "Hated." # VA: Internal monologue, pounding emphasis.
    m "Hated." # VA: Internal monologue, repeated fury.
    m "Hated it." # VA: Internal monologue, final bitter release.
    show cg medusa_door with dissolve
    m "Even by the time I'd reached my room, I couldn't help but feel he was still watching me." # VA: Internal monologue, lingering fear.
    m "Still waiting." # VA: Internal monologue, quiet dread.
    m "Still pestering." # VA: Internal monologue, exhausted resentment.
    m "Ready for any chance to claw his dirty fingertips deep into my harsh, green skin." # VA: Internal monologue, visceral revulsion.
    scene black with fade
    pause 2.0
    return

label demo_credits:


label Chapter_2_Athena_Room:
        scene black
        play sound audio.athena_door_shut
        scene black with fade
        a "Ugh." # VA: Exhausted release.
        a "That was a long day." # VA: Tired summary.
        a "I don't know I managed to keep up with snake-" # She catches herself mid sentence.
        pause 1.0
        a "..." # VA: Quiet pause to gather herself.
        a "I don't know how I managed to keep up with Medusa." # VA: Overwhelmed reflection.
        a "She was challenging..." # VA: Honest, tired admission.
        a "And father expects me to do for the rest of the semester?" # VA: Disbelieving pressure.
        a "...I don't know if I can do it." # VA: Vulnerable doubt.
        a "..." # VA: Silent beat.
        a "..." # VA: Silent beat.
        a "..." # VA: Silent beat.
        a "Maybe I should move forward in life, instead of ruminating." # VA: Self-coaching resolve.
        a "Keep moving forward, and don't look back." # VA: Firm mantra.
        show bg athena_room with fade
        show athena_robes_angry at Position(xalign=0.3) with dissolve
        a "So, what can I do to kill Chronos before Chronos kills me?" # VA: Dark humor masking stress.
        menu athena_room:
            "What do you choose?"
            "Alone time with a Vibrator":
                $ lovers += 1
                $ rivals += 1
                show athena_robes_mouth_covered at Position(xalign=0.3)
                a "Maybe I should just take a break from all of this." # VA: Tentative self-indulgent thought.
                a "Alone time." # VA: Quietly decisive.
                a "With my favourite toy." # VA: Intimate, private confession.
                # show athena_robes_lust at Position(xalign=0.3)
                a "Maybe I should just take a break from all this." # VA: Reaffirming the choice.
                a "I " # VA: Cut-off thought, trailing into silence.
                scene black with fade
                play sound audio.athena_calendar_open
                scene cg athena_calendar with fade
                pause 2.0
                a "..." # VA: Wordless beat.
                a "..." # VA: Wordless beat.
                a "..." # VA: Wordless beat.
                a "..." # VA: Wordless beat.
                a "..." # VA: Wordless beat.
                a "..." # VA: Wordless beat.
        

