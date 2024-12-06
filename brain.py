import os
import sys
import wave
import json
import pyaudio
from vosk import Model, KaldiRecognizer
import time
from tools import form_prompt, generate_new_image, run_faceswap



def brain(ear_q, speech_q,generate_q):
    # Path to your model directory



    while True:
        result = ear_q.get()

        if result == "wake_up":
            speech_q.put("What do you want darling. I am listening")

        if result == "love_mode":
            speech_q.put("What do you want to see?")
            print("put description")

        elif  result == "compliment_mode":
            speech_q.put("You need to stop being such a god dam cutie patotie." )

        elif result == "music_mode":
            speech_q.put("EYES. It's the only thing that slowly stops the ache." )

        elif result == "fail_to_understand":
            speech_q.put("I am old and my hearing is bad. Sorry.")

        elif "image_description:" in result:
            description = result.replace("image_description:", "")
            description = form_prompt(description)
            print(description)
            generate_new_image(prompt=description)
            run_faceswap()


        elif result == "sleep":
            speech_q.put("I will go back to my eternal slumber. Farewell cute princess of the south.")
            print("UNKNOWN COMMAND")
            print(result)
