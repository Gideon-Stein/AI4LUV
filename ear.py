import os
import sys
import wave
import json
import pyaudio
from vosk import Model, KaldiRecognizer
import time


def ear(ear_q):
    # Path to your model directory
    model_path = "vosk-model-small-en-us-0.15"

    # Load the Vosk model
    if not os.path.exists(model_path):
        print(f"Model path '{model_path}' does not exist")
        sys.exit(1)

    model = Model(model_path)
    recognizer = KaldiRecognizer(model, 16000)

    # Initialize PyAudio
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    print("Listening...")

    fail_counter = 0 
    listen_mode = "sleep"
    short_memory = []

    try:
        while True:


            data = stream.read(4096)
            if len(data) == 0:
                break
            if not recognizer.AcceptWaveform(data):
                #partial_result = recognizer.PartialResult()
                #print(f"Partial: {json.loads(partial_result)['partial']}")
                #streaming if necessary. 
                pass
            else:
                result = recognizer.Result()
                text = json.loads(result)["text"]
                print(f"Recognized: {text}")

                if listen_mode =="sleep":
                    # call him first to respond to anything.
                    if ("mr cuddles" in result) or ("mr colts" in result) or ("mr cardinals" in result) or ("miss the couples" in result):
                        print("Name called")
                        ear_q.put("wake_up")
                        time.sleep(5)
                        listen_mode = "command"
                        fail_counter = 0

                elif listen_mode == "command":

                    if "sleep mode" in result:
                        ear_q.put("sleep_mode")
                        listen_mode = "sleep"
                    if "memory mode" in result:
                        ear_q.put("memory_mode")
                        listen_mode = "sleep"
                    if ("love mode" in result):
                        ear_q.put("love_mode")
                        time.sleep(5)
                        listen_mode = "description"

                    elif ("compliment mode" in result):
                        ear_q.put("compliment_mode")
                        listen_mode = "sleep"
                    elif ("music mode" in result):
                        ear_q.put("music_mode")
                    else:
                        fail_counter +=1 
                        if fail_counter == 5:
                            ear_q.put("fail_to_understand")
                        if fail_counter == 10: 
                            ear_q.put("auto_sleep")
                            listen_mode = "sleep"

                elif listen_mode == "description":

                    if "reset" in result:
                        ear_q.put("reset_description")
                        time.sleep(5)
                        short_memory = []

                    elif "that's it" in result:
                        listen_mode = "sleep"
                        desc = ",".join(short_memory)
                        # quick bugfix to remove own voice: 
                        desc = desc.replace("what do you want to see", "")
                        desc = desc.replace("what", "")
                        desc = desc.replace("do", "")
                        desc = desc.replace("you", "")
                        desc = desc.replace("want", "")
                        ear_q.put("image_description:" + desc)
                        short_memory = []
                    else:
                        short_memory.append(text)

                    


    except KeyboardInterrupt:
        print("Terminating...")
    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()