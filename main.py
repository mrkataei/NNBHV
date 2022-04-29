from time import sleep
from stream.stream import Stream
from strategy.strategy import Amir
import threading


Amir_4h_stream = Stream(check_duration=60, strategy=Amir)


def run_strategies(*streams: Stream):
    for stream in streams:
        threading.Thread(target=stream.strategy_stream).start()


if __name__ == '__main__':
    run_strategies(Amir_4h_stream, Amir_4h_stream)
    while True:
        print("Running...")
        sleep(2000000)
