def on_gesture_shake():
    global list2
    list2 = list22[randint(1, 6)]
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

list2: Image = None
list22: List[Image] = []
list22[1] = images.create_image("""
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    """)
list22[2] = images.create_image("""
    . . . . .
    . # . . .
    . . . . .
    . . . # .
    . . . . .
    """)
list22[3] = images.create_image("""
    . . . . .
    . # . . .
    . . # . .
    . . . # .
    . . . . .
    """)
list22[4] = images.create_image("""
    . . . . .
    . # . # .
    . . . . .
    . # . # .
    . . . . .
    """)
list22[5] = images.create_image("""
    . . . . .
    . # . # .
    . . # . .
    . # . # .
    . . . . .
    """)
list22[6] = images.create_image("""
    . . . . .
    . # . # .
    . # . # .
    . # . # .
    . . . . .
    """)