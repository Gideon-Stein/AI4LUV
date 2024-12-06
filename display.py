import pyglet
from os import listdir
from os.path import isfile, join




def display(show_q):

    # Create a window
    window = window = pyglet.window.Window(width=1344, height=768)

    mypath = "resources/to_display/"
    file = sorted([mypath + f for f in listdir(mypath) if isfile(join(mypath, f))])[-1]

    global image
    # Load an image
    image = pyglet.image.load(file)

    # Create a label
    label = pyglet.text.Label('Omegalol!',
                            font_name='Times New Roman',
                            font_size=36,
                            x=window.width//2, y=window.height - 50,
                            anchor_x='center', anchor_y='center')

    @window.event
    def on_draw():
        """Clear the window and draw the image and label."""
        window.clear()
        image.blit(0, 0)
        label.draw()

    def update(dt):
        """Update the window."""
        global image
        image = pyglet.image.load(file)


    # Schedule the update function to be called 60 times per second
    pyglet.clock.schedule_interval(update, 1/10)

    # Run the application
    pyglet.app.run()