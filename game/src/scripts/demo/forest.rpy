label demo_forest:
    scene black_bg
    play ambience audio.forest_ambience loop # ?
    pause 1.0
    medusa "This is my forest." # Beginning of Medusa's internal monologue.
    medusa "Well, technically Groundskeeper Pan's forest, but I like to think it's mine." # VA: Continued internal monologue. Possessive tone. She wants to think the forest is hers. 
    scene forest_bg
    with Dissolve(3.0)
    medusa "The place I hung out when I wanted to be alone." # VA: Continued internal monologue. Lonely, wistful. 
    medusa "The place I went when everything in life was too much for me to handle." # VA: Continued internal monologue. Lonely, wistful. The memories are painful. 
    medusa "Where I could just be myself and not have to worry about anything." # VA: Continued internal monologue. Deep down, she wished she wasn't by herself in those memories. 
    show medusa_pond_neutral at Position(xalign=0.7) with dissolve
    medusa "When I was really down in the dumps, I'd come here and sit inside this pond for hours." # VA: Continued internal monologue. She pretends that this wasn't painful as she speaks. 
    medusa "I couldn't get an entry into Pan's forest pool." # VA: Continued internal monologue. Frustrated tone. She wanted to be there. 
    medusa "The one where the nymphs acted as lifeguards." # VA: Continued internal monologue. Frustrated tone. She wanted to be there.
    medusa "And dryads and satyrs had impromptu volleyball matches." # VA: Continued internal monologue. Frustrated tone. She wanted to be there.
    medusa "Nobody wanted the gorgon troublemaker around them." # VA: 
    medusa "So I had to make due with my own." # VA: Continued internal monologue. The lonely, wistful tone returns. She wanted to be there, but she couldn't.
    pause 1.0
    show medusa_pond_sigh at Position(xalign=0.7)
    stop audio fadeout 0.5
    play audio "assets/sfx/medusa_sigh.ogg"
    pause 1.0
    medusa "Things could be a whole lot worse." # VA: Continued internal monologue. She tries to find a silver lining in her situation.
    medusa "I had this place to myself at least." # VA: Continued internal monologue.
    medusa "For now." # End of Medusa's internal monologue.
    pause 1.0
    play sound audio.athena_forest_footsteps_1 # ?
    show medusa_pond_surprised at Position(xalign=0.7)
    medusa "Huh, who's that?" # VA: Sudden alert. Nobody comes this far into the forest, so she is surprised to hear someone. 
    pause 1.0
    play sound audio.athena_forest_footsteps_2 # ?
    pause 1.0
    athena "Σκατά! I have stepped on centaur dung." # VA: Athena swears for the first time, albeit in Greek. Which shows how important the sandals are to her.
    athena "Pan is such an uncivilized brute!" # VA: Snapping, much unlike the gentle Athena we've seen so far. 
    athena "And those were my best sandals too!" # VA: Deeply upset, disgusted. Centaur dung is not something you want to step in, especially when you're wearing sandals.
    athena "Μαλάκα!" # VA: Athena swears again in Greek. She is really upset about stepping in the dung.
    play sound audio.athena_forest_footsteps_3 # ?
    pause 1.0
    show athena_robes_neutral at Position(xalign=0.3)
    athena "Medusa Margoyles?" # VA: Neutral tone. It happens so fast that Athena doesn't realise the mistake she's made.
    play sound audio.athena_gasp
    show athena_robes_mouth_covered at Position(xalign=0.3)
    play sound audio.medusa_ugh
    show medusa_pond_annoyed at Position(xalign=0.7)
    medusa "...That's my nickname on campus, dear player." # VA: Annoyed. She's used to being called that, but she doesn't like it.
    pause 1.0
    show medusa_pond_arm_raised at Position(xalign=0.7)
    medusa "HERE!" # VA: Dull chirp, like a student who's name has been called in class. 
    medusa "You called?" # VA: Neutral tone, like this meeting is the most mundane thing in the world.
    show athena_robes_neutral at Position(xalign=0.3)
    athena "I have." # VA: Neutral tone. Athena is trying to be polite, but she doesn't know how to approach Medusa.
    athena "I am Athena, daughter of Zeus and goddess of wis-" # VA: Neutral tone. Athena's often makes the mistake of lofty introductions, but she doesn't realise that Medusa is already aware of who she is.
    show medusa_pond_dismissive at Position(xalign=0.7)
    medusa "Blah, blah, blah. I know who you are." # VA: Dismissive, annoyed. Medusa just wants to get this over with as fast as possible. 
    show athena_robes_annoyed at Position(xalign=0.3)
    medusa "You're Athena. The golden girl on campus." # VA: Annoyed, matter-of-fact. Medusa is trying to get this over with as fast as possible.
    medusa "I know all that crap already." # VA: Rushing through, annoyed. 
    pause 2.0
    athena "...Well, I'm sure you already know this then, but I'm going to be your mentor for the next few months." # Neutral tone, but the irritation is starting to show. She tries to remain polite. 
    show medusa_pond_annoyed at Position(xalign=0.7)
    medusa "Goddess, you mean." # VA: Snarky, cut in.
    medusa "Let's not downplay it." # VA: To the point.
    medusa "At all." # VA: To the point.
    pause 2.0
    athena "...Correct. Goddess." # VA: Trying to remain calm, but the irritation is beginning to boil over.
    athena "And you are to be my priestess, Medusa." # VA: Trying to remain calm, but we're moments from disaster.
    menu m_priestess:
        "How do you respond?"

        "Keep your mouth shut and nod":
            show medusa_pond_sigh at Position(xalign=0.7)
            $ friends += 1
            $ rivals += 1
            medusa "Sure, I guess." # VA: Resigned, but still annoyed. She doesn't want to be here, but she has no choice.
            medusa "I mean, someone has to help me get through my final year of university, right?" # VA: Resigned acceptance, trying to sound practical.
            athena "Yes, that's right." # VA: Polite, but still trying to remain calm. The irritation from earlier is gone. 
            medusa "But I can't hack these tests or exams." # VA: Resigned, but Medusa can't her hide her frustration.
            medusa "At all." # VA: Still frustrated, but she can't help it.

        "Piss Athena off by being sarcastic":
            $ enemies += 1
            $ rivals += 1
            medusa "And you're doing all this to get those extra credits, right?" # VA: Sarcastic jab. Medusa pushes Athena's buttons to their limits.
            medusa "Finally ascend your way into Goddesshood?" # VA: Continued sarcasm, needling tone.
            medusa "And leave me and Olympus University in the dust, right?" # VA: Bitter and accusatory.
            medusa "Right?" # VA: Sharp insistence, forcing a response.
            show athena_robes_angry at Position(xalign=0.3)
            play sound audio.athena_angry
            show medusa_pond_scared at Position(xalign=0.7)
            athena "Yes, you caught me!" # VA: Angry, rapid fire vent. She isn't afraid to show it. 
            athena "I'm doing this all for the love of credits!" # VA: Angry, rapid fire vent.
            athena "And not because I want to learn how to look after someone who chooses to follow me!" # VA: Angry, rapid fire vent.
            athena "Which is what any goddess would do!" # VA: Angry, rapid fire vent.
            pause 2.0
            play sound audio.athena_sigh
            show athena_robes_tired at Position(xalign=0.3)
            athena "I didn't mean to snap like that." # VA: Regretful, apologetic.
            athena "That was...terribly out of character for me." # VA: Regretful, apologetic. Totally out of character for Athena. 
            pause 2.0
            show medusa_pond_happy at Position(xalign=0.7)
            medusa "It's okay, I get it." # VA: Happy, understanding. Medusa is trying to be understanding of Athena's outburst.
            medusa "It just happens when you're around poor old Medusa." # VA: Happy, understanding, slight self-depracting humor. Emphasis onike "Poor Old Medusa."
            medusa "The perennial senior who can't get her act together." # VA: Medusa's aware of how much of a mess she is, and she's trying to make light of it.
            medusa "Who can't even graduate from university." # VA: Continuation of that.. 

    pause 2.0
    show athena_robes_determined at Position(xalign=0.3)
    athena "You just need to study more, Medusa." # VA: Neutral tone, like this is a simple solution.
    athena "I didn't get everything right on my first go, either." # VA: Reassuring and sincere. Athena tries to normalize struggle.
    show medusa_pond_sad at Position(xalign=0.7)
    medusa "But these tests haven't been my first go in years now!" # VA: Exasperated sound. She's heard this countless times. 
    athena "I know. That's why I'm here." # VA: Determined. She really wants to help Medusa, and she wants to make sure she succeeds.
    athena "To make sure they're your last." # VA: Determined. She really wants to help Medusa, and she wants to make sure she succeeds.
    pause 2.0
    show medusa_pond_sigh at Position(xalign=0.7)
    medusa "I thought I should snap back." # VA: Beginning of Medusa's internal monologue. She's trying to find a silver lining in this arrangement.
    medusa "We'd had a bit of a rough start, but I felt at least we'd come to an understanding." # VA: Reflective internal monologue, cautiously hopeful.
    medusa "She wanted to help me, and I wanted to be helped." # VA: Soft, honest realisation.
    medusa "She wanted to cross the finish line, and get her degree." # VA: Thoughtful, connecting their goals.
    medusa "...And so did I, deep down." # VA: Quiet admission, even if she won't admit this to Athena or in public yet.
    pause 2.0
    medusa "...Does this mean I'm going to have to go through my Greek conjugations right now?" # VA: Nervous dread with a comedic edge.
    medusa "Anything but that, I thought." # VA: Internal groan, dramatic despair. She hates her Greek. 
    show athena_robes_happy at Position(xalign=0.3)
    athena "No, not yet." # VA: Reassuring calm.
    athena "Instead, we'll do something you'd like to do." # VA: Warm, deliberate kindness. Athena's true nature shines through here, and Medusa is touched by it.
    show medusa_pond_eyebrow at Position(xalign=0.7)
    medusa "Something I like to do?" # VA: Surprised, almost disbelieving.
    pause 2.0
    medusa "It was the first time anyone had ever asked me what I wanted to do." # VA: Internal monologue, stunned, reflective.
    medusa "The first time, like ever." # VA: Quiet emphasis, still processing it.
    pause 2.0
    athena "Yes. Think of something and we'll do it together." # VA: Patient, encouraging.
    show medusa_pond_eyebrow at Position(xalign=0.7)
    pause 2.0
    medusa "Well..." # VA: Hesitant, thinking out loud.
    medusa "How about..." # VA: Hesistant mumbling.
    menu m_athena_activity:
        "What do you choose?"

        "The Owl House":
            $ friends += 1
            $ rivals += 1
            medusa "How about The Owl House?" # VA: Careful ask, hopeful underneath.
            show athena_robes_thinking at Position(xalign=0.3)
            athena "The Owl House?" # VA: Clarifying repeat, curious.
            medusa "Yeah, the Owl House." # VA: Simple confirmation.
            pause 1.0
            play sound audio.athena_lightbulb # ?
            show athena_robes_lightbulb at Position(xalign=0.3)
            pause 2.0
            show athena_robes_happy at Position(xalign=0.3)
            athena "Oh. You mean the mews!" # VA: Lightbulb moment, upbeat correction.
            show medusa_pond_annoyed at Position(xalign=0.7)
            medusa "Everyone just calls it the Owl House, Athena." # VA: Mildly annoyed correction.
            pause 2.0
            show medusa_pond_sad at Position(xalign=0.7)
            medusa "But I've never been." # VA: Softer tone, hint of embarrassment.
            show athena_robes_neutral at Position(xalign=0.3)
            athena "Why not?" # VA: Gentle curious probe.
            pause 2.0
            medusa "...Snakes and birds of prey don't usually mix." # VA: Uneasy honesty. This doesn't come naturally to Medusa, but she wants to be honest with Athena.
            medusa "But if you're there, I might feel safe." # VA: Trusting, vulnerable. This is the beginning of their bond.
            show athena_robes_happy at Position(xalign=0.3)
            athena "I am the head of it, I suppose." # VA: Modest pride.
            athena "Alongside a billion other clubs on campus." # VA: Dry, self-aware humor.
            show athena_robes_determined at Position(xalign=0.3)
            athena "Very well. I'll show you the Mews." # VA: Decisive and reassuring.
            show medusa_pond_annoyed at Position(xalign=0.7)
            medusa "...The Owl House." # VA: Insistent, slightly irked correction.
            athena "Yes, Owl House!" # VA: Quick, confident concession.
            athena "...Just get dressed, would you?" # VA: Practical, slightly flustered.
            medusa "Alright." # VA: Agreeable, easy.
            scene black_bg with Dissolve(3.0)
            pause 1.0
        "Get into the pond with me":
            $ friends += 1
            $ lovers += 1
            show medusa_pond_happy at Position(xalign=0.7)
            medusa "Why don't you come in here with me?" # VA: Playful invitation. Medusa knows what she's doing, and she wants to see how Athena reacts.
            athena "What?" # VA: Sudden surprise.
            medusa "I'm serious. Get in." # VA: Bold challenge. She really wants to see how far Athena will go.
            athena "...But I don't have my swimming gear with me." # VA: Flustered objection. 
            medusa "So? I'm not wearing mine either." # VA: Casual confidence. She really wants to see Athena get in the pond with her.
            show athena_robes_red at Position(xalign=0.3)
            medusa "For a moment, I felt her cheeks flush." # VA: Internal monologue, observant and amused.
            medusa "She was embarrassed about stripping down in front of me." # VA: Continued internal monologue, teasingly curious.
            medusa "I didn't think she was used to it." # VA: Continued internal monologue, thoughtful.
            medusa "Even in front of other women." # VA: Continued internal monologue, quietly surprised.
            pause 2.0
            medusa "C'mon, for the day that's in it." # VA: Warm coaxing.
            athena "..." # VA: Silent beat. Athena weighs it up.
            show athena_robes_neutral at Position(xalign=0.3)
            athena "Hmph, alright." # VA: Reluctant acceptance. She's still a little embarrassed, but she wants to make Medusa happy.
            athena "I did say something that you'd like to do." # VA: Principled follow-through. The Athena way.
            medusa "Yup." # VA: Satisfied little nod in her voice.
            medusa "Now get in." # VA: Playful command. Not unlike an officer telling a recruit to jump into the water.
            show athena_bra_neutral at Position(xalign=0.3)
            show medusa_pond_blush at Position(xalign=0.7)
            medusa "Oh my." # VA: Flustered admiration.
            show athena_bra_happy at Position(xalign=0.3)
            athena "What?" # VA: Curious, slightly wary.
            medusa "Nothing." # VA: Trying to play it off.
            medusa "It's just..." # VA: Hesitant, searching for words.
            athena "Just...?" # VA: Prompting, impatiently curious. Athena wants to know what Medusa is thinking.
            pause 2.0
            show medusa_pond_happy at Position(xalign=0.7)
            medusa "Redheads shouldn't wear red, you know." # VA: Unsubtle critique.
            show athena_bra_annoyed at Position(xalign=0.3)
            athena "Ugh." # VA: Annoyed groan.
            show medusa_pond_annoyed at Position(xalign=0.7)
            medusa "Just get your butt in here, golden girl!" # VA: Playful taunt. 
            pause 2.0
            scene black_bg with fade
            play sound audio.athena_pond_footsteps # ?
            scene athena_medusa_pond_cg with Dissolve(2.0)
            play ambience audio.pond loop # ?
            medusa "See?" # VA: Triumphant little nudge.
            medusa "Not so bad now, is it?" # VA: Gentle teasing, warm.
            athena "..." # VA: Quiet beat. She softens.
            athena "I guess not." # VA: Reluctant but genuine concession.
            scene black_bg with fade
            pause 1.0
    medusa "So tell me." # VA: Curious, impatient reset.
    medusa "How does this Goddess and Priestess thing work again?" # VA: Earnest question, trying to understand the arrangement.
    stop ambience fadeout 0.5
    return
