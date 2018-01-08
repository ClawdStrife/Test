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
image bg airport exit='bg_airport.jpg'
image bg office main='bg_office.png'
image bg office desk = 'bg_desk.jpg'

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
#what_xalign=0.5,
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

#################################################
# The game starts here.
#################################################

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room
    #scene bg office desk with dissolve
    scene bg airport exit
    #show bg office main

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show alandra normal #at Position(xalign=.5, yalign =0.0) with moveinright
    # a "testing character sprites"
    # "alandra"
    l "lucas"
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
        "Yes yiitit ugouyt oiyoiypoy oiyypyi ouyoyo":
            jump user_character
        "No":
            n "This contract is the agreement of employment with UniAid, The Sweet Fruit Company, and the city hall of Macondo."
            # n "Two years ago, The Sweet Fruit Company approached the Macondo city hall with the interest of purchasing farm land."
            # n "This land is owned by Macondo, however it is leased out to locals on the purpose to farm crops to feed their families and make an extra income."
            # n "For six months, city hall of Macondo debated whether to sell the land or not."
            # n "During the debate, UniAid have spoken openly about the concerns of lost source of income for the locals and introducing non local crops."
            # n "After a year and half, the three parties above have requested to hire a natural facilitator due to unsuccessful attempts to an agreement."
            # nvl clear
            # n "Job requirements:"
            # n "To Attend All Meetings in a neutral location."
            # n "To Run The Meetings, Starting off by going over The Agenda."
            # n "Allowing all parties to speak equally."
            # n "Document what has been agreed and what needs to be further discussed."
            # n "Keep all parties calm and professional."
            # nvl clear
            jump user_character

    label user_character:
    n "By signing this agreement, I agree to the tasks above and will continue to stay neutral throughout the entire session."

    #Use player's name, otherwise use the name 'Mia Caroline'
    $name = str((renpy.input("Signature:", exclude='{1234567890[]!#%\/-_=&?!}', length=8)).strip()) or "M.C."

    mc general "test general face and name"
    mc blush "test blush"
    mc awkward "test awkward"
    mc angry "test angry"
    mc determined "test determined"
    mc happy_blush "test happy blush"
    mc happy "test happy"
    mc miserable "test miserable"
    mc naughty_thoughts "test naughty thoughts"
    mc pensive "test pensive"
    mc sad "test sad"
    mc smile "test smile"
    mc surprise_blush "test surprise blush"
    mc surprise "test surprise"
    mc wink "test wink"

    d "((ARRIVAL))"

    n "Explains MC background."

menu:
    "what should I do?"
    "Offer a hand to the boy.":
        "The little boy ignores my hand and tries getting up by himself, before falling back down and continuing to cry."
        mc "Oops!"
        jump choice1_done
    "Try to pick the boy up off the ground.":
        mc "Oops-2!"
        jump choice1_done
    "Take out a Band-Aid and offer it to the boy.":
        mc "choice 3 dialog"
        jump choice1_done

label choice1_done:

    d "Exploring the town"

    n "meets Juan"

    n "get to know locals"

    n "meet the characters"

    nvl clear

    d "the first meeting"

    n "explains why everyone is there"

    d "Social interaction 1"

    n "MC invites someone to a bar (first choice)"

    d "second meeting"

    n "visit to the community. Different comments about the place trigger different reactions and outcomes"

    d "Social Interaction 2"

    n "A local wedding"

    d "third meeting: TBA"

    n "A weekend out"

    d "the shocking truth (can we have some more mush and specialization of characters before this? Or an option to romance or not)"

    d "ending (depending on path)"


    # This ends the game.

    return
