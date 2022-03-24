define e = Character("Eileen")

label start:
    e "Hi lets enter the room"
    jump Hallway

label NavScreens:
    screen room_nav():
        add "bg_mcroom"
        modal True
        imagebutton auto "bg_mcroom_chair_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Chair")
            unhovered SetVariable("screen_tooltip", "")
            action Jump ("Computer")
        imagebutton auto "back_btn_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Back")
            unhovered SetVariable("screen_tooltip", "")
            action Jump ("Hallway")

    screen hallway_nav():
        add "bg_hallway"
        modal True
        imagebutton auto "bg_hallway_door1_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Door Room")
            unhovered SetVariable("screen_tooltip", "")
            action Jump ("McRoom")


label Hallway:
    call screen hallway_nav
    scene bg_hallway with dissolve
label McRoom:
    call screen room_nav
label Computer:
    scene bg_computer with dissolve
    e "Wow so many games"
    jump McRoom
