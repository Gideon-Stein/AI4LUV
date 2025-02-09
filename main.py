import threading
import queue
from resources.ear import ear
from resources.voice import voice
from resources.brain import brain
from resources.display import display
import hydra
from omegaconf import DictConfig

# Example script to benchmark causal discovery methods.
@hydra.main(version_base=None, config_path="config", config_name="main.yaml")
def main(cfg: DictConfig):


    print(cfg)
    # Create a queue to communicate between threads
    ear_q = queue.Queue()
    speech_q = queue.Queue()
    show_q = queue.Queue()

    ear_thread = threading.Thread(target=ear, args=(ear_q,cfg.ear))
    ear_thread.start()

    brain_thread = threading.Thread(target=brain, args=(ear_q,speech_q, show_q,cfg.brain))
    brain_thread.start()

    voice_thread = threading.Thread(target=voice, args=(speech_q,cfg.voice))
    voice_thread.start()

    display_thread = threading.Thread(target=display, args=(show_q,cfg.display))
    display_thread.start()


  

if __name__ == "__main__":
    main()