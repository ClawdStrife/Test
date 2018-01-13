# The script of the game goes in this file.
############################
#SCRIPTS
############################


############################
#STRUCTURAL IMAGES
############################

############################
#BACKGROUNDS
############################
image bg airport exit ='bg_airport.jpg'
image bg office main ='bg_office.png'
image bg office desk = 'bg_desk.jpg'

##STRUCTURAL BACKGROUNDS
image bg dark month = 'bg_month.png'

############################
#CHARACTER SPRITES
############################
##MC
image side mc general= im.Scale("side_default.png", 360, 400) #Enter specific numbers <--
#image mc big = "side_default.png"
#image side mc default= "side_default.png"
image side mc blush= im.Scale("side_blush.png", 360, 400)
image side mc awkward= im.Scale("side_awkward.png", 360, 400)
image side mc angry= im.Scale("side_angry.png", 360, 400)
image side mc determined= im.Scale("side_determined.png", 360, 400)
image side mc happy_blush= im.Scale("side_happy_blush.png", 360, 400)
image side mc happy= im.Scale("side_happy.png", 360, 400)
image side mc miserable= im.Scale("side_miserable.png", 360, 400)
image side mc naughty_thoughts= im.Scale("side_naughty_thoughts.png", 360, 400)
image side mc pensive= im.Scale("side_pensive.png", 360, 400)
image side mc sad= im.Scale("side_sad.png", 360, 400)
image side mc smile= im.Scale("side_smile.png", 360, 400)
image side mc surprise_blush= im.Scale("side_surprise_blush.png", 360, 400)
image side mc surprise= im.Scale("side_surprise.png", 360, 400)
image side mc wink= im.Scale("side_wink.png", 360, 400)
##ALANDRA
image alandra normal =im.FactorScale("al.png",0.29)
##MARCOS
image marcos normal =im.FactorScale("marco.png",0.27)
image marcos super_happy = im.FactorScale("marco_super_happy_glasses.png",0.27)
image marcos smirk = im.FactorScale("marco_smirk_glasses.png",0.27)
image marcos sad =im.FactorScale("marco_sad_glasses.png",0.27)
image marcos happy_no_g =im.FactorScale("marco_happy.png",0.27)
image marcos happy = im.FactorScale("marco_happy_glasses.png",0.27)
image marcos cheeky_no_g = im.FactorScale("marco_cheeky.png",0.27)
image marcos cheeky = im.FactorScale("marco_cheeky_glasses.png",0.27)
image marcos angry = im.FactorScale("marco_angry_glasses.png",0.27)
##VINCENT
image vincent normal =im.FactorScale("vincent.png",0.26)
image vincent normal2 =im.FactorScale("vincent2.png",0.26)
image vincent cheeky =im.FactorScale("vincent_cheeky.png",0.26)
image vincent smile =im.FactorScale("vincent_smile.png",0.26)
image vincent smirk =im.FactorScale("vincent_smirk.png",0.26)
##LUCAS
image lucas normal =im.FactorScale("lucas_basic_pose2.png",0.25)
image lucas hand_up =im.FactorScale("lucas_basic_pose1.png",0.25)

# Declare characters used by this game. The color argument colorizes the
# name of the character.
############################
#CHARACTER DEFINITION
############################
##STRUCTURAL CHARACTERS
define n = Character(None, kind=nvl, color="#ff0000")
define narrator = Character(None,
#what_size=44,
#what_outlines=[(3, "#0008", 2, 2), (3, "#282", 0, 0)],
what_xalign=0.5,
what_yalign = 0.3,
#what_text_align=0.5,
#window_background=None,
window_background="textbox_plain.png",
#window_yminimum=0,
#window_xfill=False,
#window_xalign=0.5
)
define d = Character("director", color="#ff008f", window_background="textbox_original.png")
define u = Character("???")

##MC
define mc = Character ("[name]",
                        image="mc",
                        window_left_padding=100
                        )
