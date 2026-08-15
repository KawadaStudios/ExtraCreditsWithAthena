label demo_checkers:
    scene black_bg
    play ambience audio.checkers loop
    medusa "So tell me, Athena." # VA: Curious ask.
    medusa "How does the round piece work again?" # VA: Trying to follow along, slightly sheepish.
    scene checkers_athena_cg
    athena "I was tired, but somehow I eked out a smile." ## Beginning of Athena's internal monologue. 
    athena "Look, it's pretty simple." # VA: Patient teacher tone.
    athena "Every piece does the same thing." # VA: Clear, instructional.
    athena "You take one step and try to jump over the others to capture them." # VA: Practical explanation.
    athena "That's the game in a nutshell." # VA: Summing up, confident.
    pause 2.0
    medusa "..." # VA: Concentration beat.
    medusa "It does sound easy when you put it like that." # VA: Cautiously optimistic.
    medusa "OKAY, LET ME TRY!" # VA: Sudden excited burst.
    athena "I knew she was hopeless at games, but not this bad." # VA: Internal monologue, amused disbelief.
    athena "I didn't even bother to look at the board, since I was already several steps ahead of her." # VA: Internal monologue, confident and teasing.
    scene checkers_athena_look_up_cg
    athena "Instead, something else caught my eye." # VA: Internal monologue, attention shifting.
    scene checkers_medusa_cg
    athena "She was concentrating." # VA: Internal monologue, observant.
    athena "Or rather, the snakes were concentrating." # VA: Internal monologue, curious detail.
    athena "I wasn't sure which one of them was in control." # VA: Internal monologue, bemused wonder.
    scene checkers_athena_look_up_cg
    athena "I didn't even understand how serpentine hair worked." # VA: Internal monologue, fascinated confusion.
    athena "Did each one have a strange, stifling mind of its own..." # VA: Internal monologue, speculative thought.
    athena "Pulling Medusa in so many different directions in life?" # VA: Internal monologue, analytical and empathetic.
    athena "Maybe it was why she couldn't sit still in class." # VA: Internal monologue, reflective theory.
    athena "Or why, as my father had said, she'd started so many electives and never finished them." # VA: Internal monologue, piecing things together.
    athena "Perhaps." # VA: Internal monologue, tentative conclusion.
    medusa "YOUR MOVE!" # VA: Loud interruption, snapping Athena back.
    show checkers_athena_look_down_cg
    athena "Huh?" # VA: Startled break from thought.
    athena "Oh, right. The game." # VA: Refocusing, slightly flustered.
    scene black_bg with fade
    medusa "What the..." # VA: Shocked confusion.
    play sound audio.athena_giggle
    scene checkers_athena_win_cg
    athena "I win!" # VA: Triumphant burst.
    play sound audio.medusa_grunt
    medusa "Not fair." # VA: Sulky complaint.
    athena "Athena 1, Medusa 0." # VA: Cheerful scorekeeping.
    scene black_bg with fade
    pause 1.0
    stop ambience fadeout 0.5
    play sound audio.checkers_put_away
    return