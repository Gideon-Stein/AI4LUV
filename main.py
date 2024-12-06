import threading
import queue
import time
from ear import ear
from voice import voice
from brain import brain
from display import display

# Create a queue to communicate between threads
ear_q = queue.Queue()
speech_q = queue.Queue()
generate_q = queue.Queue()
show_q = queue.Queue()
listening_q = queue.Queue()


# Create and start the producer thread
producer_thread = threading.Thread(target=ear, args=(ear_q,))
producer_thread.start()


# Create and start the producer thread
producer_thread = threading.Thread(target=brain, args=(ear_q,speech_q, generate_q))
producer_thread.start()


# Create and start the consumer thread
consumer_thread = threading.Thread(target=voice, args=(speech_q,))
consumer_thread.start()


# Create and start the consumer thread
consumer_thread = threading.Thread(target=display, args=(show_q,))
consumer_thread.start()

# Wait for both threads to finish
producer_thread.join()
consumer_thread.join()