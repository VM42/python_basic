import time


class TrafficLight:
    __colours = ['red', 'yellow', 'green']

    def running(self):
        i = 0
        while i < 3:
            if i == 1:
                print(TrafficLight.__colours[i])
                time.sleep(2)
            else:
                print(TrafficLight.__colours[i])
                time.sleep(7)
            i += 1


traffic = TrafficLight()
traffic.running()