##ROMANCE CHARACTERS
define a = Character ("Alandra")
define v = Character ("Vincent")
define l = Character ("Lucas", #window_background="textbox_original.png"
                     )
define m = Character ("Marcos")
##SECONDARY CHARACTERS
define b = Character("Boss")
define g = Character("Gérard")
define v = Character("Valentina")
define j = Character("Juan")

#################################################
# The game starts here.
#################################################

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    #scene bg office desk with dissolve
    #scene bg airport exit
    #show bg office main

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show alandra normal #at Position(xalign=.5, yalign =0.0) with moveinright
    # a "testing character sprites"
    # "alandra"
    #l "lucas"
    # show lucas normal at right
    # "this is lucas, the shirtless" #, all hail his shiny nipples"
    # show lucas hand_up
    # "say bye to lucas"
    # #hide lucas
    # "and now say hello to Marcos"
    # show marcos normal at left
    # "normal"
    # show marcos super_happy
    # "super happy"
    # show marcos smirk
    # "smirk"
    # show marcos sad
    # "sad"
    # show marcos happy_no_g
    # "happy without glasses"
    # show marcos happy
    # "happy"
    # show marcos cheeky_no_g
    # "cheeky without glasses"
    # show marcos cheeky
    # "cheeky"
    # show marcos angry
    # "angry"
    # "say bye"
    # hide marcos
    # "and say hi to vincent"
    # show vincent normal
    # "make it rain, dude"
    # show vincent normal2
    # "right on"
    # show vincent cheeky
    # "cheeky"
    # show vincent smile
    # "smile"
    # show vincent smirk
    # "smirk"

    # These display lines of dialogue.
    menu:
        "Would you like to skip the Contract?"
        "Yes":
            jump user_character
        "No":
            n "This contract is the agreement to employ the Groot Mediation Company on behalf of UniAid, The Sweet Fruit Company, and the city hall of Macondo."
            n "Two years ago, The Sweet Fruit Company approached Macondo with the interest of purchasing farm land."
            n "This land is owned by Macondo, however it is leased out to locals with the purpose to farm crops to feed their families and provide them with an extra income."
            n "For six months, the city hall of Macondo debated whether to sell the land or not."
            n "During the debate, UniAid has spoken openly about the concerns of the lost source of income for the locals and the introduction of non local crops."
            nvl clear
            n "The city hall of Macondo voted to sell the land, with the agreement that The Sweet Fruit Company must hire the current leaseholders."
            n "After a year and half, the three parties above have requested to hire a natural facilitator due to unsuccessful attempts to an agreement."
            n "You will be working on behalf of the Groot Mediation Company due to having no association with any of the parties while having 3 years of experience working as a neutral facilitator for smaller but similar cases."
            nvl clear
            n "When you arrive in Macondo, your job requirements will be:"
            n "- To attend and run all meetings in a neutral location."
            n "- To allow all parties to speak equally."
            n "- To document what has been agreed and what needs to be further discussed."
            n "- Keep all parties calm and professional."
            nvl clear
            jump user_character

    label user_character:
    n "By signing this agreement, you agree to the tasks above and will continue to stay neutral throughout the entire session."
    nvl clear
    #Use player's name, otherwise use the name 'Mia Caroline' -Right now MC due to text box length concerns
    $name = str((renpy.input("Signature:", exclude='{1234567890[]!#%\/-_=&?!}', length=8)).strip()) or "M.C."

    # visual tests
    # mc general "test general face and name"
    # mc blush "test blush"
    # mc awkward "test awkward"
    # mc angry "test angry"
    # mc determined "test determined"
    # mc happy_blush "test happy blush"
    # mc happy "test happy"
    # mc miserable "test miserable"
    # mc naughty_thoughts "test naughty thoughts"
    # mc pensive "test pensive"
    # mc sad "test sad"
    # mc smile "test smile"
    # mc surprise_blush "test surprise blush"
    # mc surprise "test surprise"
    # mc wink "test wink"
    #
    # d "((ARRIVAL))"
    #
    # n "Explains MC background."

    scene bg airport exit
    with Dissolve(.5)
    pause .5

    mc happy "I can’t believe I made it!"
    mc happy "The plane ride took forever but I’m finally on the ground again."
    #"The local airport where my final plane landed is quite small. There are a handful of small aircrafts by a single hangar."
    "I walk out of the airplane, and the hot and humid jungle air immediately assaults my skin."
    #"The airport looks like an airport in name only. It looks more like a large colonial one-story home than an airport."
    "Inside the airport it looks very modern with a lot of security cameras everywhere, and guards belonging to border security look busy patrolling the customs area."
    "Shockingly, the guards look very young, but have the serious look of older men, and with their unconcealed weapons, they give off a threatening vibe."
    "Even though they are supposed to protect me, it’s a scary image, and reminds me of the fact that this place is more dangerous than I am used to. I have to watch my back."
    mc pensive "It’s hard to believe that a month ago I didn’t know what to do with my life, and now I’ve ended up in an entirely different world."

    scene bg dark month
    with Dissolve(.5)
    pause 0.8

    scene bg office desk with Dissolve(.5)
    pause .5

    b "[name!q], are you paying attention?"
    mc sad "Yes, sir, you were discussing the new project in {b}Macondo{/b}."
    #boss annoyed expression
    b "We discussed that project ten minutes ago."
    mc "..."
    b "*sigh* Go get yourself a cup of coffee and meet me in my office in ten minutes."
    #Boss’s office (basic brown desk with some maps of the world in the background, with some red markers on it signifying where they are running projects).
    #Boss friendly expression
    b "So, you want to tell me what has been going with you lately?"
    b "You are completely out of it, while you are usually so sharp."
    mc "I am so sorry sir, I promise it won’t happen again."
    b "You know I care about my employees, but these projects require everyone’s full cooperation, or we will never make a change in the world."
    mc "I know, I am sorry."
    mc miserable "I am just going through some personal stuff, but I promise I won’t let it affect my work."
    #boss determined
    b "I am glad to hear it, but know that if you want to talk about it, you can always step into my office."
    mc awkward "Thank you, sir."
    b "Your work – up until last week – is excellent."
    b "You have the highest success rate of all the employees when it comes to negotiations between two parties."
    mc surprise_blush "Really? I didn’t know."
    mc surprise "Michael is also a really good employee, so I expected his success rate to be better than mine."
    b "Michael? He is good, but he doesn’t have your drive and intuition."
    b "*sigh* I was hoping I could have you lead the project in Macondo."
    b "There is a delicate situation currently unfolding over there, and I need my best employee."
    b "However, if you aren’t feeling up to it I completely understand, and I will have Michael go instead."
    mc "Me? I would love to go!"
    mc determined "Actually, going away for a while is just what I need right now."
    mc "I promise I won’t let you down!"

    #this scene needs to switch to a bagage reclaiming area
    show bg airport exit
    with Fade(0.5, 0.3, 0.5, color="#000")

    mc smile "This change of scenery really is what I need right now."
    mc "Let’s see if I can find my luggage."
    mc happy "Found it!"
    mc smile "Great, now all I need to do is exit this area and find the man who is supposed to pick me up and bring me to Macondo."

    #Standing in the arrivals lounge
    mc pensive "What was his name again? Something with an G…"
    "Suddenly a young boy of five starts crying as he had fallen on the ground and scratched his knee."
    #Image of mother carrying all the luggage and a 2 year old toddler in her arms, at a loss for what to do.
    mc "Hey little guy, did you fall down?"
    "The teary eyed boy looks at me with his eyes and mouth open wide in an expression between awe and horror."

     #choices tutorial***

