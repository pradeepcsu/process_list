
import time
import psutil

procs =[]

for p in psutil.process_iter():
    if p.status() == 'zombie':
        # print(f"skipping zombie process: {p.pid}")
        # print(f"warning: process {proc} has counter {CACHE[proc]['counter']}")
        continue
    print(p.name())
    procs.append(p.name())

CACHE = {}


def init_proc(proc, timestamp):
    CACHE[proc] = {'occurrences': [timestamp], 'counter': 0}


def handle_process(proc):
    now = time.time()
    p = CACHE.get(proc)

    if not p:
        init_proc(proc, now)
        return

    last_occurrence = p['occurrences'][-1]
    if now - last_occurrence >= 60:
        init_proc(proc, now)
        return

    CACHE[proc]['occurrences'].append(now)
    CACHE[proc]['counter'] += 1

    if CACHE[proc]['counter'] >= 5:
        print(f"warning: process {proc} has counter {CACHE[proc]['counter']}")


for proc in procs:
    handle_process(proc)