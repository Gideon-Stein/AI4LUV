import pygame
import numpy as np
import os
from resources.tools import generate_starting_image, img_resize


def display(show_q, cfg):

    # Initialize Pygame
    pygame.init()
    generate_starting_image()
    img_resize("static/starting/starting.png","static/starting/starting_resized.png")

    # Set up some constants
    BLACK = (0, 0, 0)
    # Set up the display
    display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Set up the clock
    clock = pygame.time.Clock()

    # Set up the mode
    mode = "sleep"
    counter = 0
    counter2 = 0

    counter_direction2 = "U"
    counter_direction = "U"
    to_display = None

    # Load the resources
    starting = pygame.image.load("static/starting/starting_resized.png").convert()

    image = pygame.image.load("static/eyes/base.jpeg").convert()
    m1 = pygame.image.load("static/eyes/mouth1.png").convert()
    m2 = pygame.image.load("static/eyes/mouth3.png").convert()
    move = np.load("static/eyes/move.npy")
    think = np.load("static/eyes/think.npy")

    # Set up the display file
    file = "static/to_display/display_resized.png"

    # Main loop
    running = True
    while running:

        if not show_q.empty():
            mode = show_q.get()
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Update the mode
        if mode == "display":
            to_display = pygame.image.load(file).convert()
        elif (mode == "face") or (mode == "speak"):
            image = pygame.transform.rotate(pygame.surfarray.make_surface(move[counter]),90)
            # Update the counter
            if counter_direction == "U":
                counter += 1
            if counter >= (len(move)-1):
                counter_direction = "D"
            if counter_direction == "D":
                counter -= 1
            if counter == 0:
                counter_direction = "U"

        elif mode == "thinking":
            image = pygame.transform.rotate(pygame.surfarray.make_surface(think[counter2]),90)
            # Update the counter
            if counter_direction2 == "U":
                counter2 += 1
            if counter2 >= (len(think)-1):
                counter_direction2 = "D"
            if counter_direction2 == "D":
                counter2 -= 1
            if counter2 == 0:
                counter_direction2 = "U"


        if mode == "sleep":
            display.blit(starting,(0,0))
        # Draw the window
        if mode == "face":
            display.fill(BLACK)
            display.blit(image,(0,0))
            display.blit(image,(550,0))
            display.blit(m2,(400, 300))
        elif mode == "speak":
            display.fill(BLACK)
            display.blit(image,(0,0))
            display.blit(image,(550,0))
            display.blit(m1,(400, 300))
        elif mode == "display":
            display.blit(to_display,(0,0))

        elif mode == "thinking":
            display.fill(BLACK)
            display.blit(image,(0,0))
            display.blit(image,(550,0))
            display.blit(m2,(400, 300))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(15)

    # Quit Pygame
    pygame.quit()