menu:
    "(What should I do?)"
    "Offer a hand to the boy.":
        "The little boy ignores my hand and tries getting up by himself, before falling back down and continuing to cry."
        mc surprise "Oops!"
        jump choice1_done
    "Try to pick the boy up off the ground.":
        "The boy backs away from me and starts crying hysterically."
        mc sad "I should not have tried that..."
        jump choice1_done
    "Take out a Band-Aid and offer it to the boy.":
        "The little boy looks at the Band-Aid in my hand and nods."
        mc happy "There you go, all done!"
        jump choice1_done_success

label choice1_done:
    "Before I can continue calming the child down, the boy’s mother rushes to him and starts scolding him."
    mc awkward "Sorry, I think I upset him. I was trying to help. Is he okay?"
    "The child’s mother realizes that I am addressing her. Her eyes widen and the color leaves her face. She hastily drags her crying child away, looking horrified."
label choice1_done_success:
    "Out of nowhere, messy black hair with grey wings at the temples appears, and a figure starts running towards me. The strong smell of black coffee overwhelms me."
    u "Hey! [name!q]! I finally found you!"
    mc surprise "Uhm, are you the man who is supposed to pick me up?"
    g "Yup! My name is Gérard, nice to meet you!"
    "Gérard rushes after the mother and her children and starts conversing with her in Spanish. The woman says something in a frightened tone to Gérard, shoots me a panicked look and hurries off."
    "As Gérard walks back to my side, I suddenly take notice of his appearance. He is of a medium height, with calculating but kind, brown, eyes set in a tanned face."
    "He holds out his hand, and as I shake it I feel the thick calluses that mark him as a hard-working man."
    mc general "So I am guessing you saw what happened earlier?"
    #Gerard apologetic
    g "Yes, I did. Sorry for the rude interruption to our introduction, but I wanted to make sure Camelia knows you are not a threat."
    mc surprise "Why would she think I am a threat?"
    mc general "Is the situation in the town really that serious?"
    #Gerard confused
    g "I thought you had been told about what has been going on."
    mc "I have, but I didn’t think my appearance here would cause people to get this scared."
    #Gerard apologetic
    g "Yeah, I’m sorry about her, it’s been a difficult time for the town lately… But we can talk more about that later."
    g "For now, let’s drive you to the town and get you settled in!"
    mc determined "Right, let’s go!"
