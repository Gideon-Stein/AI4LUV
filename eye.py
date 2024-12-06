import pyglet
from os import listdir
from os.path import isfile, join
import numpy as np




move = np.load("resources/eyes/move.npy")
move2 = np.load("resources/eyes/blink.npy")

print(move.shape)
# Create a window
window = window = pyglet.window.Window(width=1344, height=768)
global image
global counter
# Load an image
image = pyglet.image.load("resources/eyes/base.jpeg")
m1 = pyglet.image.load("resources/eyes/mouth1.png")
m2 = pyglet.image.load("resources/eyes/mouth2.png")
m3 = pyglet.image.load("resources/eyes/mouth3.png")
nose = pyglet.image.load("resources/eyes/nose.png")


counter = 0


@window.event
def on_draw():
    """Clear the window and draw the image and label."""
    window.clear()
    image.blit(250, 500)
    image.blit(750, 500)

    m3.blit(500, 0)
    #if counter < 30:
    #if counter > 60:
    #    m3.blit(500, 0)
# SPlit eye left and right. 
# Make default random order to sample.
# change mouth for event
# Check mouse click event. Useful?



def update(dt):
    """Update the window."""
    global image
    global counter
    image.set_bytes('RGB', 3*move.shape[2],move[counter].tobytes())
    counter +=1
    if counter >= len(move): 
        counter = 0 


# Schedule the update function to be called 60 times per second
pyglet.clock.schedule_interval(update, 1/20)

# Run the application
pyglet.app.run()