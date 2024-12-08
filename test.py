import queue
from os.path import isfile, join
from os import listdir
import subprocess



source_path="resources/generated"
intermediate_path="resources/cache"
output_path="resources/to_display"

onlyfiles = sorted([source_path + "/" + f for f in listdir(
source_path) if isfile(join(source_path, f))])

# Define the script to run and its arguments
script_to_run = "python facefusion.py headless-run"
s = " -s ../resources/base_faces/D1.jpg"  
t = " -t ../" + onlyfiles[-1]    # take the last generated image.
o = " -o ../" + intermediate_path + "/step_1.png" 
order = " --face-selector-order right-left"
execute = script_to_run + s + t + o + order
command = "cd facefusion; . ~/anaconda3/etc/profile.d/conda.sh; conda activate facefusion;"  + execute

subprocess.run(command, shell=True)

# Second face
s = " -s ../resources/base_faces/G1.jpg"  
t = " -t ../" + intermediate_path + "/step_1.png"
o = " -o ../" + output_path + "/display.png" 

execute = script_to_run + s + t + o + order
order = " --face-selector-order left-right"
execute = script_to_run + s + t + o + order
command = "cd facefusion; . ~/anaconda3/etc/profile.d/conda.sh; conda activate facefusion;"  + execute

subprocess.run(command, shell=True)