#
#     d "Exploring the town"
#
#Scene 2: In the car with Gérard, driving towards Macondo over the highway..
    scene bg room with Dissolve(.5)

    "I get in the car with Gérard, who quickly drives out of the airport parking lot and onto the highway."
    mc general "So, Gérard huh? That is a very unusual name for this part of South America. Are you not from around here?"
    g "Actually, I was born and raised here."
    g "Been here my whole life in Macondo, I have. My mother was actually from France, though"
    g "She fell in love with my dad, who lived in Macondo, so she stayed."
    g "but I guess she couldn't forget about her home. She named me after her favorite French actor."
    mc "How interesting! So can you speak French?"
    g "Yes! My mother spoke to me only in French for the first ten years of my life, to make sure I would speak both Spanish and French at a native level."
    #comment: I think Gerard's English is too fancy. We need to dumb it down if the next statement is going to be true. Also Gerard is probably considered a sage, since people in these kinds of towns has hardly gone to the next town over, let alone know a different language and he speaks three!
    g "English I learned later on in life so I don’t speak it as well as the other languages."
    mc "You only have a slight accent. It’s very impressive!"
    #gerard smiles
    g "Thanks!"
    "His smile warms my heart, and the dread that had settled since the encounter with Camelia at the airport, begins to subside."
    g "So, you are going to be the {b}facilitator{/b} in the town between the {b}town hall{/b} and the {b}Sweet Fruit Company{/b}, right?"
    g "What made you decide to go into this line of work?"

