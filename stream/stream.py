from time import sleep, time, process_time


class Stream:
    def __init__(self, check_duration: float, strategy):
        self.check_duration = check_duration
        self.strategy = strategy

    def strategy_stream(self):
        while True:
            delay = self.check_duration - 1
            if 1 <= round(time()) % self.check_duration <= 3:
                self.strategy.signal()
                delay = process_time()
            sleep(abs(self.check_duration - delay))
            sleep(self.check_duration)
