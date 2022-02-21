from old import sleep
from old.Analysis import StrategiesThreads

thread = StrategiesThreads('BTCUSDT', 'ETHUSDT', 'ADAUSDT', 'DOGEUSDT', 'BCHUSDT', 'ETCUSDT')

if __name__ == '__main__':
    thread.start_threads()
    while True:
        print("Running...")
        sleep(2000000)