menu:
    "(Why am I here?)"
    "I always liked guiding and helping friends":
        mc smile "Well, I always liked guiding and helping friends solve their problems. A facilitator does just that, just on a larger scale."
        mc "I always wanted to work in a job that would allow me to make a difference in the world."
        mc "Ideally, I would like to help shape this world so that it can become sustainable, to preserve it for future generations."
        mc "So working as a facilitator can allow me to improve relations between two parties in order to resolve a problem"
        mc "If left unresolved or is resolved in a less than ideal manner, could have severe consequences for the planet."
        #Gerard smiling
        g "You sound very honorable! I wish kids these days were more like you"
        mc happy "That’s so sweet of you to say!"
        jump choice2_done
    "I didn’t know what else to do":
        mc general "I just kind of fell into this line of work because I didn’t know what else to do at the time."
        mc "For the longest time I didn’t know what to do with my life, so I first worked at a bar for a while."
        mc "I met my now-ex-boyfriend there, and eventually he found me this career opportunity."
        mc "I don’t know if I would have chosen to be a facilitator without a push from him, but even though we broke up, I still don’t regret this career choice."
        g "I can understand that. It’s tough to make a career choice when you are young."
        g "As long as you are happy with where you ended up, it doesn’t matter how you got into it in the first place."
        mc smile "Exactly! I’m glad you get it."
        jump choice2_done
    "This line of work looks great on a resume":
        mc general "I heard from a man at a local workshop that this line of work looks great on a resume."
        mc "Although I enjoy being a facilitator, it is not something I want to do for the rest of my life."
        mc "I really want to help make the world a better place, but I feel that I need a bigger income if I want to actually make an impact."
        #comment: wait, is Gerard part of one of these organizations? Then you can skip the comment about the language, but then we need to take away his humility about speaking English, because that level of English is seriously too fancy for a townsfolk
        g "I don’t agree with that. You don’t need money to make a difference."
        g "Money only corrupts people. Even if I earned nothing I would still try to help people."
        mc "That’s very honorable, but it’s not small changes I am after."
        mc "I feel that making a huge difference that can impact future generations can only be achieved by having a lot of money."
        g "Perhaps, but even small waves will move the ocean."

label choice2_done:
    "We continue driving along the highway for another hour. Eventually Gérard takes the exit towards Macondo."
    #comment: this is beautiful
    "As we drive, the holes in the concrete road become more numerous, making for one bumpy ride."
    "Eventually, the road morphs into a small, dirt road with various tropical plants creeping up from the sides, trying to reclaim their territory."
    "The lush green of the forest seems separate from us in the car, until, inevitably, the foliage covering the road thickens until almost no light remains from above the canopy."
    "Finally, we enter a small town and Gérard stops the car at the only hotel, and my home in the coming weeks."

    #This is a good place to skip forward to when you start the game

    #Scene info: hotel in the background, next to a road or parking lot.
    g "We’re here! Let me help you with your bags while you go check in."
    mc awkward "Thanks! That would be a great help."

    #Scene info: Lobby with a comfortable red couch in a corner with a coffee table. Next to a large fan. On the other side of the room is a desk where people check in and check out.
    u "Welcome to the {b}Green Grass Inn{/b}!"
    #it would be nice to have a description here
    v "My name is Valentina Rojas. I run this inn with my husband, Felipe Rojas. How may I help you?"
    mc general "Hi, I would like to check in if that’s alright."
    v "Of course, you are the new visitor! [name!q] right? Your room is all ready for you. Did you have a pleasant journey?"
    #Comment: wait, he works for the hotel too? I'm so confused
    mc "Yes, Gérard was very helpful. Could you let me know what time is breakfast going to be at?"
    v "You can have breakfast between 07:00 and 09:00 here on the first floor."
    v "Here is the key to your room. You will be staying in room 205 on the second floor. We hope you enjoy your stay!"
    mc smile "Thank you!"
    "As I start walking towards the staircase to make my way to the room, Gérard puts a hand on my shoulder and stops me."
    g "The hotel is run by a very nice family, but they don’t exactly have all of the necessities that a hotel should have, so you may need to buy some items."
    g "But if you have everything you need, perhaps you should explore the town a little."
    g "Everything can be reached by foot, but if you’re tired, the hotel can lend you a bike."
    g " There’s not much time left before the end of the day so choose carefully which place you want to visit."

