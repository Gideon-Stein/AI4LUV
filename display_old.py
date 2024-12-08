import pyglet
from os import listdir
from os.path import isfile, join
import numpy as np



def display(show_q):
    window = window = pyglet.window.Window(width=1024, height=600)

    mypath = "resources/to_display/"
    global image
    global counter
    global mode
    global counter_direction
    global to_display

    mode = "face"
    counter = 0
    counter_direction = "U"
    # RESOURCES
    #move = np.load("resources/eyes/move.npy")
    move = np.load("resources/eyes/blink.npy")
    image = pyglet.image.load("resources/eyes/base.jpeg")
    m1 = pyglet.image.load("resources/eyes/mouth1.png")
    m2 = pyglet.image.load("resources/eyes/mouth3.png")
    file = "resources/to_display/display_resized.png"

    @window.event
    def on_draw():
        """Clear the window and draw the image and label."""
        window.clear()
        if mode == "face":
            image.blit(250, 500)
            image.blit(750, 500)
            m2.blit(500, 0)
        elif mode == "speak":
             image.blit(250, 500)
             image.blit(750, 500)
             m1.blit(500, 0)
        elif mode == "display": 
            to_display.blit(0, 0)

    def update(dt):
        global counter
        global image
        global to_display
        global mode
        global counter_direction 
        if not show_q.empty():
            mode = show_q.get()
        """Update the window."""
        if mode == "display":
            to_display = pyglet.image.load(file)
        elif mode == "face":
            image.set_bytes('RGB', 3*move.shape[2],move[counter].tobytes())
            if counter_direction == "U":
                counter +=1
                if counter >= (len(move)-1):
                    counter_direction = "D"
            if counter_direction == "D":
                counter -=1
                if counter == 0 :
                    counter_direction = "U"


# Run the applicatio
    # Schedule the update function to be called 60 times per second
    pyglet.clock.schedule_interval(update, 1/20)

    # Create a window

    # Run the application
    pyglet.app.run()