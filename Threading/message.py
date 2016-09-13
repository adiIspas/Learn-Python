import threading

class Message(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())