menu:
    "(Where should I go?)"
    "General Store":
        "I couldn’t bring my toothpaste and shampoo, so I should pick some up now."
        jump day1_general_store
    "Town Hall":
        "This is where the meeting will take place tomorrow, so I want to get a feel of the place."
        jump day1_town_hall
    "Church":
        "The priest would be able to tell me a little bit more about the conflict in the town."
        jump day1_church
    "Bar":
        "I need to relax and unwind a little. A drink will do me some good."
        jump day1_bar
    "Market":
        "I would love to see the local produce they sell here. It’s also good to get a feel for the locals."
        jump day1_market
    "Hotel":
        "I’m exhausted, I’m going to read my book on the comfy red couch in the lobby."
        jump day1_hotel

label day1_general_store:
    #Scene info: inside of a convenience store, a few aisles may be in view with some shampoos and soaps.
    "Wow! They have more choices of toothpaste and shampoo than I expected."
    "As I browse the aisles, I notice another woman entering the store. Her red frizzy hair covers her face as she bends down to remove a pebble from her sneakers."
    show alandra normal at Position(xalign=.5, yalign =0.0) with moveinright
    "As she stretches back up, I briefly notice how tall she is before I am drawn in by her yellow eyes, which, combined with her tanned skin, give her a mystic look."
    "Her hips are swaying as she continues into the store, and she portrays the self-confidence and grace of a queen."
    u "Hola, Alandra! How are you doing?"
    "A twenty-something guy that could come straight out of a surfing video pops around the corner and waves at Alandra."
    a "Err, hi Juan. I’m fine. Has the package I ordered two weeks ago arrived yet?"
    j "It has! But are you sure you don’t want {i}my package{/i} instead?"
    "I watch as Alandra slaps Juan square in the face."
    j "Ouch!"
    a "Juan! You’re disgusting!"
    j "What? Can’t blame a guy for trying, am I right?"
    a "Ugh. Just get me my mail."
    j "I’m going, already. Maaan, she’s a tough one to crack."
    "Juan goes behind the counter and picks up a small cardboard box and hands it to Alandra."
    a "Thanks!"
    hide alandra with moveoutleft
    "As Alandra exits the store, I continue browsing the items in the shop. It’s funny how mysterious everyday products become if they are written in another language."
    "Although I speak some Spanish, there are a lot of unfamiliar terms on the packages. Some of the products are also labeled with hand-written words in the local dialect, which I don’t understand at all."
    "I keep walking and choose some items that could come in handy before turning a corner when I crash into something hard."
    mc surprise_blush "Ouch!" with hpunch
    "I rub my head and see Juan evaluating me from top to bottom."
    j "Hola, chica! You should watch where you are going, or you won’t know where you will end up."
    mc "Sorry, I didn’t see you there."
    j "No worries, chica! My name is Juan and I work in this convenience store." 
    j "If there is anything you need, my flower, anything at all, I can help you *wink*."

    menu:
        "(How will I respond?)"
        "Get angry":
            "I got angry"
            jump exit_shop
        "Flirt back":
            "I flirted with him"
            jump exit_shop


    label exit_shop:
    jump day2

label day1_town_hall:
    jump day2

label day1_church:
    jump day2

label day1_bar:
    jump day2

label day1_market:
    jump day2

label day1_hotel:
    jump day2



label day2:

#     n "meets Juan"
#
#     n "get to know locals"
#
#     n "meet the characters"
#
#     nvl clear
#
#     d "the first meeting"
#
#     n "explains why everyone is there"
#
#     d "Social interaction 1"
#
#     n "MC invites someone to a bar (first choice)"
#
#     d "second meeting"
#
#     n "visit to the community. Different comments about the place trigger different reactions and outcomes"
#
#     d "Social Interaction 2"
#
#     n "A local wedding"
#
#     d "third meeting: TBA"
#
#     n "A weekend out"
#
#     d "the shocking truth (can we have some more mush and specialization of characters before this? Or an option to romance or not)"
#
#     d "ending (depending on path)"


    # This ends the game.

    return
