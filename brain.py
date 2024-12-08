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


        if result == "sleep_mode":
            show_q.put("speak")
            speech_q.put("Ok. I will go back to my eternal slumber. Farewell cute princess of the south.")
            time.sleep(10)
            show_q.put("sleep")

        elif result == "memory_mode":
            show_q.put("speak")
            speech_q.put("Of course you cutie patotie")
            show_q.put("display")

        elif result == "wake_up":
            show_q.put("face")
            time.sleep(3)
            show_q.put("speak")
            speech_q.put("What do you want darling. I am listening")
            time.sleep(5)
            show_q.put("face")

        elif result  == "reset_description":
            show_q.put("speak")
            speech_q.put("Let's start again.")
            time.sleep(5)
            show_q.put("face")


        elif result  == "finish_description":
            show_q.put("speak")
            speech_q.put("Perfect. Let me think about it.")
            time.sleep(5)
            show_q.put("compute")

        elif result == "love_mode":
            show_q.put("speak")
            speech_q.put("What do you want to see?")
            time.sleep(4)
            show_q.put("face")

        elif  result == "compliment_mode":
            text = get_compliment()
            show_q.put("speak")
            speech_q.put(text)
            time.sleep(30)
            show_q.put("face")

        elif result == "music_mode":
            show_q.put("speak")
            speech_q.put("I push my fingers into my EEEEEEEEEYYYYYYYYYYYYSSSSSSS. It's the only thing that slowly stops the ache." )
            time.sleep(10)
            show_q.put("face")

        elif result == "fail_to_understand":
            show_q.put("speak")
            speech_q.put("I am here to serve.")
            time.sleep(5)
            show_q.put("face")

        elif "image_description:" in result:
            show_q.put("speak")
            speech_q.put("Perfect. Let me think about it.")
            description = result.replace("image_description:", "")
            description = form_prompt(description)
            print(description)
            generate_new_image(prompt=description)
            show_q.put("thinking")
            run_faceswap()
            enhance_faces()
            img_resize()
            show_q.put("speak")
            speech_q.put("Oh God. It is beautiful.")
            time.sleep(4)
            show_q.put("display")




        elif result == "auto_sleep":
            show_q.put("speak")
            speech_q.put("It seems as I am not needed. Good night you cutie patotie.")
            time.sleep(8)
            show_q.put("sleep")
