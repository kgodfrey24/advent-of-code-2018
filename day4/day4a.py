from collections import defaultdict
from collections import Counter

def split_into_date_and_event(string):
    date = string[1 : string.find("]")]
    event = string[string.find("]") + 2 :]
    return (date, event)

def get_range(tup):
    return range(tup[0], tup[1])

inputs = open("day4/input").read().splitlines()
dates_and_events = map(split_into_date_and_event, inputs)
dates_and_events.sort(key=lambda tup: tup[0])

current_guard = 0
fell_asleep_minute = 0
guard_events = defaultdict(list)

for date_and_event in dates_and_events:
    date = date_and_event[0]
    event = date_and_event[1]
    current_min = int(date[-2:])

    if event.startswith("Guard"):
        current_guard = int(event[event.find("#") + 1 : event.find(" begins")])
        print "Guard change! " + str(current_guard) + " at " + date
    elif event == "falls asleep":
        print "Guard " + str(current_guard) + " fell asleep" + " at " + date
        fell_asleep_minute = current_min
    elif event == "wakes up":
        print "Guard " + str(current_guard) + " wakes up" + " at " + date
        guard_events[current_guard].append((fell_asleep_minute, current_min))
    
sleepiest_guard_id = 0
sleepiest_guard_mins = 0
for guard_id, guard_sleepy_times in guard_events.iteritems():
    total_mins_asleep = 0
    for sleepy_time in guard_sleepy_times:
        total_mins_asleep += sleepy_time[1] - sleepy_time[0]

    if sleepiest_guard_mins < total_mins_asleep:
        sleepiest_guard_mins = total_mins_asleep
        sleepiest_guard_id = guard_id

sleepiest_guard_naps = guard_events[sleepiest_guard_id]
guard_nap_mins = [item for sublist in map(get_range, sleepiest_guard_naps) for item in sublist]
most_common_minute = Counter(guard_nap_mins).most_common(1)[0][0]
print most_common_minute * sleepiest_guard_id