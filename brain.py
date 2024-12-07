import os
import sys
import wave
import json
import pyaudio
from vosk import Model, KaldiRecognizer
import time
from tools import form_prompt, generate_new_image, run_faceswap, get_compliment, enhance_faces,img_resize



def brain(ear_q, speech_q,show_q):
    # Path to your model directory



    while True:
        result = ear_q.get()

        if result == "wake_up":
            speech_q.put("What do you want darling. I am listening")
            show_q.put("face")

        if result == "love_mode":
            speech_q.put("What do you want to see?")
        elif  result == "compliment_mode":
            text = get_compliment()
            speech_q.put(text)

        elif result == "music_mode":
            show_q.put("speak")
            speech_q.put("I push my fingers into my EEEEEEEEEYYYYYYYYYYYYSSSSSSS. It's the only thing that slowly stops the ache." )
            time.sleep(6)
            show_q.put("face")

        elif result == "fail_to_understand":
            speech_q.put("I am old and my hearing is bad. Sorry.")


        elif "image_description:" in result:

            description = result.replace("image_description:", "")
            description = form_prompt(description)
            print(description)
            generate_new_image(prompt=description)
            run_faceswap()
            enhance_faces()
            img_resize()
            speech_q.put("Oh God. It is beautiful.")
            time.sleep(4)
            show_q.put("display")



        elif result == "sleep":
            speech_q.put("I will go back to my eternal slumber. Farewell cute princess of the south.")
            print("UNKNOWN COMMAND")
            print(result)
