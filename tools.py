import replicate
import datetime
from os import listdir
from os.path import isfile, join
import subprocess
import base64


def generate_new_image(
        prompt="A man on the left and a woman on the right that lie in a forest. Frontal view, big faces, high resolution, couple, love",
        model="black-forest-labs/flux-schnell"
):

    output = replicate.run(
    model,
    input={
        "prompt": prompt,
        "aspect_ratio": "16:9"

           },
    )
    # Save the generated image
    with open("resources/generated/" + str(datetime.datetime.now()).replace(" ", "") + ".png", 'wb') as f:
        f.write(output[0].read())
    

def run_faceswap(
        source_path="resources/generated",
        intermediate_path="resources/cache",
        output_path="resources/to_display"
        ):

    onlyfiles = sorted([source_path + "/" + f for f in listdir(
        source_path) if isfile(join(source_path, f))])
    
    # Define the script to run and its arguments
    script_to_run = "python facefusion.py headless-run"
    s = " -s ../resources/base_faces/D1.jpg"  
    t = " -t ../" + onlyfiles[-1]    # take the last generated image.
    o = " -o ../" + intermediate_path + "/step_1.png" 
    order = " --face-selector-order right-left"
    execute = script_to_run + s + t + o + order
    command = "cd facefusion;"  + execute

    subprocess.run(command, shell=True)

    # Second face
    s = " -s ../resources/base_faces/G1.jpg"  
    t = " -t ../" + intermediate_path + "/step_1.png"
    o = " -o ../" + output_path + "/display.png" 

    execute = script_to_run + s + t + o + order
    order = " --face-selector-order left-right"
    execute = script_to_run + s + t + o + order
    command = "cd facefusion;"  + execute

    subprocess.run(command, shell=True)




def get_compliment(prompt=  "I need a cheesy compliment about Dajana , a beautiful young lady that has blond hair, blue eyes, is tiny, has tattos, and has a big bossom. She likes Rock music, the black forest, africa and saving money. She is an architect. Please make it really short."):

    input = {
        "prompt":prompt,
        "max_tokens": 75,
        "temperature": 0.85,
        "system_prompt": "You are an eloquent author",
        "length_penalty": 5.,
        "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
    }
    text = []
    for event in replicate.stream(
        "meta/meta-llama-3-8b-instruct",
        input=input
    ):
        text.append(event.data)
    text = "".join(text)
    text = ".".join(text.split(".")[:-1]) + "."
    return text


def form_prompt(prompt):
    a = "A picture of a man on the left and a woman on the right. They both look very happy together."
    b = "The man is extremely ugly."
    c = "They are both german looking."
    d = "There are no other people in the image."
    return a + b + c + prompt + ", high resolution, happy, uncanny valley"



def enhance_faces(path= "resources/to_display/display.png", out_path="resources/to_display/display_enhanced.png"):

    binary_fc       = open(path, 'rb').read()  # fc aka file_content
    base64_utf8_str = base64.b64encode(binary_fc).decode('utf-8')
    ext     = path.split('.')[-1]
    dataurl = f'data:image/{ext};base64,{base64_utf8_str}'

    input = {
        "img": dataurl
    }

    output = replicate.run(
        "tencentarc/gfpgan:0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c",
        input=input
    )
    with open(out_path, "wb") as file:
        file.write(output.read())