schedules = [
    [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
    [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
    [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
]


class Schedule:
    def __init__(self):
        self.schedule = [True] * 41

    def remove(self, interval):
        interv = []
        for time in interval:
            time = time.split(":")
            interv.append(int(((int(time[0]) - 9) * 4) + (int(time[1]) / 15)))
        for i in range(interv[0], interv[1]):
            self.schedule[i] = False

    def find(self, duration):
        duration //= 15
        for i in range(40 - int(duration)):
            if self.schedule[i:i + int(duration)] == [True] * duration:
                time = "%2d:%2d" % (((i // 4) + 9), i % 4)
                return time
        return None


def get_start_time(schedules, duration):
    s = Schedule()
    for person in schedules:
        for interv in person:
            s.remove(interv)
    return s.find(duration)


assert (get_start_time(schedules, 60) == '12:15')
assert (get_start_time(schedules, 90) == None)
