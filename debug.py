import threading
import queue
from resources.ear import ear
from resources.voice import voice
from resources.brain import brain
from resources.display import display
import hydra
from omegaconf import DictConfig

# Example script to benchmark causal discovery methods.
@hydra.main(version_base=None, config_path="config", config_name="debug.yaml")
def main(cfg: DictConfig):


    print(cfg)
    # Create a queue to communicate between threads
    ear_q = queue.Queue()
    speech_q = queue.Queue()
    show_q = queue.Queue()



    ear_q.put("image_description:" + "There is a giant frog in the background.")


    brain_thread = threading.Thread(target=brain, args=(ear_q,speech_q, show_q,cfg.brain))
    brain_thread.start()



  

if __name__ == "__main__":
    main()